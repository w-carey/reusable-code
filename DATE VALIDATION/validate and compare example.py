#
#
import datetime
#
def compare_dates(date1, date2):
  return {
      date1==date2 : 1,
      date1>date2  : 2,
      date1<date2  : 3
  }.get(True) ## 1 = EQ, 2 = GR, 3 = LT
#
def ValidDate(dt0):
  try:
    dt1 = dt0.split("/")
    datetime.datetime(year=int(dt1[2]),month=int(dt1[1]),day=int(dt1[0]))
    return True
  except:
    return False
#
#

# 1
START_DATE = input("Start date ('DD/MM/YYYY'): ")
#
# 2
while not ValidDate(START_DATE):
  print("ERROR! Input a real start date in the format 'DD/MM/YYYY'!")
  START_DATE = input("Start date: ")
#
# 3
END_DATE = input("Start date ('DD/MM/YYYY'): ")
#
# 4
while not ValidDate(END_DATE):
  print("ERROR! Input a real end date in the format 'DD/MM/YYYY'!")
  END_DATE = input("End date: ")
#
# 5
COMPARE_RESULT = compare_dates(START_DATE, END_DATE)
print({
    1 : "START DATE equal to END DATE",
    2 : "START DATE greater than END DATE",
    3 : "START DATE smaller than END DATE"
}.get(COMPARE_RESULT))
#
