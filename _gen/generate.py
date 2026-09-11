# -*- coding: utf-8 -*-
"""Generate content-data.js from the real markdown/text files.
Nothing is rewritten, summarized or invented. Source text is mapped verbatim to HTML."""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def esc(s):
    return html.escape(s, quote=False)

# ---------- inline formatting (shared) ----------
def inline(text, md=True):
    """Escape, then apply inline markdown if md=True. Never drops characters."""
    out = esc(text)
    if md:
        # links [text](url)
        out = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',
                     lambda m: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (m.group(2), m.group(1)), out)
        # bold **text**
        out = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', out)
        # italic *text* (avoid ** already consumed)
        out = re.sub(r'(?<!\*)\*(?!\s)([^*\n]+?)\*(?!\*)', r'<em>\1</em>', out)
        # inline code `code`
        out = re.sub(r'`([^`]+)`', r'<code>\1</code>', out)
    return out

# ---------- Markdown converter (projects + real-markdown thinking files) ----------
def md_to_html(src):
    lines = src.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    html_parts = []
    i = 0
    n = len(lines)
    def close_para(buf):
        if buf:
            html_parts.append('<p>' + '<br>'.join(inline(b) for b in buf) + '</p>')
            buf.clear()
    para = []
    while i < n:
        line = lines[i]
        stripped = line.strip()
        # fenced code
        if stripped.startswith('```'):
            close_para(para)
            i += 1
            code = []
            while i < n and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i += 1
            i += 1
            html_parts.append('<pre><code>' + esc('\n'.join(code)) + '</code></pre>')
            continue
        # blank
        if stripped == '':
            close_para(para); i += 1; continue
        # hr
        if re.match(r'^(-{3,}|\*{3,}|_{3,})$', stripped):
            close_para(para); html_parts.append('<hr>'); i += 1; continue
        # heading
        m = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if m:
            close_para(para)
            lvl = len(m.group(1))
            html_parts.append('<h%d>%s</h%d>' % (lvl, inline(m.group(2)), lvl))
            i += 1; continue
        # table (pipe) — needs a separator row of ---|---
        if stripped.startswith('|') and i + 1 < n and re.match(r'^\|?[\s:|-]+\|[\s:|-]+', lines[i+1].strip()):
            close_para(para)
            def cells(row):
                r = row.strip()
                if r.startswith('|'): r = r[1:]
                if r.endswith('|'): r = r[:-1]
                return [c.strip() for c in r.split('|')]
            header = cells(lines[i]); i += 2
            body = []
            while i < n and lines[i].strip().startswith('|'):
                body.append(cells(lines[i])); i += 1
            t = ['<table><thead><tr>'] + ['<th>%s</th>' % inline(c) for c in header] + ['</tr></thead><tbody>']
            for row in body:
                t.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in row) + '</tr>')
            t.append('</tbody></table>')
            html_parts.append(''.join(t)); continue
        # blockquote
        if stripped.startswith('>'):
            close_para(para)
            q = []
            while i < n and lines[i].strip().startswith('>'):
                q.append(re.sub(r'^\s*>\s?', '', lines[i])); i += 1
            html_parts.append('<blockquote>' + md_to_html('\n'.join(q)) + '</blockquote>')
            continue
        # unordered list
        if re.match(r'^\s*[-*+]\s+', line):
            close_para(para)
            items = []
            while i < n and re.match(r'^\s*[-*+]\s+', lines[i]):
                items.append(re.sub(r'^\s*[-*+]\s+', '', lines[i])); i += 1
            html_parts.append('<ul>' + ''.join('<li>%s</li>' % inline(it) for it in items) + '</ul>')
            continue
        # ordered list
        if re.match(r'^\s*\d+\.\s+', line):
            close_para(para)
            items = []
            while i < n and re.match(r'^\s*\d+\.\s+', lines[i]):
                items.append(re.sub(r'^\s*\d+\.\s+', '', lines[i])); i += 1
            html_parts.append('<ol>' + ''.join('<li>%s</li>' % inline(it) for it in items) + '</ol>')
            continue
        # normal paragraph line
        para.append(stripped); i += 1
    close_para(para)
    return '\n'.join(html_parts)

