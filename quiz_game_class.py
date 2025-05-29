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
        self.window.title(self.filename)
        self.window.geometry("700x380")
        self.window.config(bg="#f2f2f2")

        self.read_quiz_file()
        self.setup_ui()
        self.show_question()
        self.window.mainloop()

    def read_quiz_file(self):
        with open(self.filename, "r") as file:
            lines = [line.strip() for line in file if line.strip() != ""]

        for index in range(0, len(lines), 6):
            question = lines[index].replace("Question: ", "")
            option_a = lines[index + 1].replace("a. ", "")
            option_b = lines[index + 2].replace("b. ", "")
            option_c = lines[index + 3].replace("c. ", "")
            option_d = lines[index + 4].replace("d. ", "")
            correct_letter = lines[index + 5].replace("Correct answer:", "").strip().upper()

            choices = [option_a, option_b, option_c, option_d]
            correct_answer = choices[["A", "B", "C", "D"].index(correct_letter)]

            self.quiz_data.append({
                "question": question,
                "options": choices,
                "answer": correct_answer
            })

        self.shuffled_quiz = random.sample(self.quiz_data, len(self.quiz_data))

    def setup_ui(self):
        self.question_label = Label(
            self.window,
            text="",
            font=("Montserrat Black", 11, "bold"),
            bg="white",
            height=2
        )
        self.question_label.pack(fill="x")

        self.image = PhotoImage(file="image.png").subsample(5, 5)
        self.image_label = Label(self.window, image=self.image)
        self.image_label.pack()

        self.red_button = Button(self.window, bg="#e21b3c", fg="white", font=("Montserrat Black", 10, "bold"),
                                 height=3, padx=165, anchor="center")
        self.red_button.place(x=0, y=260)

        self.blue_button = Button(self.window, bg="#1368ce", fg="white", font=("Montserrat Black", 10, "bold"),
                                  height=3, padx=159, anchor="center")
        self.blue_button.place(x=350, y=260)

        self.orange_button = Button(self.window, bg="#d89e0a", fg="white", font=("Montserrat Black", 10, "bold"),
                                    height=3, padx=165, anchor="center")
        self.orange_button.place(x=0, y=320)

        self.green_button = Button(self.window, bg="#298a11", fg="white", font=("Montserrat Black", 10, "bold"),
                                   height=3, padx=165, anchor="center")
        self.green_button.place(x=350, y=320)

        self.feedback_label = Label(self.window, text="", font=("Montserrat Black", 11, "bold"),
                                    bg="#f2f2f2", fg="black")
        self.feedback_label.pack()

    def handle_answer(self, selected_text):
        correct = self.shuffled_quiz[self.current_question_index]["answer"]
        if selected_text == correct:
            self.score += 1
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Wrong! Correct answer: {correct}", fg="red")

        self.current_question_index += 1
        if self.current_question_index < len(self.shuffled_quiz):
            self.window.after(1000, self.show_question)
        else:
            self.window.after(1000, self.show_result)

    def show_question(self):
        question = self.shuffled_quiz[self.current_question_index]
        self.question_label.config(text=question["question"])
        self.feedback_label.config(text="")

        self.red_button.config(text=question["options"][0],
                               command=lambda: self.handle_answer(question["options"][0]))
        self.blue_button.config(text=question["options"][1],
                                command=lambda: self.handle_answer(question["options"][1]))
        self.green_button.config(text=question["options"][2],
                                 command=lambda: self.handle_answer(question["options"][2]))
        self.orange_button.config(text=question["options"][3],
                                  command=lambda: self.handle_answer(question["options"][3]))

    def show_result(self):
        self.question_label.config(text="Quiz Finished!")
        self.red_button.place_forget()
        self.blue_button.place_forget()
        self.orange_button.place_forget()
        self.green_button.place_forget()
        self.feedback_label.config(text=f"Your Score: {self.score}/{len(self.shuffled_quiz)}", fg="blue")