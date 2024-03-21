from tkinter import *

class Converter:
  def __init__(self):
    #Initialise Variables (such as the feedback variable)
    self.var_feedback = StringVar()
    self.var_feedback.set("")

    self.Var_has_error = StringVar()
    self.Var_has_error.set("no")

    #common format all buttons
    # Arial size 14 bold with white text
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"
    # set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()
    self.temp_heading = Label(self.temp_frame, text="Your Temperature Converter", font=("Arial", "16", "bold"))
    self.temp_heading.grid(row=0)

    instructions = "please enter a temperature in either degrees C or F"
    self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left")
    self.temp_instructions.grid(row=1)
    self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
    self.temp_entry.grid(row=2, padx=10, pady=10)
    error = "*Please enter a number"
    self.output_label = Label(self.temp_frame, text="", fg="red")
    self.output_label.grid(row=3)

    # convert button
    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    self.to_celsius_button = Button(self.button_frame, text="To Celsius", bg="#990099", fg=button_fg, font=button_font, width=12, command=lambda: self.temp_convert(-459))
    self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)
    self.to_farenheit_button = Button(self.button_frame, text="To Farenheit", bg="#009900", fg=button_fg, font=button_font, width=12, command=lambda: self.temp_convert(-273))
    self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)
    # sitch screens button
    self.to_help_button = Button(self.button_frame, text="Help / Info", bg="#CC6600", fg=button_fg, font=button_font, width=12)
    self.to_help_button.grid(row=1, column=0, padx=5, pady=5)
    self.to_history_button = Button(self.button_frame, text="History / Export", bg="#004C99", fg=button_fg, font=button_font, width=12, state=DISABLED)
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
      
  #check temp is valid and convert it
  def temp_convert(self, min_val):
    to_convert = self.check_temp(min_val)
    deg_sign = u"\N{DEGREE SIGN}"
    set_feedback = "yes"
    answer = ""
    from_to = ""
    if to_convert != "invalid":
      set_feedback = "No"
      
    elif min_val == -459:
      # do Calulation
      answer = (to_convert - 32) * 5 / 9
      from_to = "{} F{} is {} C{}"
    else:
      answer = to_convert * 1.8 + 32
      from_to = "{} C{} is {} F{}"

    if set_feedback == "yes":
      #(X)-to_convert = self.round_ans(to_convert)
      #(X)-answer = self.round_ans(answer)
      #create user output and add to cal history
      feedback = from_to.format(to_convert, deg_sign, answer, deg_sign)
      self.var_feedback.set(feedback)
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
#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()