# ---------- Plain-text converter (research + 2 thinking files) ----------
CN_H2 = re.compile(r'^[一二三四五六七八九十]{1,3}、')
NUM_H3 = re.compile(r'^\d+[\.、]\s?')
UNNUM_H3_PREFIX = ('方法论小结', '小结', '方法论提炼', '背景回顾', '设计推演小结')

def plain_to_html(src):
    """First line = title, second line = subtitle -> returned separately.
    Rest mapped: 一、->h2 ; 1./1、->h3 ; 方法论小结->h3 ; •->li ; tab-rows->table ; else <p>."""
    lines = [l.rstrip() for l in src.replace('\r\n', '\n').replace('\r', '\n').split('\n')]
    # drop leading blanks
    while lines and lines[0].strip() == '':
        lines.pop(0)
    title = lines[0].strip() if lines else ''
    # line 2 is a subtitle ONLY if it is not already a section heading / bullet.
    second = lines[1].strip() if len(lines) > 1 else ''
    is_heading_second = bool(second) and (CN_H2.match(second) or NUM_H3.match(second)
                          or second.startswith('•') or any(second.startswith(p) for p in UNNUM_H3_PREFIX))
    if second and not is_heading_second:
        subtitle = second
        rest = lines[2:]
    else:
        subtitle = ''
        rest = lines[1:]
    parts = []
    i = 0
    n = len(rest)
    while i < n:
        line = rest[i]
        s = line.strip()
        if s == '':
            i += 1; continue
        # tab-separated table block
        if '\t' in line:
            rows = []
            while i < n and '\t' in rest[i]:
                rows.append([c.strip() for c in rest[i].split('\t')]); i += 1
            header = rows[0]
            t = ['<table><thead><tr>'] + ['<th>%s</th>' % inline(c, md=False) for c in header] + ['</tr></thead><tbody>']
            for row in rows[1:]:
                t.append('<tr>' + ''.join('<td>%s</td>' % inline(c, md=False) for c in row) + '</tr>')
            t.append('</tbody></table>')
            parts.append(''.join(t)); continue
        # bullet block
        if s.startswith('•'):
            items = []
            while i < n and rest[i].strip().startswith('•'):
                items.append(rest[i].strip()[1:].strip()); i += 1
            parts.append('<ul>' + ''.join('<li>%s</li>' % inline(it, md=False) for it in items) + '</ul>')
            continue
        # headings
        if CN_H2.match(s):
            parts.append('<h2>%s</h2>' % inline(s, md=False)); i += 1; continue
        if NUM_H3.match(s):
            parts.append('<h3>%s</h3>' % inline(s, md=False)); i += 1; continue
        if any(s.startswith(p) for p in UNNUM_H3_PREFIX):
            parts.append('<h3>%s</h3>' % inline(s, md=False)); i += 1; continue
        parts.append('<p>%s</p>' % inline(s, md=False)); i += 1
    return title, subtitle, '\n'.join(parts)

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# ---------- PROJECT BODIES ----------
PROJECTS = {
    'lovememo': [
        '01-project-background.md','02-user-analysis.md','03-competitive-analysis.md',
        '04-information-architecture.md','05-user-flow.md','06-prd.md','07-review.md',
    ],
    'personal': None,  # set below
    'vybcall': [
        'business-background.md','user-flow.md','information-architecture.md',
        'subscription-flow.md','error-states.md','07-prd.md','08-h5-prototype.md',
        '09-tracking.md','10-development.md','11-launch.md','12-review.md',
    ],
}
PERSONAL_FILES = ['01-prd.md','02-product-positioning.md','03-user-problems.md',
    '04-module-design.md','05-user-flow.md','06-feature-spec.md',
    '07-iteration-plan.md','08-product-review.md']
