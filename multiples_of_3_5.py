def solution(number):
  y = []
  loop = 1
  
  while(loop < number):
    y.append(loop)
    loop = loop + 1

  return sum(filter(lambda x: x%3 == 0 or x%5 == 0, y))
