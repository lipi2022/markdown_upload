import logging
import configparser


from src import replace_img_src


# return
def read_config():
    config = configparser.ConfigParser()
    config.read("config.ini")  # must two line
    return config


def init_log():
    logging.basicConfig(filename="markdown.log", encoding="utf-8", level=logging.DEBUG)


if __name__ == "__main__":
    config = read_config()
    if config["LOG"]["Filename"]:
        logging.info("create log success:%s", config["LOG"]["Filename"])
        init_log()
    print("Starting")

    if config["DIR"]["Root"] and config["DIR"]["Dest"]:
        replace_img_src(config["DIR"]["Root"], config["DIR"]["Dest"])
