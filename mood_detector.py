import tkinter as tk
import webbrowser

mood_links = {
    "Happy": "https://youtu.be/KGn-erOG-Bs?si=epe_2W_oFKfY5TSN",
    "Sad": "https://youtu.be/-2RAq5o5pwc?si=xkr1o5yOQkyULhNE",
    "Angry": "https://youtu.be/_51KXfwcPMs?si=6wbtuWEwWH52Gn6f",
    "Relaxed": "https://youtu.be/IImcBEHuDRI?si=NZXM7aAoajxK95qX",
    "Excited": "https://youtu.be/NW6Dgax2d6I?si=dGGM-5yYjmMb4-d8"
}
descriptions = {
    "Happy":"Make a Cheerful Day.",
    "Sad":"Keep some patience and music heals",
    "Angry":"Be Calm and listen",
    "Relaxed":"Relax and listen a music",
    "Excited":"Try to be more Excited"
}
def open_link(mood):
    webbrowser.open(mood_links[mood])
    description_label.config(text=descriptions[mood])

root = tk.Tk()
root.title("Mood Based music lover.")
root.geometry("450x300")

tk.Label(root, text = "Select your mood", font =( "Helvetica",16 )).pack(pady = 10)

for mood in  mood_links:
    tk.Checkbutton(root, text=mood, width=20, command=lambda m=mood: open_link(m)).pack(pady=5)

description_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=350)
description_label.pack(pady = 20)

root.mainloop()
