import logging
import os
import re


def replace_img_src(root_dir, dest_dir, storage):

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
                # print(dir_path, "/", file, sep="")
                # print(dest_dir_new, "/", file, sep="")
                if filename == "DatabrickFinance":  # just debug
                    print("filename:", filename)
                    md_file = dir_path + "/" + file
                    dest_file = dest_dir_new + "/" + file

                    # check dest_dir exist
                    if not os.path.exists(dest_dir_new):
                        os.makedirs(dest_dir_new)

                    img_src_change(md_file, dest_file, storage)


# md_file,dest_file : file with path
def img_src_change(md_file, dest_file, storage):
    print("md file, dest file", md_file, dest_file)

    with open(md_file, "r") as file:
        data = file.read()

        # search and replace img src
        new_data = regex_images(data, storage)

        # write new data to new file
        f = open(dest_file, "w")
        f.write(new_data)  # overwrite existing file 
        f.close()

        # close read file
        file.close()


# search img src ,upload to cloud storage ,return new data
def regex_images(data, storage):
    img_srcs = re.findall(r"!\[(.*)\]\((.+)\)", data)

    # get img src
    for img_tuple in img_srcs:
        if img_tuple[1]:  # tuple's second item is src,first is description
            new_img_src = storage.upload_img(img_tuple[1])

            # replace data img src with new_img_src
            data.replace(img_tuple[1], new_img_src)

    return data  # new data
