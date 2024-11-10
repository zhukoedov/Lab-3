import tkinter as tk
from tkinter import ttk
import random


A = 65
Z = 90
a = 97
z = 122


def str_to_part_of_key(source_str):
    ans = 0
    for char in source_str:
        ans *= 10
        char = ord(char)
        if char >= A and char <= Z:
            ans += (char - 64) % 10
        if char >= a and char <= z:
            ans += (char - 96) % 10
    return ans


def str_dicer(source_str):
    numbers = [0, 1, 2, 3, 4, 5]
    random.shuffle(numbers)
    str_part1 = source_str[numbers[0]] + \
        source_str[numbers[1]] + source_str[numbers[2]]
    str_part2 = source_str[numbers[3]] + \
        source_str[numbers[4]] + source_str[numbers[5]]
    return str_part1, str_part2


def key_gen(source_str):
    key = ""
    mid = str_to_part_of_key(source_str)
    begin, end = str_dicer(source_str)
    key = str(begin) + '-' + str(mid) + '-' + str(end)
    return key


def get_n_gen():
    lbl_result['text'] = key_gen(entry.get())


if __name__ == "__main__":

    root = tk.Tk()
    root.geometry('600x560')
    root.title('MEGACHIFFRATOR')

    background_image = tk.PhotoImage(file='boss.png')
    lbl_bg = tk.Label(root, image=background_image)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

    lbl_welcome = ttk.Label(text='Write a source for key')
    lbl_welcome.place(y=300)
    lbl_welcome.pack(anchor='center', pady=10)

    global entry
    entry = ttk.Entry()
    entry.pack(anchor='center', pady=10)

    btn = ttk.Button(text="Click", command=get_n_gen)
    btn.pack(anchor='s', pady=10)

    global lbl_result
    lbl_result = ttk.Label()
    lbl_result.pack(anchor="s", pady=10)

    root.mainloop()
