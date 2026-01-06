import firebase_admin
from firebase_admin import credentials, firestore
import os
from time import time, sleep


import tkinter as tk
from tkinter import ttk

# ---- STATE ----
current_total = 0
paused = False
time_left = 120



# Initialize Firebase
cred = credentials.Certificate("the-chase-data-firebase-adminsdk-fbsvc-df2ae5424f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# Input contestant and episode data
season = input("season: ")
episode = input("episode: ")


contestant1 = input("name1: ")
contestant1gender = input("gender1: ")
contestant1age = input("age1: ")

contestant2 = input("name2: ")
contestant2gender = input("gender2: ")
contestant2age = input("age2: ")

contestant3 = input("name3: ")
contestant3gender = input("gender3: ")
contestant3age = input("age3: ")

contestant4 = input("name4: ")
contestant4gender = input("gender4: ")
contestant4age = input("age4: ")

contestant1cashbuilder = input("cash builder 1: ")
chaser = input("chaser: ")
contestant1offertaken = input("offer taken 1: ")
contestant1madeit = input("made it 1: ")

contestant2cashbuilder = input("cash builder 2: ")
contestant2offertaken = input("offer taken 2: ")
contestant2madeit = input("made it 2: ")

contestant3cashbuilder = input("cash builder 3: ")
contestant3offertaken = input("offer taken 3: ")
contestant3madeit = input("made it 3: ")

contestant4cashbuilder = input("cash builder 4: ")
contestant4offertaken = input("offer taken 4: ")
contestant4madeit = input("made it 4: ")

# Save contestant metadata
contestants = {
    "season": season,
    "episode": episode,
    "chaser": chaser,
    "contestant1": contestant1,
    "contestant1 gender": contestant1gender,
    "contestant1 age": contestant1age,
    "contestant1 cash builder": contestant1cashbuilder,
    "contestant1 offer taken": contestant1offertaken,
    "contestant1 made it": contestant1madeit,
    "contestant2": contestant2,
    "contestant2 gender": contestant2gender,
    "contestant2 age": contestant2age,
    "contestant2 cash builder": contestant2cashbuilder,
    "contestant2 offer taken": contestant2offertaken,
    "contestant2 made it": contestant2madeit,
    "contestant3": contestant3,
    "contestant3 gender": contestant3gender,
    "contestant3 age": contestant3age,
    "contestant3 cash builder": contestant3cashbuilder,
    "contestant3 offer taken": contestant3offertaken,
    "contestant3 made it": contestant3madeit,
    "contestant4": contestant4,
    "contestant4 gender": contestant4gender,
    "contestant4 age": contestant4age,
    "contestant4 cash builder": contestant4cashbuilder,
    "contestant4 offer taken": contestant4offertaken,
    "contestant4 made it": contestant4madeit,
}

db.collection("contestant_data").add(contestants)

# Initializle total score


global target 
target = 0
paused = False
pause_time = 0
current_total = 0



# Function to send final chase events
def send(event, contestant, time_left, target, current_total, chaser, season, episode):
    print(current_total)
    final_chase_event = {
        "chaser": chaser,
        "season": season,
        "episode": episode,
        "event": event,
        "time_left": time_left,
        "contestant": contestant,
        "current_total": current_total,
        "target": target,
    }

    db.collection("final_chase_data").add(final_chase_event)

# Wait to start
input("Press Enter to start clock...")
start_time = time()

start_pause = 0
time_left = 120


paused = False
number_in_final = [contestant1madeit, contestant2madeit, contestant3madeit, contestant4madeit].count("true")

if number_in_final == 0:
    total = 1
else:
    total = number_in_final 

def button_clicked(event, contestant, time_left, current_total, target):
    global paused, pause_start
    global total
    if event == "correct" or event == "correct chaser":
        total += 1
    elif event == "correct pushback":
        total -= 1

    send(event, contestant, time_left, target, total, chaser, season, episode)
    if event == "incorrect chaser" or event == "correct pushback" or event == "incorrect pushback":
        if not paused:
            paused = True
            pause_start = time()
    else:
        paused = False

def unpause_clock():
    global paused, start_time, pause_start

    if paused:
        paused = False
        start_time += time() - pause_start  # ⬅️ compensate for pause
        pause_start = None


root = tk.Tk()
root.title("My First Button")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", padx=20)

right_frame = tk.Frame(main_frame)
right_frame.pack(side="right", padx=40)

button = tk.Button(left_frame, text=(str(contestant1) + " correct"), command=lambda:button_clicked("correct", contestant1, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="green")
button2 = tk.Button(left_frame, text=contestant1 + " incorrect", command=lambda:button_clicked("incorrect", contestant1, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="red")
button3 = tk.Button(left_frame, text=contestant2 + " correct", command=lambda:button_clicked("correct", contestant2, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="green")
button4 = tk.Button(left_frame, text=contestant2 + " incorrect", command=lambda:button_clicked("incorrect", contestant2, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="red")
button5 = tk.Button(left_frame, text=contestant3 + " correct", command=lambda:button_clicked("correct", contestant3, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="green")
button6 = tk.Button(left_frame, text=contestant3 + " incorrect", command=lambda:button_clicked("incorrect", contestant3, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="red")
button7 = tk.Button(left_frame, text=contestant4 + " correct", command=lambda:button_clicked("correct", contestant4, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="green")
button8 = tk.Button(left_frame, text=contestant4 + " incorrect", command=lambda:button_clicked("incorrect", contestant4, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="red")
button9 = tk.Button(left_frame, text="chaser correct", command=lambda:button_clicked("correct chaser", chaser, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="green")
button10 = tk.Button(left_frame, text="chaser incorrect", command=lambda:button_clicked("incorrect chaser", chaser, time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="red")
button11 = tk.Button(left_frame, text="pushback correct", command=lambda:button_clicked("correct pushback", "team", time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="green")
button12 = tk.Button(left_frame, text="pushback incorrect", command=lambda: button_clicked("incorrect pushback", "team", time_left, current_total, target), font=("Helvetica", 22, "bold"), height=2, width = 20, highlightbackground="red")
button13 = tk.Button(left_frame, text="Unpause", command=lambda: unpause_clock(), font=("Helvetica", 22, "bold"), height=2, width = 20)

button.pack(padx=10, pady=1)
button2.pack(padx=10, pady=1)
button3.pack(padx=10, pady=1)
button4.pack(padx=10, pady=1)
button5.pack(padx=10, pady=1)
button6.pack(padx=10, pady=1)
button7.pack(padx=10, pady=1)
button8.pack(padx=10, pady=1)
button9.pack(padx=10, pady=1)
button10.pack(padx=10, pady=1)
button11.pack(padx=10, pady=1)
button12.pack(padx=10, pady=1)
button13.pack(padx=10, pady=1)


time_label_title = tk.Label(
    right_frame,
    text="TIME LEFT",
    font=("Helvetica", 20)
)
time_label_title.pack(pady=(20, 5))

time_label = tk.Label(
    right_frame,
    text="120",
    font=("Helvetica", 48, "bold")
)
time_label.pack(pady=10)


total_label_title = tk.Label(
    right_frame,
    text="CURRENT TOTAL",
    font=("Helvetica", 20)
)
total_label_title.pack(pady=(30, 5))

total_label = tk.Label(
    right_frame,
    text="0",
    font=("Helvetica", 48, "bold")
)
total_label.pack()


start_time = time()
paused = False
pause_offset = 0
time_left = 120


def update_timer():
    global time_left, start_time, target, total

    

    if not paused:
        elapsed = time() - start_time
        time_left = max(-4, 120 - elapsed)



    time_label.config(text=str(int(time_left)))
    total_label.config(text=str(total))


    if time_left > -4:
        root.after(100, update_timer)
    else:
        target = total
        total = 0
        input("press enter for chaser time")
        total = 0
        time_left = 120
        start_time = time()
        root.after(100, update_timer)

update_timer()
root.mainloop()




    



