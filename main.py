from tkinter import *
from PIL import ImageTk, Image
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 3)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = ImageTk.PhotoImage(Image.open("tomato.gif"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=YELLOW, fg=GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, fg=GREEN, highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = Label(text="✓", bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()