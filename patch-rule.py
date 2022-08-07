import sys
import re
DNS = """
tls://101.6.6.6:853
""".split()
PATTERNS = [(re.compile(i.split('[---]')[0]), i.split('[---]', 1)[1]) for i in r"""
(\s*dns-server\s*=).*[---]\1 tls://101.6.6.6:853
""".split('\n') if i]


def process(fn):
    f = open(fn, 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    for li, l in enumerate(lines):
        fixlineend = l.endswith('\n')
        for p, s in PATTERNS:
            if p.match(l):
                l = p.sub(s, l)
        if fixlineend and not l.endswith('\n'):
            l += '\n'
        lines[li] = l
    f = open(fn, 'w', encoding='utf8')
    f.writelines(lines)
    f.close()


for i in sys.argv[1:]:
    process(i)
