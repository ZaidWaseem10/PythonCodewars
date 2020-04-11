def order(sentence):
  
  new_arr = sentence.split()
  list_num = ['1','2','3','4','5','6','7','8','9']
  new_sentence = ""

  for j in list_num:
    for x in new_arr:
      if j in x:
        if(new_sentence == ""):
          new_sentence = x
        else:
          new_sentence = new_sentence + " " + x

  return new_sentence
