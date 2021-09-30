import fitz
import os

PATH = "./res/samples/"
looked_word = "This"


def write_log(str):
    with open("log.md", "a") as f:
        f.write(str)


def reset_log():
    with open("log.md", "w") as f:
        f.write("")


def find_word(path, pdf_name, lk_word):
    with fitz.open(path+pdf_name) as pages:
        w = False
        for page in pages:
            lis_txt = page.getText().lower().strip().split()
            if lk_word in lis_txt:
                if w is False:
                    write_log(f"\nWord found at pdf {pdf_name}\n")
                    w = True
                write_log(f"Word found at page: {page.number}\n")


def main(path, lk_word):
    lk_word = lk_word.lower()
    lis_dir = os.listdir(path=path)

    for file in lis_dir:
        if ".pdf" in file[-4:]:
            find_word(path, file, lk_word)
        
        
if __name__ == '__main__':
    reset_log()
    main(PATH, looked_word)