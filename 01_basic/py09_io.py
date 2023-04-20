# -*- coding: UTF-8 -*- 


def writeFile(filepath):
    file = open(filepath, 'w')
    file.write('Hello, world!\n')
    file.close()


def writeFileByWith(filepath):
    # 使用with语句自动关闭文件
    with open(filepath, 'w') as file:
        file.write('Hello, world!\n')


def readFile(filepath):
    file = open(filepath, 'r')
    data = file.read()
    # file.close()
    print(data)
    input("Press Enter to exit...")


def readFileByWith(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
    print(data)


# writeFile("filename.txt")
readFile("E:/Code/Windows批处理/实用批处理脚本工具/test1/demo1.txt")
