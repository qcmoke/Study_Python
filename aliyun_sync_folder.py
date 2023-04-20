import os
import tkinter
from aligo import Aligo
from tkinter import filedialog

if __name__ == '__main__':
    ali = Aligo()

    tk = tkinter.Tk()
    tk.withdraw()
    directory = filedialog.askdirectory(initialdir='E:/Temp/阿里同步盘')
    if len(directory) == 0:
        exit(1)

    default_folder_path = "/同步盘"
    folder_path = input('请输入云盘文件夹（默认为"' + default_folder_path + '"）：')
    if folder_path == '' or None:
        folder_path = default_folder_path
    folder = ali.get_folder_by_path(folder_path)
    if folder is None:
        create_folder = input('云盘文件夹[%s]不存在，是否创建?(yes)：' % folder_path)
        if create_folder.lower() == 'yes':
            folder = ali.create_folder(folder_path)
            print('云盘文件夹[%s]创建完成' % folder_path)
        else:
            print('云盘文件夹[%s]不存在，同步已取消' % folder_path)
            os.system('pause')
            exit(1)

    print('本地目录：%s' % directory)
    print('远程目录：https://www.aliyundrive.com/drive/folder/%s' % folder.file_id)
    # None：双端同步 True：以本地为主 False：以云端为主
    ali.sync_folder(directory, folder.file_id, True)
    os.system('pause')

    # more：https://github.com/foyoux/aligo
