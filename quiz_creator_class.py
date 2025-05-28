# Convert Quiz Creator to OOP format

from tkinter import *

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

        self.question_placeholder = "Start typing your question"
        self.option_placeholders = [
            "Add answer 1 (A)", "Add answer 2 (B)",
            "Add answer 3 (C)", "Add answer 4 (D)"
        ]
        self.correct_answer_placeholder = "Correct Answer"
        self.filename_placeholder = "Title of the Quiz"

        self.create_widgets()

    def create_widgets(self):
        pass

# define and instantiate the quiz creator
app = QuizCreatorApp()
app.mainloop()
