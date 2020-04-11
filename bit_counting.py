def countBits(n):
  return len(list(filter(lambda x: x == "1", list(bin(n)[2:]))))
