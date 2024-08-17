import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
import os
from quiz_data import quiz_data

def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    image_path = question.get("image")
    if image_path:
        full_image_path = os.path.join(os.path.dirname(__file__), image_path)
        if os.path.exists(full_image_path):
            img = Image.open(full_image_path)
            img = img.resize((400, 400), Image.LANCZOS)  # Resize the image
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.image = photo
        else:
            image_label.config(image='')
    else:
        image_label.config(image='')

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        feedback_label.config(text="Rätt svar!", foreground="green")
    else: 
        feedback_label.config(text="Fel svar!", foreground="red")

    score_label.config(text="Poäng: {}/{}".format(score, len(quiz_data)))

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question += 1
    
    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Väg Quiz Färdigt", 
                            "Väg Quiz Färdigt! Ditt slutresultat: {}/{}".format(score, len(quiz_data)))
        root.destroy()

root = tk.Tk()
root.title("Väg Quiz")

# Get the screen height and set the window height to fill the screen
screen_height = root.winfo_screenheight() - 100
window_width = 800  # You can set this to any desired width
root.geometry(f"{window_width}x{screen_height}")

style = Style(theme='cosmo')

style.configure("TLabel", font=("Poppins", 20))
style.configure("TButton", font=("Poppins", 16))

qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

score = 0

score_label = ttk.Label(
    root,
    text="Poäng: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

current_question = 0

show_question()

root.mainloop()
