numbers = {
  'one':'1',
  'two':'2',
  'three':'3',
  'four':'4',
  'five':'5',
  'six':'6',
  'seven':'7',
  'eight':'8',
  'nine':'9',
}
rev_numbers = {
  'eno':'1',
  'owt':'2',
  'eerht':'3',
  'ruof':'4',
  'evif':'5',
  'xis':'6',
  'neves':'7',
  'thgie':'8',
  'enin':'9',
}

with (open('a.txt') as f):
    words = f.readlines()

total = 0

for w in words:
  new_w = w
  if any (num in new_w for num in numbers):
    next_num = min(numbers, key=lambda x:new_w.find(x) if x in new_w else 99)
    new_w = new_w.replace(next_num, numbers[next_num], 1) 
  digits = next(c for c in new_w if c.isdigit()) 

  new_w = w[::-1]
  if any (num in new_w for num in rev_numbers):
    next_num = min(rev_numbers, key=lambda x:new_w.find(x) if x in new_w else 99)
    new_w = new_w.replace(next_num, rev_numbers[next_num], 1) 
  digits= digits + next(c for c in new_w if c.isdigit())

  print(f'{w.strip()} = {digits}')
  total +=int(digits)

print(total)
