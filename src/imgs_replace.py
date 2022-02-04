import logging
import os


def replace_img_src(root_dir, dest_dir):

    if not dest_dir:
        logging.info("dest directory is null")
        return

    # create root directory,if exist do nothing
    os.makedirs(dest_dir, exist_ok=True)
    logging.info("create dest dir:%s", dest_dir)

    for dir_path, _dir_names, filenames in os.walk(root_dir):

        for file in filenames:
            # create directory in dest dir
            dest_dir_new = dir_path.replace(root_dir, dest_dir)

            filename, file_extension = os.path.splitext(file)
            if file_extension == ".md":
                print(dir_path, "/", file, sep="")
                print(dest_dir_new, "/", file, sep="")
                md_file = dir_path + "/" + file
                dest_file = dest_dir_new + "/" + file
                img_src_change(md_file, dest_file)


# md_file,dest_file : file with path
def img_src_change(md_file, dest_file):
    print("md file, dest file", md_file, dest_file)
    pass
