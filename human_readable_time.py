def make_readable(seconds):

  initial = seconds/3600

  hours = int(initial)
  minutes = (initial - hours)*60
  seconds = round((minutes - int(minutes))*60)
  if seconds == 60 : minutes = minutes+1

  return "{:02d}:{:02d}:{:02d}".format(hours, int(minutes), seconds)
