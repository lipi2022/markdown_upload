import logging
import sys


from src import replace_img_src

# logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)

logging.basicConfig(stream=sys.stdout, encoding="utf-8", level=logging.DEBUG)

if __name__ == "__main__":
    # replace_img_src(
    #     "/Users/dialling/Library/Mobile Documents/com~apple~CloudDocs/md",
    #     "/Users/dialling/Library/Mobile Documents/com~apple~CloudDocs/md_upload",
    # )

    replace_img_src("/Users/dialling/dev/cubox", "markdown_online")
    print("Starting")
