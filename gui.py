import tkinter as tk
import random
from game import Game, load_words

def main():

    words=load_words("words.txt")
    game=None

    root=tk.Tk()
    root.title("Hangman")
    root.geometry("1200x800")
    root.configure(bg="#0998b8")

    label=tk.Label(root, text = "Welcome to Hangman!", bg="#0998b8", font=("Courier",20,"italic"))
    label.pack(pady=30)
    label.pack(padx=10)


    word_label =tk.Label(root,text="",font=("Courier",20,"bold"),bg="#0998b8")
    entry=tk.Entry(root,text="Guess the letter",width=3, font=("Courier", 20),state="disabled")     #textbox 
    message=tk.Label(text="",font=("Courier",20,"bold"),bg="#0998b8")
    strikes=tk.Label(text="",font=("Courier",20),bg="#0998b8")

    def refresh():
        word_label.config(text=game.masked())
        empty=6-game.tries
        strikes.config(text="STRIKES: "+"[X]"*game.tries +"[ ]"*empty)
        if game.victory:
            message.config(text="Yay you won! Here's a star ☆")
            entry.config(state="disabled")
        elif game.loss:
            message.config(text="Oh no! You lost! Better luck next time!")
            entry.config(state="disabled")

    def start_game():
        nonlocal game                       #ovo govori programu da menjamo neku promenljivu koja vec postoji    
        game = Game(random.choice(words))
        entry.config(state="normal")
        entry.focus()                       #ne moras da kliknes textbox da bi pisao
        button.config(state="disabled")
        message.config(text="")
        refresh()

    def submit(event=None):
        text = entry.get().strip().lower()
        entry.delete(0, tk.END)              #ocisti textbox
        if game is None or not text.isalpha():
            return
        game.Round(text[0])                     #samo prvo slovo
        refresh()

    button=tk.Button(root,text="Click me to start!",bg="white",command=start_game)
    button.pack(pady=30)                     #raspored pack odredjuje kojim redosledom ide sta!!! 
    entry.bind("<Return>", submit)            #enter klik da submituje
    word_label.pack(pady=70)

    button.pack(pady=70)
    word_label.pack(pady=70)
    entry.pack(pady=40)
    strikes.pack(pady=20)
    message.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":                  #dupli underscore(dunder) i na pocetku i na kraju su spec. ugradjene stvari u pythonu. kao npr. konstruktor . moze da se koristi sa operator overloading!
    main()                                  #ovo konkretno samo pita da li je trenutni fajl pokrenut direktno, ili importovan? ako je direktno, pokreni f-ju main. da je importovan, __name__ bi bio = gui
