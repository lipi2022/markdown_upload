import logging
import os
import re


def replace_img_src(root_dir, storage):

    for dir_path, _dir_names, filenames in os.walk(root_dir):

        for file in filenames:

            # # just debug
            # if file != "DatabrickFinance.md":
            #     continue

            filename, file_extension = os.path.splitext(file)
            if file_extension == ".md":
                md_file = dir_path + "/" + file

                # dest_file_path - root_dir = prefix
                filename = md_file.removeprefix(root_dir + "/")
                public_url = file_upload(md_file, storage, filename)
                logger = logging.getLogger()
                logger.setLevel(logging.INFO)
                logger.info("upload %s success!", filename)


# upload file,filename: /finance/DatabrickFinance.md
def file_upload(md_file, storage, filename):
    # search and replace img src
    new_data = regex_images(md_file, storage)

    # upload markdown data to cloud storage
    if new_data != "":
        storage.upload_md_from_string(new_data, filename)


# search img src ,upload to cloud storage ,return new data
def regex_images(md_file, storage):
    with open(md_file, "r") as file:
        data = file.read()

        img_srcs = re.findall(r"!\[(.*)\]\((.+)\)", data)

        new_data = data
        # get img src
        for img_tuple in img_srcs:
            if img_tuple[1]:  # tuple's second item is src,first is description
                # no prefix
                new_img_src = storage.upload_image_from_file(img_tuple[1])

                # replace data img src with new_img_src
                if new_img_src != "":
                    new_data = new_data.replace(img_tuple[1], new_img_src)  # recurse
        file.close()

    return new_data  # new data
