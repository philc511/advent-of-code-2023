import re

a = 'Game 1:3 red, 2 blue;1 green, 2 blue'
def extract(a, reds, greens, blues):
  match = re.search('Game (\d):(.*)', a)

  id = match.group(1)
  counts = {}
  turn = match.group(2).split(';')
  for b in turn:
    for c in b.strip().split(','):
      d = c.strip().split(' ')
      print(f'{d[1]} {d[0]}')
      counts[d[1]] = counts.get(d[1], 0) + int(d[0])
  print(counts)

  if(counts['red'] <= reds and counts['green'] <= greens and counts['blue'] <= blues):
    return int(id)
  else:
    return 0

sum = 0
with (open('a.txt') as f):
  words = f.readlines()
  for w in words:
    sum = sum + extract(w, 12, 13, 14)
print(sum)
