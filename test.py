
with open("E:/Projects/ILLUSION_1/animation/scenes/e0010/e0010s0030d0010v0010/e0010s0030d0010v0010.", 'r') as infile:
    content = infile.read()

import re

pattern = r"@([^%]+)%([^@%]+)"

matches = re.findall(pattern, content)

pairs = [(match[0], match[1]) for match in matches]


for pair in pairs:
    print(pair[0], pair[1])