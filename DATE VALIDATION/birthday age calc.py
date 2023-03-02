#
import datetime
#
#
def ValidDate(dt0):
  try:
    dt1 = dt0.split("/")
    dt2 = datetime.datetime(day=int(dt1[0]),month=int(dt1[1]),year=int(dt1[2]))
    return dt2
  except:
    return False
#
#
def input_birthday():
  birthday = ValidDate(input("Input date ('DD/MM/YYYY'): "))
  while not birthday:
    birthday = ValidDate(input("Input date ('DD/MM/YYYY'): "))
  return birthday
#
#
def calc_age(birthday):
  days_in_year = datetime.timedelta(365.24219)
  today = datetime.datetime.today()
  return (today - birthday)/ days_in_year
#
#
## MAIN
#
birthday = input_birthday()
age = calc_age(birthday)
print(age)
#
