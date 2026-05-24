from tkinter import*
from tkinter import messagebox
import random
# ---------------- WINDOW ---------------- #

root = Tk()
root.title("💀 Meme Quiz Game")
root.geometry("700x500")
root.config(bg="#121212")

# ---------------- QUIZ DATA ---------------- #

quiz_data = [
{
        "question": "What does 'Bro is cooked 💀' mean?",
        "options": ["He is making food", "He is in trouble", "He is studying", "He is sleeping"],
        "answer": "He is in trouble"
    },

    {
        "question": "What does 'No cap' mean?",
        "options": ["No hat", "Not lying / for real", "No coding", "No money"],
        "answer": "Not lying / for real"
    },

    {
        "question": "What does 'sus' mean?",
        "options": ["Super smart", "Suspicious", "Sad user", "Sleepy"],
        "answer": "Suspicious"
    },

    {
        "question": "Which game made impostor memes famous?",
        "options": ["Minecraft", "PUBG", "Among Us", "Free Fire"],
        "answer": "Among Us"
    },

    {
        "question": "What does 'Rizz' mean?",
        "options": ["Coding skill", "Charisma / Flirting", "Gaming rage", "Dance move"],
        "answer": "Charisma / Flirting"
    }

]

random.shuffle(quiz_data)

# ---------------- VARIABLES ---------------- #

q_no = 0
score = 0

# ---------------- FUNCTIONS ---------------- #

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

# ---------------- MENU ---------------- #

def display_menu():

    clear_screen()

    title = Label(
        root,
        text="💀 QUIZ GAME MENU 💀",
        font=("Arial", 24, "bold"),
        bg="#121212",
        fg="#bb86fc"
    )

    title.pack(pady=30)

    # START QUIZ BUTTON

    Button(
        root,
        text="1. Start Quiz 🎮",
        font=("Arial", 14, "bold"),
        bg="#bb86fc",
        fg="black",
        width=30,
        pady=10,
        command=start_quiz
    ).pack(pady=10)

    # VIEW QUESTIONS

    Button(
        root,
        text="2. View Questions 📚",
        font=("Arial", 14, "bold"),
        bg="#03dac6",
        fg="black",
        width=30,
        pady=10,
        command=view_questions
    ).pack(pady=10)

    # ADD QUESTION

    Button(
        root,
        text="3. Add Question ✨",
        font=("Arial", 14, "bold"),
        bg="#ffb703",
        fg="black",
        width=30,
        pady=10,
        command=add_question
    ).pack(pady=10)

    # DELETE QUESTION

    Button(
        root,
        text="4. Delete Question ❌",
        font=("Arial", 14, "bold"),
        bg="#ff4d6d",
        fg="black",
        width=30,
        pady=10,
        command=delete_question
    ).pack(pady=10)

    # QUIT

    Button(
        root,
        text="5. Quit 💀",
        font=("Arial", 14, "bold"),
        bg="white",
        fg="black",
        width=30,
        pady=10,
        command=root.destroy
    ).pack(pady=20)

# ---------------- START QUIZ ---------------- #

def start_quiz():

    clear_screen()

    global question_label
    global selected_option
    global option1, option2, option3, option4

    question_label = Label(
        root,
        text="",
        font=("Arial", 18, "bold"),
        wraplength=600,
        bg="#121212",
        fg="white"
    )

    question_label.pack(pady=30)

    selected_option = StringVar()

    option1 = Radiobutton(root, variable=selected_option,
                          bg="#121212", fg="white",
                          font=("Arial", 14),
                          selectcolor="#333333")

    option1.pack(anchor="w", padx=120)

    option2 = Radiobutton(root, variable=selected_option,
                          bg="#121212", fg="white",
                          font=("Arial", 14),
                          selectcolor="#333333")

    option2.pack(anchor="w", padx=120)

    option3 = Radiobutton(root, variable=selected_option,
                          bg="#121212", fg="white",
                          font=("Arial", 14),
                          selectcolor="#333333")

    option3.pack(anchor="w", padx=120)

    option4 = Radiobutton(root, variable=selected_option,
                          bg="#121212", fg="white",
                          font=("Arial", 14),
                          selectcolor="#333333")

    option4.pack(anchor="w", padx=120)

    Button(
        root,
        text="Next 💅",
        font=("Arial", 14, "bold"),
        bg="#bb86fc",
        fg="black",
        command=next_question
    ).pack(pady=30)

    load_question()

# ---------------- LOAD QUESTION ---------------- #

