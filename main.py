from tkinter import *
from functools import partial
from datetime import date
import re

class Converter:
  def __init__(self):
    button_font_12 = ("Arial", 12, "bold")
    button_fg = "#FFFFFF"
    #5 item list
    #self.all_calculations = ["0 F is -18 C", "0 C is 32 F", "30 F is -1", "30 C is 86 F", "40 F is 4 C"]
    #6 item list
    self.all_calculations = ["0 F is -18 C", "0 C is 32 F", "30 F is -1", "30 C is 86 F", "40 F is 4 C", "100 C is 212 F"]
    # set up GUI frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.button_frame = Frame(padx=30, pady=30)
    self.button_frame.grid(row=0)

    self.to_history_button = Button(self.button_frame, text="History / Export", bg="#004C99", fg=button_fg, font=button_font_12, width=12, state=DISABLED, command=lambda: self.to_history(self.all_calculations))
    self.to_history_button.grid(row=1, column=1, padx=5, pady=5)
    # ***** Remove when integrating *****
    self.to_history_button.config(state=NORMAL)

  def to_history(self, all_calculations):
    DisplayHistory(self, all_calculations)

class DisplayHistory:
  def __init__(self, partner, calc_list):
    #max number of calculations to be displayed
    max_calcs = 5
    self.var_max_calcs = IntVar()
    self.var_max_calcs.set(max_calcs)
    
    # set filename var
    self.var_filename = StringVar()
    self.var_today_date = StringVar()
    
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

    self.history_heading_label = Label(self.history_frame, text="History / Export", font=button_font_14)
    self.history_heading_label.grid(row=0)

    # decide which history of calculations to displays
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

    self.all_calcs_label = Label(self.history_frame, text=calc_string_text, padx=10, pady=10, bg=calc_background, width=40, justify="left")
    self.all_calcs_label.grid(row=2)

    save_text = "Either choose a custom file name (and push \n <Export>) or simply push <Export> to save your \n CAL to a text file. if the \n file already exists, it will be overwritten."
    self.save_instructions_label = Label(self.history_frame, text=save_text, wraplength=300, justify="left", width=40, padx=10, pady=10)
    self.save_instructions_label.grid(row=3)

    self.filename_entry = Entry(self.history_frame, font=("Arial", "12"), bg="#ffffff", width=25)
    self.filename_entry.grid(row=4)

    self.filename_error_label = Label(self.history_frame, text="Filename error goes here", fg="#9C0000", font=button_font_12)
    self.filename_error_label.grid(row=5)

    self.button_frame = Frame(self.history_frame)
    self.button_frame.grid(row=6)

    self.export_button = Button(self.button_frame, font=button_font_12, text="Export", bg="#004C99", fg="#FFFFFF", width=12, command=self.make_file)
    self.export_button.grid(row=0, column=0, padx=10, pady=10)

    self.dismiss_button = Button(self.button_frame, font=button_font_12, text="Dismiss", bg="#666666", fg="#FFFFFF", width=12, command=partial(self.close_history, partner))
    self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

  def get_cals_string(self, var_cal):
    #max_calcs
    max_calcs = self.var_max_calcs.get()
    calc_string = ""
    #work out how many calculations to display
    if len(var_cal) >= max_calcs:
      stop = max_calcs
    else:
      stop = len(var_cal)
    #list all but the last cal
    for item in range(0, stop - 1):
      calc_string += var_cal[len(var_cal) - item -1] + "\n"
    #add last cal
    calc_string += var_cal[-max_calcs]
    return calc_string

  def make_file(self):
    filename = self.filename_entry.get()

    filename_ok = ""
    
    if filename == "":
      # get date & create file name
      date_part = self.get_date()
      filename = "{}_Temperature_CAL".format(date_part)
    else:
      # check filename is valid
      filename_ok = self.check_filename(filename)
      pass

    if filename_ok == "":
      filename += ".txt"
      self.filename_error_label.config("you are ok")
    else:
      self.filename_error_label.config(text=filename_ok)

  def get_date(self):
    today = date.today()
    
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")
    
    todays_date = "{}_{}_{}".format(day, month, year)
    self.var_today_date.set(todays_date)
    
    return "{}_{}_{}".format(year, month, day)

  
  def close_history(self, partner):
    partner.to_history_button.config(state=NORMAL)
    self.history_box.destroy()

# ***** Main Routine *****
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()