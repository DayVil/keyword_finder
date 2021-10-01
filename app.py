import tkinter as tk
from tkinter import filedialog
from tkinter.constants import S
from PIL import Image, ImageTk
import math

from src.word_finder import finder



class App(tk.Tk):

    def __init__(self):
        _scaler = 6
        _ico_path = "./res/icons/tmp/pdf_key.ico"

        super().__init__()
        self._ctx = None
        self._font = "Arial"
        self._font_size = 11
        self._font_def = (self._font, self._font_size)
        self._path = None

        # canvas = tk.Canvas(self, width=750, height=300)
        # canvas.grid(columnspan=3, rowspan=5)
        self.geometry("730x550")

        #loading image
        image = Image.open('./res/icons/pdf_key.jpg')
        scaling = image.size
        print(scaling)
        new_scaling = tuple(math.floor(s/_scaler) for s in scaling)
        print(new_scaling)
        new_image = image.resize(new_scaling)

        #icon
        new_image.save(_ico_path)
        self.iconbitmap(_ico_path)

        #logo
        # logo = ImageTk.PhotoImage(new_image)
        # logo_label = tk.Label(self, image=logo)
        # logo_label.image = logo
        # logo_label.grid(column=1, row=0)

        #Create Widgets
        self.widget_create_dir()

        # canvas = tk.Canvas(self, width=600, height=50)
        # canvas.grid(columnspan=3)


    def widget_create_dir(self):
        beg = [30,20]

        #Label
        instruct = tk.Label(self, text="Select a directory:", font=self._font_def)
        instruct.place(x=beg[0], y=beg[1])

        instruct1 = tk.Label(self, text="Looking for:", font=self._font_def)
        instruct1.place(x=beg[0], y=beg[1]*7)

        #text panel
        text_box = tk.Text(self, height=30, width=50)
        text_box.insert(1.0, "")
        text_box.place(x=beg[0]+260, y=beg[1]+8)

        #browse button
        browse_text = tk.StringVar()
        browse_btn = tk.Button(self, textvariable=browse_text, command=lambda:self.browse_button(browse_text), font=self._font_def, bg="gray", fg="white", height=1, width=26)
        browse_text.set("Browse")
        browse_btn.place(x=beg[0], y=beg[1]+25)

        #Entry field
        ent_field = tk.Entry(self, text="Insert keyword", font=self._font_def, width=30)
        ent_field.place(x=beg[0], y=beg[1]*7+25)

        #run button
        run_button = tk.Button(self, text= "Start search", command=lambda: self.start_search(ent_field.get(), text_box), font=self._font_def, bg="gray", fg="white")
        run_button.place(x=beg[0],y=beg[1]*7+50)

    def start_search(self, key, txt):
        self._ctx = finder(self._path, key)

        s = ""
        for ele in self._ctx:
            s += f"Found '{key}' in {ele}\n"

        txt.delete("1.0","end")
        self._ctx = S
        txt.insert(1.0, s)

    def browse_button(self, browse_txt):
        browse_txt.set("loading...")
        self._path = filedialog.askdirectory(parent=self, title="Directory with pdfs.")
        browse_txt.set(self._path)


def main():
    app = App()
    app.mainloop()

if __name__=='__main__':
    main()


#TODO
#page num

#TODO
#Auto new line