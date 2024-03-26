from tkinter import *
from functools import partial # to prevent unwanted windows
from datetime import date
import re

class Converter:
  def __init__(self):
    #Initialise Variables (such as the feedback variable)
    self.var_feedback = StringVar()
    self.var_feedback.set("")

    self.Var_has_error = StringVar()
    self.Var_has_error.set("no")

    self.all_calculations = []

    #common format all buttons
    # Arial size 14 bold with white text
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"
    # set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()
    # ***** row0 ****** 
    self.temp_heading = Label(self.temp_frame, text="Your Temperature Converter", font=("Arial", "16", "bold"))
    self.temp_heading.grid(row=0)
    # ***** row1 ****** 
    instructions = "please enter a temperature in either degrees C or F"
    self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left")
    self.temp_instructions.grid(row=1)
    # ***** row2 ****** 
    self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
    self.temp_entry.grid(row=2, padx=10, pady=10)
    error = "*Please enter a number"
    # ***** row3 ****** 
    self.output_label = Label(self.temp_frame, text="", fg="red")
    self.output_label.grid(row=3)

    # ***** row4 ****** convert button
    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    self.to_celsius_button = Button(self.button_frame, text="To Celsius", bg="#990099", fg=button_fg, font=button_font, width=12, command=lambda: self.temp_convert(-459))
    self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)
    self.to_farenheit_button = Button(self.button_frame, text="To Farenheit", bg="#009900", fg=button_fg, font=button_font, width=12, command=lambda: self.temp_convert(-273))
    self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)
    # sitch screens button
    self.to_help_button = Button(self.button_frame, text="Help / Info", bg="#CC6600", fg=button_fg, font=button_font, width=12, command=self.to_help)
    self.to_help_button.grid(row=1, column=0, padx=5, pady=5)
    self.to_history_button = Button(self.button_frame, text="History / Export", bg="#004C99", fg=button_fg, font=button_font, width=12, state=DISABLED, command=lambda: self.to_history(self.all_calculations))
    self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

  def check_temp(self, min_value):
    has_error = "no"
    error = "Please enter a number that is more than {}".format(min_value)
    response = self.temp_entry.get()
    try:
      response = float(response)
      if response < min_value:
        has_error = "yes"

    except ValueError:
      has_error = "yes"

    #set Var_has_error so that entry box and labels can be correctly formatted by formatting function
    if has_error == "yes":
      self.Var_has_error.set("yes")
      self.var_feedback.set(error)
      return "invalid"
    else:
      # set to 'no' in case of previous errors
      self.Var_has_error.set("no")
      #return number to be converted and enable history button
      self.to_history_button.config(state=NORMAL)
      return response
  # round
  @staticmethod
  def round_ans( answer):
    var_rounded = round(answer)
    return var_rounded

  #check temp is valid and convert it
  def temp_convert(self, min_val):
    to_convert = self.check_temp(min_val)
    deg_sign = u"\N{DEGREE SIGN}"
    set_feedback = "yes"
    feedback = ""
    answer = ""
    from_to = ""
    if to_convert == "invalid":
      set_feedback = "No"

    elif min_val == -459:
      # do Calulation
      answer = (to_convert-32)*5/9
      from_to = "{} F{} is {} C{}"
    else:
      answer = to_convert * 1.8 + 32
      from_to = "{} C{} is {} F{}"

    if set_feedback == "yes":
      to_convert = self.round_ans(to_convert)
      answer = self.round_ans(to_convert)
      print(answer)
      #create user output and add to cal history
      feedback = from_to.format(to_convert, deg_sign, answer, deg_sign)
      self.var_feedback.set(feedback)
      #add to cal history
      self.all_calculations.append(feedback)
      print(self.all_calculations)
    self.output_answer()

  #shows user output and clears entry widget ready for next calculations
  def output_answer(self):
    output = self.var_feedback.get()
    has_error = self.Var_has_error.get()

    if has_error == "yes":
      # red text, pink entry box
      self.output_label.config(fg="red")
      self.temp_entry.config(bg="pink")
    else:
      self.output_label.config(fg="blue")
      self.temp_entry.config(bg="white")
    self.output_label.config(text=output)
    print(output)

  def to_history(self, all_calculations):
    DisplayHistory(self, all_calculations)
  
  # open help / Info dialogue box
  def to_help(self):
    DisplayHelp(self)

class DisplayHelp:
  def __init__(self, partner):
    #set up dialogue box and background colour
    background = "#ffe6cc"
    self.help_box = Toplevel()
    # disable help button
    partner.to_help_button.config(state=DISABLED)
    # If users press cross at top, closes help and 'releases' help button
    self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

    self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
    print("you pressed help")
    self.help_frame.grid()
    self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info", font=("Arial", "14", "bold"))
    self.help_heading_label.grid(row=0)
    help_text = "to use this program, enter a temperature in either degrees C or F and click one of the buttons to convert it to the other... \n \n Note that the program will not work if you enter a temperature that is less than -273.15 degrees Celsius or -459.67 degrees Fahrenheit... \n \n You can also click the 'History / Export' button to see a list of your conversions..."
    self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wrap=350, justify="left")
    self.help_text_label.grid(row=1, padx=10)
    self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#CC6600", fg="#FFFFFF", command=partial(self.close_help, partner))
    self.dismiss_button.grid(row=2, padx=10, pady=10)

  # closes help dialogue (used by button and x at top of dialogue)
  def close_help(self, partner):
    #put help button back to normal...
    partner.to_help_button.config(state=NORMAL)
    self.help_box.destroy()
  #main routine

