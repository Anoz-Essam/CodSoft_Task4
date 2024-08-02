import random
from tkinter import *

game_choices = ["ROCK","PAPER","SCISSORS"]
player_score = 0
computer_score = 0

def computer_choice():
    global game_choices
    rand = random.randint(0,2)
    choice = game_choices[rand]
    return choice

def decide_winner(person_choice):
    global player_score
    global computer_score
    co_choice = computer_choice()
    you_choice.config(text="You: "+str(person_choice).capitalize())
    comp_choice.config(text="Computer: "+str(co_choice).capitalize())
    if co_choice == person_choice:
        winner_text.config(text= "Draw!")
    elif co_choice == "ROCK" and person_choice == "PAPER": #win
        winner_text.config(text= "You win!")
        player_score += 1
    elif co_choice == "ROCK" and person_choice == "SCISSORS": #lose
        winner_text.config(text= "You lose!")
        computer_score += 1
    elif co_choice == "SCISSORS" and person_choice == "ROCK": #win
        winner_text.config(text= "You win!")
        player_score += 1
    elif co_choice == "SCISSORS" and person_choice == "PAPER": #lose
        winner_text.config(text= "You lose!")
        computer_score += 1
    elif co_choice == "PAPER" and person_choice == "ROCK": #lose
        winner_text.config(text= "You lose!")
        computer_score += 1
    elif co_choice == "PAPER" and person_choice == "SCISSORS": #win
        winner_text.config(text= "You win!")
        player_score += 1
    you_score.config(text='You: '+str(player_score))
    comp_score.config(text='Computer: '+str(computer_score))
    

if __name__ == "__main__":
    root = Tk()
    root.title("Game")
    root.geometry('270x100')
    root.eval('tk::PlaceWindow . center')

    you_score = Label(root, text='You: 0', font=("Calibri", 10))
    you_score.grid(row=2)
    comp_score = Label(root, text='Computer: 0', font=("Calibri", 10))
    comp_score.grid(row=2,column=2)

    you_choice = Label(root, font=("Calibri", 10))
    you_choice.grid(row=3,column=0)
    comp_choice = Label(root, font=("Calibri", 10))
    comp_choice.grid(row=3,column=2 )
    winner_text = Label(root, font=("Calibri", 10))
    winner_text.grid(row=4,column=1,pady=5)

    rock = Button(root, text='Rock', fg='black',command=lambda:decide_winner("ROCK"), width=10).grid(row=5,column=0)
    paper = Button(root, text='Paper', fg='black',command=lambda:decide_winner("PAPER"), width=10).grid(row=5,column=1)
    scissors = Button(root, text='Scissors', fg='black', command=lambda:decide_winner("SCISSORS"),width=10).grid(row=5,column=2)

    root.mainloop()