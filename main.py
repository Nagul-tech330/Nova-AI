import customtkinter as ctk
import speech_recognition as sr
import threading

# ---------- Appearance ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------- Window ----------
app = ctk.CTk()
app.title("Nova AI")
app.geometry("1000x650")

title = ctk.CTkLabel(
    app,
    text="🤖 NOVA AI",
    font=("Segoe UI", 36, "bold")
)
title.pack(pady=25)

subtitle = ctk.CTkLabel(
    app,
    text="Your Personal Voice Assistant",
    font=("Segoe UI", 18)
)
subtitle.pack()

status = ctk.CTkLabel(
    app,
    text="Status: Ready",
    font=("Segoe UI", 16)
)
status.pack(pady=15)

textbox = ctk.CTkTextbox(app, width=750, height=280)
textbox.pack(pady=20)

textbox.insert("end", "Welcome to Nova AI!\n")


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        status.configure(text="🎤 Listening...")
        textbox.insert("end", "\nListening...\n")

        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)

        textbox.insert("end", f"\nYou: {text}\n")
        status.configure(text="✅ Command Received")

    except Exception as e:
        textbox.insert("end", f"\nError: {e}\n")
        status.configure(text="❌ Try Again")


def start():
    threading.Thread(target=listen).start()


button = ctk.CTkButton(
    app,
    text="Start Assistant",
    command=start,
    width=220,
    height=45,
    font=("Segoe UI", 18)
)
button.pack(pady=15)

app.mainloop()