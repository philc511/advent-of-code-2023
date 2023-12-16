import re

a = 'Game 1:3 red, 2 blue;1 green, 2 blue'
def extract(a):
  match = re.search('Game (\d):(.*)', a)

  id = match.group(1)
  counts = {}
  turn = match.group(2).split(';')
  for b in turn:
    for c in b.split(','):
      d = c.split(' ')
      print(f'{d[1]} {d[0]}')
      counts[d[1]] += int(d[0])
  print(counts)
  
