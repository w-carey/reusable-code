import datetime
def ValidDate(dt0):
  try:
    dt1 = dt0.split("/")
    datetime.datetime(year=int(dt1[2]),month=int(dt1[1]),day=int(dt1[0]))
    return True
  except:
    return False
  
result = ValidDate("29/02/2025")
print(result)
