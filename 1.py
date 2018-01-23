#http://www.pythonchallenge.com/pc/def/map.html

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s = "map"

def next(x):
  if x >= 'a' and x <= 'z':
    return chr((ord(x) - ord('a') + 2) % 26 + ord('a'))
  return x

def cipher(s):
  return "".join(map(lambda x: next(x), list(s)))

print(" ".join(map(lambda x: cipher(x), s.split(" "))))
