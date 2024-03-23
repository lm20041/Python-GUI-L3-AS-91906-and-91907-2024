from tkinter import *
from functools import partial

class Converter:
    def __init__(self):
        button_font_12 = ("Arial", 12, "bold")
        button_fg = "#FFFFFF"

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_history_button = Button(self.button_frame, text="History / Export", bg="#004C99", fg=button_fg, font=button_font_12, width=12, state=NORMAL, command=self.to_history)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

    def to_history(self):
        DisplayHistory(self)

class DisplayHistory:
    def __init__(self, partner):
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

        history_text = "Below are your recent CAL - \n showing 3 / 3 CAL. \n ALL CALS are shown to the nearest degree. \n"
        self.text_instructions_label = Label(self.history_frame, text=history_text, width=45, justify="left", wraplength=300, padx=10, pady=10)
        self.text_instructions_label.grid(row=1, padx=10)

        self.all_calcs_label = Label(self.history_frame, text="CAL goes here", padx=10, pady=10, bg=self.background, width=40, justify="left")
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

        self.export_button = Button(self.button_frame, font=button_font_12, text="Export", bg="#004C99", fg="#FFFFFF", width=12, command=self.export_history)
        self.export_button.grid(row=0, column=0, padx=10, pady=10)

        self.dismiss_button = Button(self.button_frame, font=button_font_12, text="Dismiss", bg="#666666", fg="#FFFFFF", width=12, command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export_history(self):
        filename = self.filename_entry.get()
        # Add functionality here to save the history to a file with the specified filename
        # Handle filename validation and error messages
        print(f"Exporting history to file: {filename}")

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()