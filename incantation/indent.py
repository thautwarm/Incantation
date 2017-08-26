
import sys

inp = sys.argv[1]

with open(inp, encoding = 'utf-8') as f:
	s = f.read()
with open(inp,'w', encoding = 'utf-8') as f:
	f.write(s.replace('\t',"    "))

