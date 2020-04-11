def get_middle(s):
  word_middle = len(s)/2
  if (word_middle.is_integer()):
    return s[int(word_middle)-1] + s[int(word_middle)]
  else:
    return s[int(word_middle - 0.5)]
