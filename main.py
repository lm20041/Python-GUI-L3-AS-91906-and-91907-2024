from datetime import date
import re

# retreive date
def get_date():
  today = date.today()
  day = today.strftime("%d")
  month = today.strftime("%m")
  year = today.strftime("%Y")
  return "{}_{}_{}".format(day, month, year)

def check_filename(filename):
  Problem = ""
  # 
  valid_char = "[A-Za-z0-9_]"
  #
  for letter in filename:
    if re.match(valid_char, letter):
      continue
    elif letter == " ":
      Problem = "sorry, no spaces allowed"
    else:
      Problem = ("sorry, no {}'s allowed".format(letter))
    break
  if Problem != "":
    Problem = "{}. Use letters / numbers / underscores only".format(Problem)
  return Problem

def filename_maker(filename):
  #
  if filename == "":
    filename_ok = ""
    date_part = get_date()
    filename = "{}_Temperature_CAL".format(date_part)
  else:
    filename_ok = check_filename(filename)

  if filename_ok == "":
    filename += ".txt"
  else:
    filename = filename_ok
  return filename

# ***** Main Routine *****
test_filenames = ["", "Test.txt", "Test it", "Test"]

for item in test_filenames:
  checked = filename_maker(item)
  print("\n -<", checked)
print("***** end progam *****")