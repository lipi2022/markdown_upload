import logging
import os


def replace_img_src(root_dir, dest_dir):

    if not dest_dir:
        logging.info("dest directory is null")
        return

    # 创建根目录，如果存在就不做处理
    os.makedirs(dest_dir, exist_ok=True)
    logging.info("create dest dir:", dest_dir)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # offset = len(dirpath.split(os.sep))
        # print("    " * (offset - 1), dirpath, sep="")
        # print("    " * (offset - 1), dirnames, sep="")

        for a_file in filenames:
            print(dirpath, "/", a_file, sep="")
            pass
        pass
