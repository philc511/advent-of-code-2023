import re

a = 'Game 1:3 red, 2 blue;1 green, 2 blue'
def extract(a, limits):
  match = re.search('Game (\d+):(.*)', a)

  id =int( match.group(1))
  turn = match.group(2).split(';')
  for b in turn:
    for c in b.strip().split(','):
      d = c.strip().split(' ')
      print(f'{d[1]} {d[0]}')
      if(int(d[0]) > limits[d[1]]) :
        id = 0
  print(id)
  return id

sum = 0
limits = {}
limits['red']=12
limits['green']=13
limits['blue']=14
with (open('a.txt') as f):
  words = f.readlines()
  for w in words:
    sum = sum + extract(w, limits)
print(sum)
