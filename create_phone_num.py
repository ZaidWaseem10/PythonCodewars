def create_phone_number(n):
  number = ""
  for x in n:
    number = number + str(x)

  return "("+number[0:3]+")"+" "+number[3:6]+"-"+number[6:10]
