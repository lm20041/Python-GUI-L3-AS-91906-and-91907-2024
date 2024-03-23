from tkinter import *
from functools import partial # to prevent unwanted windows

class Converter:
  def __init__(self):
    #common format all buttons
    # Arial size 14 bold with white text
    button_font_12 = ("Arial", "12", "bold")
    button_font_14 = ("Arial", "14", "bold")
    button_font_16 = ("Arial", "16", "bold")
    button_fg = "#FFFFFF"

    # Five E.G
    # self.all_calculations = ['0 F = -17.78 C', '0 C = -17.78 F', '100 C = 212 F', '40 F = 104 C', '-40 C = -40 F', '-40 F = -40 C', '-273.15 C = -273.15 F']
    # six item list
    #self.all_calculations = ['0 F = -18 C', '0 C = 32 F', '30 F is -1 C', '30 C is 86 F', '100 C is 212 F', '40 F is 4 C']


    # set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    # convert button
    self.button_frame = Frame(padx=30, pady=30)
    self.button_frame.grid(row=0)

    # sitch screens button
    self.to_history_button = Button(self.button_frame, text="History / Export", bg="#004C99", fg=button_fg, font=button_font_12, width=12, state=DISABLED, command=self.to_history)
    self.to_history_button.grid(row=1, column=1, padx=5, pady=5)
    # **** Remove when integrating!! ****
    self.to_history_button.config(state=NORMAL)

  def to_history(self):
    DisplayHistory(self)

class DisplayHistory:
  def __init__(self, partner):
    self.history_box = Toplevel()
    # disable help button
    partner.to_history_button.config(state=DISABLED)
    # If users press cross at top, closes help and 'releases' help button
    self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

    self.history_frame = Frame(self.history_box, width=300, height=200)
    self.history_frame.grid()

    self.history_heading_label = Label(self.history_frame, text="History / Export", font=button_font_14)
    self.history_heading_label.grid(row=0)

    # History text and label
    history_text = "Below are your recent CAL - \n showing 3 / 3 CAL. \n ALL CALS are shown to the nearest degree. \n"
    self.text_instructions_label = Label(self.history_frame, text=history_text, width=45, justify="left", wraplength=300, padx=10, pady=10)
    self.text_instructions_label.grid(row=1, padx=10)

    self.all_calcs_label = Label(self.history_frame, bg=background, text="CAL go here", padx=10, pady=10, bg="#ffe6cc", width=40, justify="left")
    self.all_calcs_label.grid(row=2)

    # instuctions for saving files
    save_text = "Either choose a custom file name (and push \n <Export>) or simply push <Export> to save your \n CAL to a text file. if the \n file already exists, it will be overwritten."
    self.save_instructions_label = Label(self.history_frame, text=save_text, wraplength=300, justify="left", width=40, padx=10, pady=10)
    self.save_instructions_label.grid(row=3)

    #filename entry widget, white background to start
    self.filename_entry = Entry(self.history_frame, font=("Arial", "12"), bg="#ffffff", width=25)
    self.filename_entry.grid(row=4)

    self.filename_error_label = Label(self.history_frame, text="Filename error goes here", fg="#9C0000", font=button_font_12)
    self.filename_error_label.grid(row=5)

    self.button_frame = Frame(self.history_frame)
    self.button_frame.grid(row=6)

    self.export_button = Button(self.button_frame, font=button_font_12, text="Export", bg="#004C99", fg="#FFFFFF", width=12)
    self.export_button.grid(row=0, column=0, padx=10, pady=10)

    self.dismiss_button = Button(self.history_frame, font=button_font_12, text="Dismiss", bg="#666666", fg="#FFFFFF", width=12, command=partial(self.close_history, partner))
    self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

  # closes help dialogue (used by button and x at top of dialogue)
  def close_history(self, partner):
      #put help button back to normal...
      partner.to_history_button.config(state=NORMAL)
      self.history_box.destroy()

#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  Converter()
  root.mainloop()