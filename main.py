from tkinter import *

class Converter:
  def __init__(self):
    #common format all buttons
    # Arial size 14 bold with white text
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"
    # set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    # convert button
    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=0)

    # sitch screens button
    self.to_help_button = Button(self.button_frame, text="Help / Info", bg="#CC6600", fg=button_fg, font=button_font, width=12, command=self.to_help)
    self.to_help_button.grid(row=1, column=0, padx=5, pady=5)
  @staticmethod
  def to_help():
    DisplayHelp()
class DisplayHelp:
  def __init__(self):
    background = "#ffe6cc"
    self.help_box = Toplevel()
    self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
    print("you pressed help")
    self.help_frame.grid()
    self.help_heading_label = Label(self.help_frame, bg=background, text="Help / Info", font=("Arial", "14", "bold"))
    self.help_heading_label.grid(row=0)
    help_text = "to use this program, enter a temperature in either degrees C or F and click one of the buttons to convert it to the other... \n \n Note that the program will not work if you enter a temperature that is less than -273.15 degrees Celsius or -459.67 degrees Fahrenheit... \n \n You can also click the 'History / Export' button to see a list of your conversions..."
    self.help_text_label = Label(self.help_frame, bg=background, text=help_text, wrap=350, justify="left")
    self.help_text_label.grid(row=1, padx=10)
    self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"), text="Dismiss", bg="#CC6600", fg="#FFFFFF")
    self.dismiss_button.grid(row=2, padx=10, pady=10)
  
#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()