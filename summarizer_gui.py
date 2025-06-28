import tkinter as tk
from tkinter import messagebox
from transformers import pipeline

# Load the summarization model explicitly
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    revision="a4f8f3e",
    device=-1  # use CPU; change to 0 if you want to use GPU
)

# Function to summarize the text from user input
def summarize_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    try:
        summary = summarizer(input_text, max_length=50, min_length=25, do_sample=False)
        summary_output.delete("1.0", tk.END)
        summary_output.insert(tk.END, summary[0]['summary_text'])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
app = tk.Tk()
app.title("🧠 AI Text Summarizer")
app.geometry("600x600")
app.configure(bg="#ffffff")

# Input Label
tk.Label(app, text="Enter text to summarize:", font=("Helvetica", 12), bg="#ffffff").pack(pady=10)

# Text Input Box
text_input = tk.Text(app, height=10, width=70, wrap=tk.WORD)
text_input.pack(pady=5)

# Summarize Button
tk.Button(app, text="Summarize", font=("Helvetica", 12), bg="blue", fg="white", command=summarize_text).pack(pady=10)

# Output Label
tk.Label(app, text="Summarized Output:", font=("Helvetica", 12), bg="#ffffff").pack(pady=10)

# Output Box
summary_output = tk.Text(app, height=6, width=70, wrap=tk.WORD, bg="#f0f0f0")
summary_output.pack(pady=5)

# Run the App
app.mainloop()
