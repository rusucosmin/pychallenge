#http://www.pythonchallenge.com/pc/def/ocr.html

s = ""
with open("3.html") as f:
  for line in f.readlines():
    s += line

for el in s:
  if el >= 'a' and el <= 'z':
    print(el),
