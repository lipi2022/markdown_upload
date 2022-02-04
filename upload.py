import logging
import sys


from src import replace_img_src

logging.basicConfig(filename="markdown.log", encoding="utf-8", level=logging.DEBUG)


if __name__ == "__main__":
    print("Starting")
    # replace_img_src(
    #     "/Users/dialling/Library/Mobile Documents/com~apple~CloudDocs/md",
    #     "/Users/dialling/Library/Mobile Documents/com~apple~CloudDocs/md_upload",
    # )

    replace_img_src("/home/me/Downloads/Archive/md", "markdown_online")
