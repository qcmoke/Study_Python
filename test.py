import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# 创建 Frame 组件作为卡片容器
card_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
card_frame.pack(side="top", fill="both", padx=10, pady=10)

# 创建文本组件，并放置在卡片容器中
text = "This is some text content that will be displayed in the card."
text_label = tk.Label(card_frame, text=text, font=("Calibri", 14), bg="white", justify="left")
text_label.pack(padx=10, pady=5)

# 运行主循环
root.mainloop()
