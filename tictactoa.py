from tkinter import * #this is module tkinter which we want for buttons and popups
import tkinter.messagebox #this messagebox is for popup
board=Tk()    #Tk () function to use it we have to make tkinter object 
board.title("tictactao game")
p1_sc=StringVar()
p2_sc=StringVar()
ptr1=0
ptr2=0
flag=True
ctr=0

def play(btn):
   global flag,ctr
   if btn["text"]=="" and flag==True:# checking if button empty and  clicked, if it is then flage is true
    flag=False #set the flag false for that button
    btn["text"]="X" #
    ctr+=1 #tells you if the game is over or not max moves are 9
    Check() # check for who win 
   elif btn["text"]=="" and flag==False: #flag is false for o
    flag=True
    btn["text"]="O"
    ctr+=1
    Check()
   elif btn["text"]!="": #if the btn is not empty then not allowed
       tkinter.messagebox.showinfo("TicTacTOe","not allowed you already click the button!!")

def ClearButton():
    for btn in buttonss :
        btn["text"]="" #i had made array for accessing them in iteration 




def Check():
    global ptr1,ptr2,p1_sc,p2_sc,ctr
    if (button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or  
        button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or  
        button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or  
        button1['text']=='X' and button5['text']=='X' and button9['text']=='X' or  
        button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or  
        button3['text']=='X' and button5['text']=='X' and button7['text']=='X' or  
        button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or  
        button3['text']=='X' and button6['text']=='X' and button9['text']=='X' ):
        #button7['text']=='X' and button6['text']=='X' and button9['text']=='X'
        # here are different 8 cases that can be possible to win the gam
        
        ClearButton()
        tkinter.messagebox.showinfo("tic tac tao","player 1 won [X]")
        ptr1+=1
        ctr=0
        p1_sc.set(ptr1)  # to set or add the score to the player1 score
    elif (button1['text']=='O' and button2['text']=='O' and button3['text']=='O' or  
          button4['text']=='O' and button5['text']=='O' and button6['text']=='O' or  
          button7['text']=='O' and button8['text']=='O' and button9['text']=='O' or  
          button1['text']=='O' and button5['text']=='O' and button9['text']=='O' or  
          button2['text']=='O' and button5['text']=='O' and button8['text']=='O' or  
          button3['text']=='O' and button5['text']=='O' and button7['text']=='O' or  
          button1['text']=='O' and button4['text']=='O' and button7['text']=='O' or  
          button3['text']=='O' and button6['text']=='O' and button9['text']=='O' ):
          #button7['text']=='O' and button6['text']=='O' and button9['text']=='O'
          
          ClearButton()
          tkinter.messagebox.showinfo("tic tac toa","player 2 won[O]")
          ptr2+=1  #for the score player 2 
          ctr=0
          p2_sc.set(ptr2)
    elif(ctr==9): #we completed all 9 moves but not get winner
        ClearButton()
        tkinter.messagebox.showinfo("tic tac toa","it is a tie")

button1= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                 command=lambda: play(button1)) #command works when we click the btn 
button1.grid(row=1,column=0) #for locating the btn it is value of btn on the borad of tictac tao

button2= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                 command=lambda: play(button2))
button2.grid(row=1,column=1)

button3= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                 command=lambda: play(button3))
button3.grid(row=1,column=2)

button4= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                 command=lambda: play(button4))
button4.grid(row=2,column=0)

button5= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                command=lambda: play(button5))
button5.grid(row=2,column=1)

button6= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                command=lambda: play(button6))
button6.grid(row=2,column=2)

button7= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                command=lambda: play(button7))
button7.grid(row=3,column=0)

button8= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                 command=lambda: play(button8))
button8.grid(row=3,column=1)

button9= Button(board,text="",font='times 15 bold',bg='pink',
                 fg='black',bd=5,height=4,width=7,
                command=lambda: play(button9))
button9.grid(row=3,column=2)
label=Label(board,text="player1",font='times 15 bold',bg='green',fg='white')
label.grid(row=4,column=0,columnspan=2)
p1 = Entry(board,textvariable=p1_sc,bd=5,width=6)
p1.grid(row=4,column=2)
label=Label(board,text="player2",font='times 15 bold',bg='blue',fg='white')
label.grid(row=5,column=0,columnspan=2)
p2 = Entry(board,textvariable=p2_sc,bd=5,width=6)
p2.grid(row=5,column=2)
buttonss=[button1,button2,button3,button4,button5,button6,button7,button8,button9]
#this is the array used for clear 
board.mainloop()
