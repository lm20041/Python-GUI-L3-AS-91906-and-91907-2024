from tkinter import *

class Converter:
  def __init__(self):
    # set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()
    self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "16", "bold"))
    self.temp_heading.grid(row=0)
    
    instructions = "please enter a temperature in either degrees C or F"
    self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left")
    self.temp_instructions.grid(row=1)
    self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
    self.temp_entry.grid(row=2, padx=10, pady=10)
    error = "*Please enter a number"
    self.temp_error = Label(self.temp_frame, text=error, fg="red")
    self.temp_error.grid(row=3)

#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()