class DisplayHistory:
  def __init__(self, partner, calc_list):
    #max number of calculations to be displayed
    max_calcs = 5
    self.var_max_calcs = IntVar()
    self.var_max_calcs.set(max_calcs)

    # set filename var
    self.var_filename = StringVar()
    self.var_today_date = StringVar()
    self.var_calc_list = StringVar()

    #convert cal list to string
    calc_string_text = self.get_cals_string(calc_list)

    self.background = "#ffe6cc"
    button_font_12 = ("Arial", "12", "bold")
    button_font_14 = ("Arial", "14", "bold")
    self.history_box = Toplevel()

    partner.to_history_button.config(state=DISABLED)
    self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

    self.history_frame = Frame(self.history_box, width=300, height=200)
    self.history_frame.grid()
    
    # ***** row0 *****
    self.history_heading_label = Label(self.history_frame, text="History / Export", font=button_font_14)
    self.history_heading_label.grid(row=0)

    # ***** row1 ***** decide which history of calculations to displays
    num_calcs = len(calc_list)
    if num_calcs > max_calcs:
      calc_background = "#FFE6CC" #peach
      showing_all = "here are your recent CALcs \n ({} / {} CAL shown). please export your Cal to see your full cal History".format(max_calcs, num_calcs)
    else:
      calc_background = "#B4FACB" #light green
      showing_all = "here are your recent CALcs"

    # History text and label
    history_text = "{} \n\n ALL CALS are shown to the nearest degree.".format(showing_all)
    self.text_instructions_label = Label(self.history_frame, text=history_text, width=40, justify="left", wraplength=300, padx=10, pady=10)
    self.text_instructions_label.grid(row=1)
    # ***** row2 *****
    self.all_calcs_label = Label(self.history_frame, text=calc_string_text, padx=10, pady=10, bg=calc_background, width=40, justify="left")
    self.all_calcs_label.grid(row=2)
    # ***** row3 *****
    save_text = "Either choose a custom file name (and push \n <Export>) or simply push <Export> to save your \n CAL to a text file. if the \n file already exists, it will be overwritten."
    self.save_instructions_label = Label(self.history_frame, text=save_text, wraplength=300, justify="left", width=40, padx=10, pady=10)
    self.save_instructions_label.grid(row=3)
    # ***** row4 *****
    self.filename_entry = Entry(self.history_frame, font=("Arial", "12"), bg="#ffffff", width=25)
    self.filename_entry.grid(row=4)
    # ***** row5 *****
    self.filename_feedback_label = Label(self.history_frame, text="", fg="#9C0000", wraplength=300, font=button_font_12)
    self.filename_feedback_label.grid(row=5)
    # ***** row6 ***** import button_frame
    self.button_frame = Frame(self.history_frame)
    self.button_frame.grid(row=6)
    # ***** button_frame-row0 *****
    self.export_button = Button(self.button_frame, font=button_font_12, text="Export", bg="#004C99", fg="#FFFFFF", width=12, command=self.make_file)
    self.export_button.grid(row=0, column=0, padx=10, pady=10)

    self.dismiss_button = Button(self.button_frame, font=button_font_12, text="Dismiss", bg="#666666", fg="#FFFFFF", width=12, command=partial(self.close_history, partner))
    self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

  def get_cals_string(self, var_cal):
    #max_calcs
    max_calcs = self.var_max_calcs.get()
    calc_string = ""
    # generate string for writing to file
    oldest_first = ""
    for item in var_cal:
      oldest_first += item + "\n"
    self.var_calc_list.set(oldest_first)

    #work out how many calculations to display
    if len(var_cal) >= max_calcs:
      stop = max_calcs
    else:
      stop = len(var_cal)
    #list all but the last cal
    for item in range(0, stop):
      calc_string += var_cal[len(var_cal) - item -1] + "\n"

    calc_string = calc_string.strip()
    return calc_string

  def make_file(self):
    filename = self.filename_entry.get()

    filename_ok = ""
    date_part = self.get_date()

    if filename == "":
      # get date & create file name
      filename = "{}_Temperature_CAL".format(date_part)
    else:
      # check filename is valid
      filename_ok = self.check_filename(filename)

    if filename_ok == "":
      filename += ".txt"
      success = "Succes! your CAL history has \n been saved as {}".format(filename)
      self.var_filename.set(filename)
      self.filename_feedback_label.config(text=success, fg="dark green")
      self.filename_entry.config(bg="#ffffff")
      # write content to file
      self.write_to_file()
    else:
      self.filename_feedback_label.config(text=filename_ok, fg="dark red")
      self.filename_entry.config(bg="#f8cecc")

  def get_date(self):
    today = date.today()

    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    todays_date = "{}_{}_{}".format(day, month, year)
    self.var_today_date.set(todays_date)

    return "{}_{}_{}".format(year, month, day)

  @staticmethod
  def check_filename(filename):
    problem = ""
    #
    valid_char = "[A-Za-z0-9_]"
    #
    for letter in filename:
      if re.match(valid_char, letter):
        continue
      elif letter == " ":
        problem = "sorry, no spaces allowed"
        return str(problem)
      else:
        problem = str("sorry, no {}'s allowed".format(letter))
        return str(problem)
      break

  def write_to_file(self):
    # retrieve date, filename and CAL history...
    filename = self.var_filename.get()
    date_part = self.var_today_date.get()

    # set up strings to be written to file
    heading = "Temperature Calculator History \n"
    generated = "Generated on: {} \n".format(date_part)
    sub_heading = "Here is your CALs history: \n"
    all_CAL = self.var_calc_list.get()

    to_output_list = [heading, generated, sub_heading, all_CAL]

    # write to file
    # write output to file
    text_file = open(filename, "w+")
    for item in to_output_list:
      text_file.write(item)
      text_file.write("\n")

    # close file
    text_file.close()

  def close_history(self, partner):
    partner.to_history_button.config(state=NORMAL)
    self.history_box.destroy()


if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()