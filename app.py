import tkinter as tk
from tkinter import filedialog
from tkinter.constants import WORD
import tkinter.scrolledtext as st
from PIL import Image
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
        self._scroll_text = None

        self.title("Pdf Word Finder")
        self.geometry("800x550")

        # loading image
        image = Image.open("./res/icons/pdf_key.jpg")
        scaling = image.size
        print(scaling)
        new_scaling = tuple(math.floor(s / _scaler) for s in scaling)
        print(new_scaling)
        new_image = image.resize(new_scaling)

        # icon
        new_image.save(_ico_path)
        self.iconbitmap(_ico_path)

        # Create Widgets
        self.widget_create_dir()

    def widget_create_dir(self):
        beg = [30, 20]

        # Label
        instruct = tk.Label(self, text="Select a directory:", font=self._font_def)
        instruct.place(x=beg[0], y=beg[1])

        instruct1 = tk.Label(self, text="Looking for:", font=self._font_def)
        instruct1.place(x=beg[0], y=beg[1] * 7)

        # text panel
        self._scroll_text = st.ScrolledText(
            self, width=59, height=29, font=self._font_def, wrap=WORD
        )
        self._scroll_text.place(x=beg[0] + 260, y=beg[1] + 8)
        self.s_write("First pick your directory then insert a search key.")

        # browse button
        browse_text = tk.StringVar()
        browse_btn = tk.Button(
            self,
            textvariable=browse_text,
            command=lambda: self.browse_button(browse_text),
            font=self._font_def,
            bg="gray",
            fg="white",
            height=1,
            width=26,
        )
        browse_text.set("Browse")
        browse_btn.place(x=beg[0], y=beg[1] + 25)

        # Entry field
        ent_field = tk.Entry(self, text="Insert keyword", font=self._font_def, width=30)
        ent_field.place(x=beg[0], y=beg[1] * 7 + 25)

        # run button
        run_button = tk.Button(
            self,
            text="Start search",
            command=lambda: self.start_search(ent_field.get(), self._scroll_text),
            font=self._font_def,
            bg="gray",
            fg="white",
        )
        run_button.place(x=beg[0], y=beg[1] * 7 + 50)

    def start_search(self, key, txt):
        if self.checker(key):
            return

        self._ctx = finder(self._path, key)
        print("Building dict: ", self._ctx)

        s = ""
        for ele in self._ctx:
            s += f"Found '{key}' in {ele}\n\n"

        s += "--------------------------------------------------------------------------------\n\n"

        for a, b in self._ctx.items():
            s += f"In '{a}' you can find '{key}' on the following pages:\n"

            for i in b:
                s += f"\tPage: {i + 1}\n"
            s += "\n"

        self.s_write(s)

    def browse_button(self, browse_txt):
        browse_txt.set("loading...")
        self._path = filedialog.askdirectory(parent=self, title="Directory with pdfs.")
        browse_txt.set(self._path)

    def s_write(self, s):
        self._scroll_text.delete("1.0", "end")
        self._scroll_text.insert(tk.INSERT, s)

    def checker(self, key):
        if not self._path:
            self.s_write("No path is selected!")
            return True

        if not key:
            self.s_write("Your search key is empty!")
            return True


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
