import tkinter as tk
from tkinter import messagebox
import export as ex


r = tk.Tk()
r.title("Judy's Questions")


def input_file():
    x1 = entry1.get()
    return x1


def input_game():
    g1 = entry2.get()
    with open("title.txt", 'w') as f:
        f.writelines(g1)


def answer1():
    messagebox.showinfo(
        title="Answer", message=ex.get_text_for_most_played(input_file()))


def answer2():
    messagebox.showinfo(
        title="Answer", message=ex.get_text_for_sum_sold(input_file()))


def answer3():
    messagebox.showinfo(
        title="Answer", message=ex.get_text_for_selling_avg(input_file()))


def answer4():
    messagebox.showinfo(
        title="Answer", message=ex.get_text_for_count_logest_title(input_file()))


def answer5():
    messagebox.showinfo(
        title="Answer", message=ex.get_text_for_date_avg(input_file()))


def answer6():
    messagebox.showinfo(
        title="Answer", message=ex.get_text_for_game_prop_gui(input_file()))


def answer7():
    messagebox.showinfo(
        title="Answer", message=ex.get_text_for_count_grouped_by_genre_gui(input_file()))


def answer8():
    messagebox.showinfo(
        title="Answer", message=ex.get_text_for_get_date_ordered_gui(input_file()))


def reset(event):
    entry1.delete(0, tk.END)


button0 = tk.Button(r, text="Submit File", width=60, command=input_file)
button0.grid(row=0, column=0, sticky='E')

entry1 = tk.Entry(r)
entry1.insert(0, "Enter File Name Here")
entry1.bind("<Button-1>", reset)
entry1.grid(row=0, column=0, sticky='E')

button1 = tk.Button(
    r, text='What is the title of the most played game (i.e. sold the most copies)?', width=60, command=answer1)
button1.grid(row=1, column=0)


button2 = tk.Button(
    r, text='How many copies have been sold total?', width=60, command=answer2)
button2.grid(row=2, column=0)

button3 = tk.Button(
    r, text='What is the average selling??', width=60, command=answer3)
button3.grid(row=3, column=0)

button4 = tk.Button(
    r, text='How many characters long is the longest title?', width=60, command=answer4)
button4.grid(row=4, column=0)

button5 = tk.Button(
    r, text='What is the average of the release dates?', width=60, command=answer5)
button5.grid(row=5, column=0)

button6 = tk.Button(
    r, text='What properties has a game?', width=60, command=answer6)
button6.grid(row=7, column=0)


button_game_entry = tk.Button(
    r, text="Enter Game and click Here!", command=input_game)
button_game_entry.grid(row=6, column=0, sticky='W')

entry2 = tk.Entry(r)
entry2.grid(row=6, column=0, sticky='E')


button7 = tk.Button(
    r, text='How many games are there grouped by genre?', width=60, command=answer7)
button7.grid(row=8, column=0)

button8 = tk.Button(
    r, text='What is the date ordered list of the games?', width=60, command=answer8)
button8.grid(row=9, column=0)


# for c in sorted(r.children):
#     r.children[c].pack()


r.mainloop()
