from tkinter import *

class Converter:
  def __init__(self):
    # set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()
    self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "16", "bold"))
    self.temp_heading.grid(row=0)

#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()