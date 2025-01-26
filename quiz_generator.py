import tkinter as tk
from tkinter import messagebox

# Define the Quiz Questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0,  # Position in the options array
    },
    {
        "topic": "Lists",
        "question": "What will be the output of this Python code?",
        "code": "my_list = [1, 2, 3]\nprint(my_list[1])",
        "options": ["1", "2", "3", "Error"],
        "answer": 1,
    },
    # Add more questions here
]

# Function to fetch a question based on topic
def get_question_by_topic(topic):
    for question in questions:
        if question["topic"].lower() == topic.lower():
            return question
    return None

# GUI Design
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Code Quiz Generator")
        self.root.geometry("500x500")

        # Variables
        self.topic_var = tk.StringVar()
        self.selected_option = tk.IntVar()
        self.current_question = None

        # Topic Entry
        tk.Label(root, text="Enter Python Topic (e.g., loops, lists):").pack(pady=10)
        self.topic_entry = tk.Entry(root, textvariable=self.topic_var, width=30)
        self.topic_entry.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Python Question", command=self.generate_question)
        self.generate_button.pack(pady=10)

        # Question Display Area
        self.question_frame = tk.Frame(root)
        self.question_frame.pack(pady=20)

        self.question_label = tk.Label(self.question_frame, text="", wraplength=400, justify="left", font=("Arial", 12))
        self.question_label.pack(pady=5)

        self.code_label = tk.Label(self.question_frame, text="", wraplength=400, justify="left", font=("Courier", 12))
        self.code_label.pack(pady=5)

        self.options_frame = tk.Frame(self.question_frame)
        self.options_frame.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)
        self.submit_button["state"] = "disabled"

        # Feedback Label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.feedback_label.pack(pady=10)

    # Generate a question based on the topic
    def generate_question(self):
        topic = self.topic_var.get().strip()
        if not topic:
            messagebox.showwarning("Input Error", "Please enter a Python topic!")
            return

        question = get_question_by_topic(topic)
        if not question:
            messagebox.showerror("No Questions Found", f"No questions found for topic '{topic}'.")
            return

        self.current_question = question
        self.display_question()

    # Display the question and options
    def display_question(self):
        question = self.current_question

        # Update question and code labels
        self.question_label.config(text=f"Q: {question['question']}")
        self.code_label.config(text=f"Code:\n{question['code']}")

        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        self.selected_option.set(-1)  # Reset selection
        for i, option in enumerate(question["options"]):
            tk.Radiobutton(
                self.options_frame,
                text=option,
                variable=self.selected_option,
                value=i,
                font=("Arial", 10),
            ).pack(anchor="w")

        # Enable submit button
        self.submit_button["state"] = "normal"
        self.feedback_label.config(text="")  # Clear feedback

    # Check the selected answer
    def check_answer(self):
        if self.selected_option.get() == -1:
            messagebox.showwarning("Selection Error", "Please select an answer!")
            return

        correct_answer = self.current_question["answer"]
        if self.selected_option.get() == correct_answer:
            self.feedback_label.config(text="Correct! Well done! 🎉", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again. ❌", fg="red")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
" change the import" 
