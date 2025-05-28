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

        # options image
        self.options_image = PhotoImage(file="choices.png").subsample(2, 2)
        self.options_image_label = Label(self, image=self.options_image)
        self.options_image_label.place(x=40, y=300)

        # Entries for the 4 possible answer options
        self.option_entries = []
        option_positions = [(80, 331), (398, 331), (80, 400), (398, 400)]
        for position, placeholder in zip(option_positions, self.option_placeholders):
            entry = self.create_entry(
                text=placeholder,
                x_position=position[0],
                y_position=position[1],
                width=33,
                bg_color="white",
                on_focus_in=self.handle_option_focus_in,
                on_focus_out=self.handle_option_focus_out
            )
            self.option_entries.append(entry)

        # Entry for the correct answer with its placeholder and handlers
        self.correct_answer_entry = self.create_entry(
            text=self.correct_answer_placeholder,
            x_position=550,
            y_position=270,
            width=17,
            bg_color="#fff7e6",
            on_focus_in=self.handle_correct_answer_focus_in,
            on_focus_out=self.handle_correct_answer_focus_out
        )

        self.submit_button = Button(self, text="Submit", font=("Montserrat", 10), command=self.save_to_file)
        self.submit_button.place(x=360, y=460)

        self.exit_button = Button(self, text="Exit", font=("Montserrat", 10), command=self.exit_app)
        self.exit_button.place(x=320, y=460)

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
    
    def handle_option_focus_in(self, event):
        # Remove placeholder for any option entry focused
        if event.widget.get() in self.option_placeholders:
            event.widget.delete(0, END)
            event.widget.config(fg="black")

    def handle_option_focus_out(self, event):
        # Restore placeholder if option entry left empty
        if event.widget.get() == "":
            entry_position = self.option_entries.index(event.widget)
            placeholder_text = self.option_placeholders[entry_position]
            event.widget.insert(0, placeholder_text)
            event.widget.config(fg="gray")

    def handle_correct_answer_focus_in(self, event):
        # Remove placeholder in correct answer entry when focused
        if self.correct_answer_entry.get() == self.correct_answer_placeholder:
            self.correct_answer_entry.delete(0, END)
            self.correct_answer_entry.config(fg="black")

    def handle_correct_answer_focus_out(self, event):
        # Restore placeholder if empty
        if self.correct_answer_entry.get() == "":
            self.correct_answer_entry.insert(0, self.correct_answer_placeholder)
            self.correct_answer_entry.config(fg="gray")

    def save_to_file(self):
        quiz_filename = self.filename_entry.get().strip()
        if quiz_filename == self.filename_placeholder or not quiz_filename:
            messagebox.showwarning("Missing Filename", "Please enter a title")
            return

        correct_answer = self.correct_answer_entry.get().strip().upper()
        if not correct_answer or correct_answer == self.correct_answer_placeholder:
            messagebox.showerror("Invalid Input", "Please enter the correct answer")
            return

        with open(f"{quiz_filename}.txt", "a") as file:
            file.write("Question: " + self.question_entry.get() + "\n")
            file.write("a. " + self.option_entries[0].get() + "\n")
            file.write("b. " + self.option_entries[1].get() + "\n")
            file.write("c. " + self.option_entries[2].get() + "\n")
            file.write("d. " + self.option_entries[3].get() + "\n")
            file.write("Correct answer: " + correct_answer + "\n\n")

        messagebox.showinfo("Notice", "Item saved successfully!")
        self.clear_all_fields()

    def clear_all_fields(self):
        self.question_entry.delete(0, END)
        self.question_entry.insert(0, self.question_placeholder)
        self.question_entry.config(fg="gray")

        for position, entry in enumerate(self.option_entries):
            entry.delete(0, END)
            entry.insert(0, self.option_placeholders[position])
            entry.config(fg="gray")

        self.correct_answer_entry.delete(0, END)
        self.correct_answer_entry.insert(0, self.correct_answer_placeholder)
        self.correct_answer_entry.config(fg="gray")

    def exit_app(self):
        if messagebox.askyesno("Notice", "Are you sure you want to exit?"):
            self.destroy()

# define and instantiate the quiz creator
app = QuizCreatorApp()
app.mainloop()
