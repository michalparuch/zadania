import sys
  
for line in sys.stdin:
    line = line.strip()
    words = line.split()

dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']

for word in words:
    for a in word.lower():
      if a in dict:
        print '%s\t%s' % (a, 1)