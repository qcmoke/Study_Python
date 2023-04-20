import os
import tkinter
from tkinter import filedialog


def get_symlinks(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            fullpath = os.path.join(root, name)
            if os.path.islink(fullpath):
                print(f"{fullpath} -> {os.readlink(fullpath)}")
                count += 1

    if count == 0:
        print("该目录下没有软链接！")


if __name__ == '__main__':
    tk = tkinter.Tk()
    tk.withdraw()
    directory = filedialog.askdirectory(
        initialdir='C:\\Users\\'+os.environ.get("username"))
    if len(directory) == 0:
        exit(1)
    get_symlinks(directory)
