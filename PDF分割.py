from PyPDF2 import PdfReader, PdfWriter
import os
import tkinter as tk
from tkinter import ttk

def on_enter_pressed(event=None):
    global entered_text  # グローバル変数を使用
    # Entryウィジェットから入力値を取得し、変数に格納
    entered_text = textbox.get()
    # 現在のディレクトリを取得
    current_directory = os.getcwd()

    # 現在のディレクトリ内のファイル名を取得
    file_names = os.listdir(current_directory)

    # ファイル名を表示
    for file_name in file_names:
        if "pdf" in file_name:
            input_pdf_file = file_name

    # PDFファイルを読み込む
    pdf = PdfReader(input_pdf_file)

    # 各ページを1枚ずつに分割
    for page_num, page in enumerate(pdf.pages, start=1):
        # 新しいPDFファイルを作成
        output_pdf = PdfWriter()
        output_pdf.add_page(page)

        # 出力PDFファイル名を指定
        output_pdf_file = f"{entered_text}-{page_num}.pdf"

        # 出力PDFファイルを保存
        with open(output_pdf_file, 'wb') as output_file:
            output_pdf.write(output_file)

        print(f'Page {page_num} saved as {output_pdf_file}')

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


