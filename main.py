from tkinter import *
import math
#Constant
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
#time reset
def reset_timer():
    window.after_cancel(timer)
    canvas_variable.itemconfig(canvas_timer , text="00:00")
    title_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps=0
#Timer
def start_timer():
    global reps
    reps+=1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps%8==0:
        counter_timer(long_break)
        title_label.config(text="Break" , fg=RED)
        title_label.place(x=165,y=44)
    elif reps%2==0:
        counter_timer(short_break)
        title_label.config(text="Break", fg=PINK)
        title_label.place(x=165,y=44)
    else:
        counter_timer(work)
        title_label.config(text="Work", fg=GREEN)

#Countdown
def counter_timer(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    canvas_variable.itemconfig(canvas_timer,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000 ,counter_timer ,count-1)
    else:
        start_timer()
        mark=""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            mark="✔"
            checkmark.config(text=mark)
#Setting up the GUI
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100,pady=50,bg=YELLOW)
window.minsize(700,580)
window.maxsize(700,580)
img_tomato = PhotoImage(file="tomato.png")
canvas_variable = Canvas(width=200, height=224,bg=YELLOW , highlightthickness=0)
canvas_variable.create_image(100 ,112 ,image=img_tomato)
canvas_timer = canvas_variable.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME ,30 , "bold"))
canvas_variable.place(x=140,y=80)



#labels configuration :
Label(window,text="Welcome to the most effective technique for studying",font=("courier",12,"bold"),bg=YELLOW).place(x=0,y=0)
title_label = Label(window , text="Timer",font=("courier",25),bg=YELLOW,fg=GREEN)
title_label.place(x=190,y=44)
checkmark = Label(window , text="",font=(14),bg=YELLOW)
checkmark.place(x=226,y=350)

#configuring Buttons
Button(window,text="Start",font=("courier",12),highlightthickness=0,command=start_timer).place(x=80,y=350)
Button(window,text="reset", font=("courier",12),highlightthickness=0,command=reset_timer).place(x=330,y=350)



window.mainloop()