def load_question():

    question_label.config(
        text=quiz_data[q_no]["question"]
    )

    options = quiz_data[q_no]["options"]

    option1.config(text=options[0], value=options[0])
    option2.config(text=options[1], value=options[1])
    option3.config(text=options[2], value=options[2])
    option4.config(text=options[3], value=options[3])

    selected_option.set(None)

# ---------------- NEXT QUESTION ---------------- #

def next_question():

    global q_no
    global score

    selected = selected_option.get()

    if selected == "":
        messagebox.showwarning("Oops 😭", "Select an option first!")
        return

    if selected == quiz_data[q_no]["answer"]:
        score += 1

    q_no += 1

    if q_no == len(quiz_data):

        messagebox.showinfo(
            "Quiz Finished 🎉",
            f"Your Score: {score}/{len(quiz_data)}")
        root.destroy()
    else:
        load_question()

    # ---------------- VIEW QUESTIONS ---------------- #

def view_questions():

        questions = ""

        for q in quiz_data:
            questions += f"\nQ: {q['question']}\nAns: {q['answer']}\n"

        messagebox.showinfo("All Questions 📚", questions)

    # ---------------- ADD QUESTION ---------------- #

def add_question():


        add_window = Toplevel(root)

        add_window.title("Add Question ✨")
        add_window.geometry("500x500")
        add_window.config(bg="#121212")

        # ---------- LABELS ---------- #

        Label(
            add_window,
            text="Enter Question",
            bg="#121212",
            fg="white",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        question_entry = Entry(
            add_window,
            width=50,
            font=("Arial", 12)
        )

        question_entry.pack(pady=5)

        # ---------- OPTIONS ---------- #

        option_entries = []

        for i in range(4):
            Label(
                add_window,
                text=f"Option {i + 1}",
                bg="#121212",
                fg="white",
                font=("Arial", 12, "bold")
            ).pack(pady=5)

            entry = Entry(
                add_window,
                width=40,
                font=("Arial", 12)
            )

            entry.pack(pady=5)

            option_entries.append(entry)

        # ---------- ANSWER ---------- #

        Label(
            add_window,
            text="Correct Answer",
            bg="#121212",
            fg="white",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        answer_entry = Entry(
            add_window,
            width=40,
            font=("Arial", 12)
        )

        answer_entry.pack(pady=5)

        # ---------- SAVE FUNCTION ---------- #

        def save_question():

            question = question_entry.get()

            options = []

            for entry in option_entries:
                options.append(entry.get())

            answer = answer_entry.get()

            # CREATE NEW QUESTION

            new_question = {
                "question": question,
                "options": options,
                "answer": answer
            }

            # ADD TO QUIZ DATA

            quiz_data.append(new_question)

            messagebox.showinfo(
                "Success 🎉",
                "New question added successfully!"
            )

            add_window.destroy()

        # ---------- SAVE BUTTON ---------- #

        Button(
            add_window,
            text="Save Question 💾",
            bg="#bb86fc",
            fg="black",
            font=("Arial", 12, "bold"),
            command=save_question
        ).pack(pady=20)

    # ---------------- DELETE QUESTION ---------------- #

def delete_question():


        delete_window = Toplevel(root)

        delete_window.title("Delete Question ❌")
        delete_window.geometry("600x400")
        delete_window.config(bg="#121212")

        Label(
            delete_window,
            text="Select a Question to Delete",
            bg="#121212",
            fg="#ff4d6d",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        # ---------- LISTBOX ---------- #

        listbox = Listbox(
            delete_window,
            width=70,
            height=10,
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="white"
        )

        listbox.pack(pady=20)

        # ADD QUESTIONS TO LISTBOX

        for q in quiz_data:
            listbox.insert(END, q["question"])

        # ---------- DELETE FUNCTION ---------- #

        def remove_question():

            selected = listbox.curselection()

            if not selected:
                messagebox.showwarning(
                    "Oops 😭",
                    "Please select a question first!"
                )
                return

            index = selected[0]

            deleted_question = quiz_data[index]["question"]

            # REMOVE QUESTION

            quiz_data.pop(index)

            # REMOVE FROM LISTBOX

            listbox.delete(index)

            messagebox.showinfo(
                "Deleted ❌",
                f"Question deleted:\n\n{deleted_question}"
            )

        # ---------- DELETE BUTTON ---------- #

        Button(
            delete_window,
            text="Delete Selected 💀",
            bg="#ff4d6d",
            fg="black",
            font=("Arial", 12, "bold"),
            command=remove_question
        ).pack(pady=20)
    # ---------------- START APP ---------------- #

display_menu()

root.mainloop()
            
            
