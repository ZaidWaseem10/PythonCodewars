def find_outlier(integers):
  odd_list = list(filter(lambda x: x%2 == 0, integers))
  even_list = list(filter(lambda x: x%2 != 0, integers))

  return odd_list[0] if len(odd_list) == 1 else return even_list[0]
