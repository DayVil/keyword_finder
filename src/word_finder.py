import fitz
import os


def _write_log(str):
    with open("log.md", "a") as f:
        f.write(str)


def _reset_log():
    with open("log.md", "w") as f:
        f.write("")


def _find_word(path, pdf_name, lk_word):
    lis_page_num = []
    with fitz.open(path + pdf_name) as pages:
        w = False
        for page in pages:
            lis_txt = page.getText().lower().strip().split()

            if lk_word in lis_txt:
                if w is False:
                    s = f"Word found at pdf {pdf_name}"
                    print(s)
                    _write_log("\n" + s + "\n")
                    w = True

                lis_page_num.append(page.number)
                _write_log(f"Word found at page: {page.number}\n")

    return lis_page_num


def finder(path, lk_word):
    _reset_log()
    print("clicked!")

    path += "/"
    lk_word = lk_word.lower()
    lis_dir = os.listdir(path=path)

    ctx = {}
    for file in lis_dir:
        if ".pdf" in file[-4:]:
            pag = _find_word(path, file, lk_word)
            if pag:
                ctx[file] = pag

    return ctx


if __name__ == "__main__":
    PATH = "./res/samples/"
    looked_word = "This"

    finder(PATH, looked_word)
