# Convert Quiz Game to OOP

from tkinter import *
import random

class QuizGameApp:
    def __init__(self, filename):
        self.filename = filename
        self.quiz_data = []
        self.shuffled_quiz = []
        self.current_question_index = 0
        self.score = 0

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.geometry("700x380")
        self.window.config(bg="#f2f2f2")

        self.read_quiz_file()
        self.setup_ui()

        self.window.mainloop()

    def read_quiz_file(self):
        pass

    def setup_ui(self):
        pass

    def handle_answer(self):
        pass

    def show_question(self):
        pass

    def show_result(self):
        pass