def duplicate_count(text):
  x = text.lower()
  emp_arr = []
  duplication = 0

  for alph in x:
    if alph in emp_arr and emp_arr.count(alph) <= 1:
      duplication = duplication + 1
      emp_arr.append(alph)
    else:
      emp_arr.append(alph)

  return duplication
    
    # Your code goes here
     
