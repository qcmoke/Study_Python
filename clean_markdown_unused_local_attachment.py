# -*- coding: UTF-8 -*- 
import datetime
import os
import tkinter as tk
import shutil
from tkinter import filedialog as fd
import imghdr
import tkinter.messagebox as mbox

# 只处理的子目录（默认处理所有子目录）
only_dirs = [
    # "source/_posts"  # hexo博客
]

# 排除处理的相对路径子目录，相对于“起始处理目录”（默认不排除）
exclude_dirs = [
    "node_modules",
    ".obsidian",
    ".trash"
]


default_att_dirpath = "./${filename}"


def clean_att_file(start_dirpath, is_clean_all_att, select_att_dirpath):
    start_dirpath = os.path.normpath(start_dirpath).replace('\\', '/')
    if start_dirpath == None or start_dirpath == '' or start_dirpath == '.':
        rs = {"code": -1, "note": "未选择有效目录路径！"}
        print(rs["note"])
        return rs

    # 垃圾桶目录路径
    trash_dir = start_dirpath + "/.trash"

    dirList = []
    for dirpath, dirnames, filenames in os.walk(start_dirpath):
        dirpath = os.path.normpath(dirpath).replace('\\', '/')
        isExclude = False
        for exclude_dir in exclude_dirs:
            if dirpath.startswith(start_dirpath+"/"+exclude_dir):
                isExclude = True
        isDo = True
        for only_dir in only_dirs:
            if not dirpath.startswith(start_dirpath+"/"+only_dir):
                isDo = False
        if (not isExclude) and isDo:
            dirList.append(dirpath)

    has_clean = False
    for dirpath in dirList:
        fileList = os.listdir(dirpath)
        for item_filename in fileList:
            # 只根据markdown文件内容进行处理
            if not item_filename.endswith(".md"):
                continue
            filename_without_extension, extension = os.path.splitext(
                item_filename)

            att_dirpath = ""
            if select_att_dirpath.startswith("./"):
                select_att_dirpath_tmp = ""
                if select_att_dirpath.startswith(default_att_dirpath):
                    select_att_dirpath_tmp = select_att_dirpath.replace(default_att_dirpath, f"/{filename_without_extension}")
                else:
                    select_att_dirpath_tmp = select_att_dirpath.replace("./", "/")
                att_dirpath = dirpath+select_att_dirpath_tmp
            else:
                att_dirpath = select_att_dirpath
            # 只处理markdown所在目录下的同名文件夹
            if not (os.path.exists(att_dirpath) and os.path.isdir(att_dirpath)):
                continue
            att_filenameList = os.listdir(att_dirpath)
            markdown_filepath = dirpath+"/"+item_filename
            with open(markdown_filepath, 'r', encoding='utf-8') as md:
                markdown_content = md.read()
            found_att_filename_list = []
            for att_filename in att_filenameList:
                if markdown_content.find(att_filename) != -1:
                    found_att_filename_list.append(att_filename)
            # 遍历所有附件并删除不存在与markdown文件中的图片
            for att_filename in att_filenameList:
                if att_filename in found_att_filename_list:
                    continue
                att_filepath = att_dirpath+"/" + att_filename
                if (imghdr.what(att_filepath) is None):  # 如果不是图片
                    if not is_clean_all_att:  # 仅清理图片
                        continue
                if not os.path.exists(trash_dir):
                    os.mkdir(trash_dir)
                to_save_file = trash_dir + att_dirpath[len(start_dirpath):] + "/"+att_filename
                to_save_dir = os.path.dirname(to_save_file)
                if not os.path.exists(to_save_dir):
                    os.makedirs(to_save_dir)
                if os.path.exists(to_save_file):
                    # 如果垃圾桶里有同名附件则先删除
                    os.remove(to_save_file)
                    # 不删除的话也可以继续备份垃圾桶里的文件
                    # shutil.copy(to_save_file, trash_dir + "/"+filename_without_extension+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+extension)
                shutil.move(att_filepath, to_save_dir)
                # shutil.copy2(att_filepath, to_save_file)
                # os.remove(att_filepath)
                has_clean = True
                print(f" {att_filepath[len(start_dirpath)+1:]}  ==>  {to_save_dir[len(start_dirpath)+1:]}")

    if has_clean:
        rs = {"code": 1, "note": f'\n已清理完毕，清理掉的附件备份于：{trash_dir} '}
        print(rs["note"])
        return rs
    else:
        rs = {"code": -1, "note": "没有需要清理的附件！"}
        print(rs["note"])
        return rs


def restoreAttFile(start_dirpath):
    start_dirpath = os.path.normpath(start_dirpath).replace('\\', '/')
    if start_dirpath == None or start_dirpath == '' or start_dirpath == '.':
        rs = {"code": -1, "note": "未选择有效目录路径！"}
        print(rs["note"])
        return rs

    # 垃圾桶目录路径
    trash_dir = start_dirpath + "/.trash"

    if not os.path.exists(trash_dir):
        rs = {"code": -1, "note": "没有需要还原的附件！"}
        print(rs["note"])
        return rs

    dirList = []
    for dirpath, dirnames, filenames in os.walk(trash_dir):
        dirpath = os.path.normpath(dirpath).replace('\\', '/')
        dirList.append(dirpath)

    for dirpath in dirList:
        fileList = os.listdir(dirpath)
        for fileName in fileList:
            copy_from = dirpath+"/"+fileName
            if os.path.isfile(copy_from):
                copy_to = start_dirpath + dirpath[len(trash_dir):]
                shutil.move(copy_from, copy_to)
                print(f" {copy_to[len(start_dirpath)+1:]}  <==  {copy_from[len(start_dirpath)+1:]}")

    shutil.rmtree(trash_dir)
    rs = {"code": 1, "note": f'\n附件还原完毕！'}
    print(rs["note"])
    return rs


