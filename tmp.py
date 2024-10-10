import tkinter as tk
from tkinter import scrolledtext


def remove_newlines(input_string):
    # \r\n (Windows) と \n (Unix) の両方の改行を取り除く
    return input_string.replace('\r\n', '').replace('\n', '')

def on_ok_clicked():
    # OKボタンが押されたときの処理
    text = text_area.get("1.0", tk.END)  # テキストエリアの内容を取得
    print(eval(remove_newlines(text)))

# メインウィンドウの作成
root = tk.Tk()
root.title("テキストエリアとOKボタンのUI")
root.geometry("400x300")  # ウィンドウサイズを指定

# テキストエリア（スクロール付き）
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# OKボタン
ok_button = tk.Button(root, text="OK", command=on_ok_clicked)
ok_button.pack(pady=10)

# ウィンドウのメインループ開始
root.mainloop()
