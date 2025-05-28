# Convert Quiz Creator to OOP format

from tkinter import *
from tkinter import messagebox

class QuizCreatorApp(Tk):
    def __init__(self):
        super().__init__()

        # title, icon, size
        self.title("Quiz Creator")
        self.geometry("700x500")
        self.icon_image = PhotoImage(file="Kahoot_Logo.png")
        self.iconphoto(True, self.icon_image)

        # background image
        self.background_image = PhotoImage(file="bg_image.png").subsample(4, 4)
        self.background_label = Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # kahoot image
        self.kahoot_logo_image = PhotoImage(file="kahoot.png").subsample(5, 5)
        self.kahoot_logo_label = Label(self, image=self.kahoot_logo_image)
        self.kahoot_logo_label.place(x=150, y=75)

        # title label
        self.title_label = Label(self, text="Quiz Creator", fg="black")
        self.title_label.place(x=320, y=5)

        # placeholder texts for entries
        self.question_placeholder = "Start typing your question"
        self.option_placeholders = [
            "Add answer 1 (A)", "Add answer 2 (B)",
            "Add answer 3 (C)", "Add answer 4 (D)"
        ]
        self.correct_answer_placeholder = "Correct Answer"
        self.filename_placeholder = "Title of the Quiz"

        self.create_widgets()

    # method to create an entry widget
    def create_entry(self, text, x_position, y_position, width, bg_color, on_focus_in, on_focus_out):
        entry = Entry(
            self,
            font=("Montserrat", 10),
            bg=bg_color,
            fg="gray",
            width=width,
            justify="center"
        )
        entry.insert(0, text)
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        entry.place(x=x_position, y=y_position)
        return entry

    def create_widgets(self):
        # placeholder for filename and focus handling
        self.filename_entry = self.create_entry(
            text=self.filename_placeholder,
            x_position=245,
            y_position=28,
            width=30,
            bg_color="white",
            on_focus_in=self.handle_filename_focus_in,
            on_focus_out=self.handle_filename_focus_out
        )

                # placeholder for question and focus handling
        self.question_entry = self.create_entry(
            text=self.question_placeholder,
            x_position=130,
            y_position=50,
            width=60,
            bg_color="#f2f2f2",
            on_focus_in=self.handle_question_focus_in,
            on_focus_out=self.handle_question_focus_out
        )

    def handle_filename_focus_in(self, event):
        # Remove placeholder in filename entry when focused
        if self.filename_entry.get() == self.filename_placeholder:
            self.filename_entry.delete(0, END)
            self.filename_entry.config(fg="black")

    def handle_filename_focus_out(self, event):
        # Restore placeholder if filename entry left empty
        if self.filename_entry.get() == "":
            self.filename_entry.insert(0, self.filename_placeholder)
            self.filename_entry.config(fg="gray")
    
    def handle_question_focus_in(self, event):
        # Remove placeholder when user focuses on question entry
        if self.question_entry.get() == self.question_placeholder:
            self.question_entry.delete(0, END)
            self.question_entry.config(fg="black")

    def handle_question_focus_out(self, event):
        # Restore placeholder if entry left empty
        if self.question_entry.get() == "":
            self.question_entry.insert(0, self.question_placeholder)
            self.question_entry.config(fg="gray")

# define and instantiate the quiz creator
app = QuizCreatorApp()
app.mainloop()
