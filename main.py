import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data


#*function to display the current question and choices
def show_question():
    #? get current question
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    #? display choices in btns 
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    #? clear feedback label and disable the next btn
    feedback_label.config(text="")
    next_btn.config(state="disabled")


#* function to check answer / provide feedback
def check_answer(choice):
    #? get current question
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    #? check answer
    if selected_choice == question["answer"]:
        #? update score
        global score
        score += 1
        feedback_label.config(text="Rätt svar!", foreground="green")
    else: 
        feedback_label.config(text="Fel svar!", foreground="red")

    #? Update the score label
    score_label.config(text="Poäng: {}/{}".format(score, len(quiz_data)))

    #? disable all choices, enable next btn
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")



#* function to show next question
def next_question():
    global current_question
    current_question += 1
    
    if current_question < len(quiz_data):
        #? if more questions, show next question
        show_question()
    else:
        #? if no more questions, show final score
        messagebox.showinfo("Väg Quiz Färdigt", 
                            "Väg Quiz Färdigt! Ditt slutresultat: {}/{}".format(score, len(quiz_data)))
        root.destroy()


#*  main window
root = tk.Tk()
root.title("Väg Quiz")
root.geometry("700x600")
style = Style(theme='solar')

#* configure the font size for the questions and choice btns
style.configure("TLabel", font=("Poppins", 20))
style.configure("TButton", font=("Poppins", 16))

#*  label for question
qs_label = ttk.Label(
    root,
    anchor = "center",
    wraplength=500,
    padding=10
    )
qs_label.pack(pady=10)

#*  choices (buttons)

choice_btns = []

for i in range(4):
    button = ttk.Button(
        root,
        command = lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)


#* feedback label (correct / incorrect / score)

feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)

feedback_label.pack(pady=10)

#* score init
score = 0
#* feedback label (score)

score_label = ttk.Label(
    root,
    text = "Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)

score_label.pack(pady=10)

#*create next button

next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)

next_btn.pack(pady=10)

# init current question index
current_question = 0

#show first question
show_question()

#start main event loop
root.mainloop()