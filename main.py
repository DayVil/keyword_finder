import fitz


PATH = "./samples/"
looked_word = "This"

def main():
    pdf_name = "Recipes.pdf"
    lk_word = looked_word.lower()

    with fitz.open(PATH+pdf_name) as pages:
        with open("log.md", "a") as f:
                    f.write(f"Word found at pdf {pdf_name}\n\n")

        for page in pages:
            lis_txt = page.getText().lower().split(" ")
            if lk_word in lis_txt:
                with open("log.md", "a") as f:
                    f.write(f"Word found at page: {page.number}\n")
        
        
if __name__ == '__main__':
    with open("log.md", "w") as f:
        f.write("")
    main()