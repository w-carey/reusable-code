#
import datetime
#
dt0 = '02/03/2023'
#
def ValidateDate(dt1):
  dt2 = '%d/%m/%Y' ## 'Y' = 2023, 'y' = 23
  try:
    dt3 = datetime.datetime.strptime(dt1, dt2) ## DATE, FORMAT
    return True
  except:
    return False
#
valid = ValidateDate(dt0)
print(valid)
#
