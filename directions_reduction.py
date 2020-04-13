def dirReduc(arr):
  
  s=arr
  
  for x in range(len(s)):

    if x+1 == len(s):
      return s

    if s[x].endswith("TH") and s[x+1].endswith("TH") and s[x] is not s[x+1]:

      s.pop(x)
      s.pop(x)
      return dirReduc(s)

    
    if s[x].endswith("ST") and s[x+1].endswith("ST") and s[x] is not s[x+1]:

      s.pop(x)
      s.pop(x)
      return dirReduc(s)
    
  return s