DIRMAP = {'lovememo':'lovememo','personal':'personal-os','vybcall':'vybcall'}

def split_first_h1(raw):
    """Return (title, remaining_markdown). Title = first '# ' heading text; if none, ''."""
    lines = raw.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    for j, l in enumerate(lines):
        m = re.match(r'^#\s+(.*)$', l.strip())
        if m:
            return m.group(1).strip(), '\n'.join(lines[:j] + lines[j+1:])
    return '', raw

project_docs = {}
project_report = {}
for key, files in [('lovememo', PROJECTS['lovememo']), ('personal', PERSONAL_FILES), ('vybcall', PROJECTS['vybcall'])]:
    d = os.path.join(ROOT, 'content', 'projects', DIRMAP[key])
    used = []
    docs = []
    for fn in files:
        p = os.path.join(d, fn)
        if not os.path.exists(p):
            project_report.setdefault('missing', []).append('%s/%s' % (DIRMAP[key], fn)); continue
        raw = read(p)
        title, rest = split_first_h1(raw)
        html_body = md_to_html(rest)
        docs.append({'title': title, 'html': html_body})
        used.append(fn)
    project_docs[key] = docs
    project_report[key] = used

# ---------- ARTICLES ----------
# (id, relative path, mode)  mode: 'plain' or 'md'
RESEARCH = [
    ('xhs',   'content/research/小红书产品拆解：从“信不信”到“设计怎么服务信任”/小红书产品拆解：从信不信到设计怎么服务信任.md', 'plain'),
    ('qqmusic','content/research/QQ音乐 vs 网易云音乐评论区：从产品基因到AI功能边界/QQ音乐 vs 网易云音乐评论区：从产品基因到AI功能边界.md', 'plain'),
    ('didi',  'content/research/滴滴排队机制拆解：从心理学滥用到AI介入的边界/滴滴排队机制拆解：从心理学滥用到AI介入的边界.md', 'plain'),
    ('moments','content/research/朋友圈碎碎念：从痛点发现到AI介入判断/朋友圈碎碎念：从痛点发现到AI介入判断.md', 'plain'),
    ('personalos','content/research/Personal-OS × AI助手记录功能：从直觉到可落地设计/Personal-OS × AI助手记录功能：从直觉到可落地设计.md', 'plain'),
]
THINKING = [
    ('memory','content/thinking/为什么AI产品越来越像记忆产品？/为什么AI产品越来越像记忆产品？.md', 'md'),
    ('tech',  'content/thinking/产品经理为什么要懂一点技术？/产品经理为什么要懂一点技术？.md', 'md'),
    ('anime', 'content/thinking/AI漫剧为什么今年爆火？/AI漫剧为什么今年爆火？.md', 'plain'),
    ('cart',  'content/thinking/关于购物车的思考/购物车的取舍：一个被大多数人忽略的产品哲学分野.md', 'plain'),
]

def build_group(defs):
    items = {}
    order = []
    report = []
    for idx, (aid, rel, mode) in enumerate(defs):
        p = os.path.join(ROOT, rel.replace('/', os.sep))
        if not os.path.exists(p):
            report.append('MISSING: ' + rel); continue
        raw = read(p)
        if mode == 'plain':
            title, subtitle, body = plain_to_html(raw)
        else:
            # markdown file: title from first # heading, subtitle from first *italic* line
            title, subtitle, body = md_article(raw)
        # per user request: drop the "Thinking板块 · " lead-in from subtitles
        subtitle = re.sub(r'^\s*Thinking\s*板块\s*[·・]\s*', '', subtitle)
        items[aid] = {'no': '%02d' % (idx+1), 'title': title, 'subtitle': subtitle, 'html': body}
        order.append(aid)
        report.append(rel + '  =>  title="%s"' % title)
    return {'order': order, 'items': items}, report

