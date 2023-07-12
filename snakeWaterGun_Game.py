
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox
import string
GAME_WIDTH = 500
GAME_HEIGHT = 500
def choice():
    player1=player_input.get()
    player2=player_input2.get()
    if player1 == player2:
        messagebox.showinfo("Game Result", "IT'S A TIE!")
    elif player1 == 'W':
        if player2 == 'S':
            messagebox.showinfo("Game Result", "Player 1 wins!")
        elif player2 == 'G':
            messagebox.showinfo("Game Result", "Player 2 wins!")
    elif player1 == 'G':
        if player2 == 'S':
            messagebox.showinfo("Game Result", "Player 2 wins!")
        elif player2 == 'W':
            messagebox.showinfo("Game Result", "Player 1 wins!")
    elif player1 == 'S':
        if player2 == 'W':
            messagebox.showinfo("Game Result", "Player 2 wins!")
        elif player2 == 'G':
            messagebox.showinfo("Game Result", "Player 1 wins!")


window = tk.Tk()
window.title("Snake Water and Gun")
window.configure(background="#FFB6C1")
window.iconbitmap('E:\pyton practice\project_SnakeWaterGun_Game\snake.png')
window.resizable(False,False)
label=tk.Label (window,text="SNAKE WATER AND GUN",font=("consolas",40))
label.pack()
img=ImageTk.PhotoImage(Image.open("E:\pyton practice\project_SnakeWaterGun_Game\snake.png"))
img_label=tk.Label(window,image=img)
txt_label=tk.Label(window,text="WELCOME TO THE GAME !!!!!")
img_label.pack(pady=(10,10))
txt_label.pack()
txt_label.config(font=('veranda',18))
player1_turn=tk.Label(window,text='''OPTIONS: 
Choose S for Snake \n Choose W for Water \n Choose G for Gun \n ''',bg='white')
player1_turn.pack(pady=(24,30))
player1_turn.config(font=('Georgia'))
txt=tk.Label(window,text="Player 1",font='Impact')
player_input=tk.Entry(window)
txt.pack(padx=(15,20))
player_input.pack(pady=(10,10))

txt2=tk.Label(window,text="Player 2",font='Impact')
player_input2=tk.Entry(window)
txt2.pack(padx=(10,20))
player_input2.pack(pady=(10,10))

enterb=tk.Button(window,text="Enter",width=15,height=3,command=choice)
enterb.pack()
    
canvas=tk.Canvas(window, bg="#FFB6C1",height=GAME_HEIGHT,width=GAME_HEIGHT)
canvas.pack()
window.update()

window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x = int(screen_width - window_width) // 2
y = int(screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.mainloop()