def show_tip(dict):
    code = dict.get("code")
    note = dict.get("note")
    if code == -1:
        mbox.showwarning("Message", note)
    elif code == 1:
        mbox.showinfo("Message", note)


def buttonHandle(type, att_dirpath_var=None, is_clean_all_att_var=None):
    if type == "clean":
        # 获取起始处理目录的路径
        start_dirpath = fd.askdirectory()
        select_att_dirpath = att_dirpath_var.get()
        is_clean_all_att = is_clean_all_att_var.get()
        dict = clean_att_file(start_dirpath, is_clean_all_att, select_att_dirpath)
        show_tip(dict)
    elif type == "restore":
        start_dirpath = fd.askdirectory()
        dict = restoreAttFile(start_dirpath)
        show_tip(dict)
    elif type == "select_att_dirpath":
        att_dirpath_var.set(fd.askdirectory())
    elif type == "reset":
        att_dirpath_var.set(default_att_dirpath)
    elif type == "quit":
        window.destroy()


if __name__ == '__main__':
    # 创建 Tkinter 窗口
    window = tk.Tk()
    # 设置窗口大小
    window.geometry("600x400")
    # 禁止用户调整窗口大小
    window.resizable(False, False)
    frame = tk.Frame(window)
    frame.pack(expand=True)

    is_clean_all_att_var = tk.BooleanVar(value=False)
    # 创建字符串类型的变量 var1 和关联的输入框 entry1
    att_dirpath_var = tk.StringVar(value=default_att_dirpath)

    entry1_frame = tk.Frame(frame)
    entry1_frame.pack(pady=5)
    att_dirpath_title_label = tk.Label(entry1_frame, text="设置附件目录", font=("Microsoft YaHei", 9))
    att_dirpath_title_label.pack(side=tk.LEFT, padx=10)
    entry_box = tk.Entry(entry1_frame, textvariable=att_dirpath_var, width=30, font=("Microsoft YaHei", 9))
    entry_box.pack(side=tk.LEFT)
    select_att_dirpath_btn = tk.Button(entry1_frame, text="选择", font=("Microsoft YaHei", 9), command=lambda: buttonHandle("select_att_dirpath", att_dirpath_var=att_dirpath_var))
    select_att_dirpath_btn.pack(side=tk.LEFT)
    reset_att_dirpath_btn = tk.Button(entry1_frame, text="重置", font=("Microsoft YaHei", 9), command=lambda: buttonHandle("reset", att_dirpath_var=att_dirpath_var))
    reset_att_dirpath_btn.pack(side=tk.LEFT, padx=5)
    label_tip = f'附件目录说明：\n\n（1）对于绝对路径：可通过“选择”按钮选择附件目录。\n（2）对于相对路径：可设置："./"、"{default_att_dirpath}"、"{default_att_dirpath}/xxx/xxx（如：{default_att_dirpath}/assets）" 等相对路径。（其中“./”表示markdown文件所在目录；“{default_att_dirpath}” 表示markdown文件所在目录下的同名文件夹。）'
    att_dirpath_tip_label = tk.Label(frame, text=label_tip, bg="#ced6e0", justify="left", wraplength=500, foreground="#282c34", font=("Microsoft YaHei", 8, "italic"))
    att_dirpath_tip_label.pack(pady=5)

    switch = tk.Checkbutton(frame, text="清理所有附件（默认只清理图片）", variable=is_clean_all_att_var, width=40, height=5, onvalue=True, offvalue=False, bd=0)
    switch.pack()

    # 创建标签
    clean_or_restore_label = tk.Label(frame, text="请选择清理或还原", fg="#101014", font=("Microsoft YaHei", 12, "bold"))
    # 创建按钮
    clean_btn = tk.Button(frame, text="清理",  width=10,  command=lambda: buttonHandle("clean", is_clean_all_att_var=is_clean_all_att_var, att_dirpath_var=att_dirpath_var))
    restore_btn = tk.Button(frame, text="还原", width=10,  command=lambda: buttonHandle("restore"))
    # quit_button = tk.Button(frame, text="关闭", width=10,  command=lambda: buttonHandle("quit"))
    # 将按钮、标签添加到窗口中
    clean_or_restore_label.pack(pady=10)
    clean_btn.pack(pady=5)
    restore_btn.pack(pady=5)
    # quit_button.pack(pady=5)
    # 获取屏幕的宽度和高度
    frame_width = frame.winfo_reqwidth()
    frame_height = frame.winfo_reqheight()
    # 计算窗口左上角的坐标使其居中
    x = (window.winfo_screenwidth() // 2) - (frame_width // 2)
    y = (window.winfo_screenheight() // 2) - (frame_height // 2)
    # 设置窗口左上角的坐标
    window.geometry("+%d+%d" % (x, y))
    window.mainloop()
