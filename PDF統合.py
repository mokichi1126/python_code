import PyPDF2
import os
import tkinter as tk
from tkinter import ttk

def on_enter_pressed(event=None):
# 結合するPDFファイルのリストを作成
    filename=textbox.get()
    pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

    # PDFファイルを統合するためのPdfMergerオブジェクトを作成
    pdf_merger = PyPDF2.PdfMerger()

    # 各PDFファイルを統合
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)

    # 結合したPDFを保存
    with open(f"{filename}.pdf", "wb") as output_pdf:
        pdf_merger.write(output_pdf)

    print("PDFファイルを統合しました。")


root= tk.Tk()
root.geometry("200x80")
label = tk.Label(root)
label.pack()
textbox= ttk.Entry(root)
textbox.pack()
textbox.bind("<Return>", on_enter_pressed)
button=ttk.Button(root, text= "PDF出力",command = on_enter_pressed)
button.pack()
textbox.focus_set()
root.mainloop()