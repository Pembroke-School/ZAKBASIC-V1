import tkinter as tk
from gpt4all import GPT4All

# device='amd', device='intel'
model = GPT4All("llama-2-7b-chat.ggmlv3.q4_0.bin")


def send_message():
    user_message = user_input.get()
    if user_message:
        add_message("User:", user_message)
        output = model.generate(user_message, max_tokens=3)
        add_message("ChatGPT:", output)


def add_message(sender, message):
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, sender + " " + message + "\n")
    chat_text.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("ZAK")

# Create a text widget to display the chat messages
chat_text = tk.Text(root, state=tk.DISABLED)
chat_text.pack()

# Create an entry widget for user input
user_input = tk.Entry(root)
user_input.pack()

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Set up the layout
chat_text.pack(fill=tk.BOTH, expand=True)
user_input.pack(fill=tk.BOTH, expand=True)
send_button.pack(fill=tk.BOTH, expand=True)

# Start the GUI main loop
root.mainloop()
