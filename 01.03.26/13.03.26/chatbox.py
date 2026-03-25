import tkinter as tk

# Function to send message
def send_message():
    user_msg = entry.get()
    chat.insert(tk.END, "You: " + user_msg + "\n")
    
    # Simple bot replies
    if user_msg.lower() == "hello":
        bot_reply = "Hi! How are you?"
    elif user_msg.lower() == "how are you":
        bot_reply = "I am fine 😊"
    elif user_msg.lower() == "bye":
        bot_reply = "Goodbye! Have a nice day."
    else:
        bot_reply = "I don't understand."

    chat.insert(tk.END, "Bot: " + bot_reply + "\n")
    entry.delete(0, tk.END)

# Create window
window = tk.Tk()
window.title("Simple Chatbox")
window.geometry("400x400")

# Chat display area
chat = tk.Text(window, height=20, width=50)
chat.pack()

# Input box
entry = tk.Entry(window, width=30)
entry.pack()

# Send button
send_btn = tk.Button(window, text="Send", command=send_message)
send_btn.pack()

window.mainloop()