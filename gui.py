import tkinter as tk
from game import Game

def main():

    root=tk.Tk()
    root.title("Hangman")
    root.geometry("1200x800")
    root.configure(bg="#0998b8")

    label=tk.Label(root, text = "Welcome to Hangman!", bg="#0998b8")
    label.pack(pady=10)
    label.pack(padx=10)

    button=tk.Button(root,text="Click me to start!")
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":     #dupli underscore(dunder) i na pocetku i na kraju su spec. ugradjene stvari u pythonu. kao npr. konstruktor . moze da se koristi sa operator overloading!
    main()                     #ovo konkretno samo pita da li je trenutni fajl pokrenut direktno, ili importovan? ako je direktno, pokreni f-ju main. da je importovan, __name__ bi bio = gui
