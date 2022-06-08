from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
PADDING= 20

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Display
        self.score_display = Label(text=f"Score:{self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_display.grid(column=1, row=0)

        # Question Panel
        self.question_panel = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question_panel.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=FONT
            )
        self.question_panel.grid(column=0, row=1, columnspan=2, padx=PADDING, pady=PADDING)

        # True Button
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, command=self.answer_true)
        self.true_button.grid(column=0, row=2, padx=PADDING, pady=PADDING)

        # False Button
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, command=self.answer_false)
        self.false_button.grid(column=1, row=2, padx=PADDING, pady=PADDING)

        self.get_next_question()

        self.window.mainloop()

    # Display the new question
    def get_next_question(self):

        # Enable buttons when new question appears
        self.true_button.config(state=NORMAL)
        self.false_button.config(state=NORMAL)

        # Set background to white and display new question.
        self.question_panel.config(bg="white")
        q_text = self.quiz.next_question()
        self.question_panel.itemconfig(self.question_text, text=q_text)

    # 
    def game_over(self):
        self.question_panel.config(bg="white")
        self.question_panel.itemconfig(self.question_text, text=f"GAME OVER\n Final Score: {self.quiz.score}")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        
        # Disable the buttons
        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)

        if is_right:
            self.score_display.config(text=f"Score: {self.quiz.score}")
            self.question_panel.config(bg="green")
        else:
            self.question_panel.config(bg="red")
        if self.quiz.still_has_questions():
            self.window.after(3000,self.get_next_question)
        else:
            self.window.after(3000,self.game_over)