def md_article(raw):
    lines = raw.replace('\r\n','\n').split('\n')
    title = ''
    subtitle = ''
    # find first heading as title
    body_lines = list(lines)
    for j, l in enumerate(lines):
        m = re.match(r'^#\s+(.*)$', l.strip())
        if m:
            title = m.group(1).strip()
            body_lines = lines[j+1:]
            break
    # subtitle: first *...* italic-only line near top
    cleaned = []
    grabbed_sub = False
    for l in body_lines:
        s = l.strip()
        mm = re.match(r'^\*([^*].*?)\*$', s)
        if (not grabbed_sub) and mm and subtitle == '':
            subtitle = mm.group(1).strip(); grabbed_sub = True
            continue
        cleaned.append(l)
    return title, subtitle, md_to_html('\n'.join(cleaned))

research_group, research_report = build_group(RESEARCH)
thinking_group, thinking_report = build_group(THINKING)

research_group['kicker'] = '03 / RESEARCH'
research_group['back'] = '#research'
thinking_group['kicker'] = '04 / THINKING'
thinking_group['back'] = '#thinking'

# ---------- RESOURCES (from links/project-links.md, real URLs only) ----------
RESOURCES = {
    'lovememo': [
        {'label':'Live Demo ↗','sub':'OPEN LIVE PROJECT','url':'https://our-lovememo-rcuv.vercel.app/'},
        {'label':'GitHub ↗','sub':'SOURCE / REPO','url':'https://github.com/carla-guguwwwy051010'},
        {'label':'PRD 文档 ↗','sub':'FEISHU DOC','url':'https://my.feishu.cn/wiki/BmLPwLjfziACD0kP0FkcnZ58nMg?from=from_copylink'},
    ],
    'personal': [
        {'label':'Live Demo ↗','sub':'OPEN LIVE PROJECT','url':'https://personal-os-green-nine.vercel.app/'},
        {'label':'GitHub ↗','sub':'SOURCE / REPO','url':'https://github.com/carla-guguwwwy051010'},
        {'label':'PRD 文档 ↗','sub':'FEISHU DOC','url':'https://my.feishu.cn/wiki/NfdLwDJNViedKBkox0OcFKWCn13?from=from_copylink'},
    ],
    'vybcall': [
        {'label':'H5 Demo ↗','sub':'OPEN LIVE PROJECT','url':'https://kuyin.iflysec.com/grocery/vybcall/index.html?b=1#/'},
        {'label':'GitHub ↗','sub':'SOURCE / REPO','url':'https://github.com/carla-guguwwwy051010'},
        {'label':'墨刀原型 ↗','sub':'INTERACTIVE PROTOTYPE','url':'https://modao.cc/proto/AM6VODUtjwjoydsDThOG/sharing?view_mode=read_only&screen=rbpVSXFU1kby2mQiU'},
        {'label':'PRD 文档 ↗','sub':'FEISHU DOC','url':'https://my.feishu.cn/docx/PbRqdqTjpoA7a2xNOmscWngrn6c?from=from_copylink'},
    ],
}

data = {
    'PROJECT_DOCS': project_docs,
    'RESOURCES': RESOURCES,
    'ARTICLE_DATA': {'research': research_group, 'thinking': thinking_group},
}

out = os.path.join(ROOT, 'content-data.js')
with open(out, 'w', encoding='utf-8') as f:
    f.write('/* AUTO-GENERATED from content/ + links/ by _gen/generate.py. Do not edit by hand. */\n')
    f.write('window.PORTFOLIO_DATA = ')
    f.write(json.dumps(data, ensure_ascii=False))
    f.write(';\n')

# ---------- report ----------
print('=== PROJECT FILES USED ===')
for k in ('lovememo','personal','vybcall'):
    print(k, '->', ', '.join(project_report[k]))
if project_report.get('missing'):
    print('MISSING PROJECT FILES:', project_report['missing'])
print('\n=== RESEARCH ===')
print('\n'.join(research_report))
print('\n=== THINKING ===')
print('\n'.join(thinking_report))
print('\n=== OUTPUT ===')
print(out, '%.1f KB' % (os.path.getsize(out)/1024))
