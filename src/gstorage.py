from email.mime import base
import logging
import os

from google.cloud import storage
from google.cloud.exceptions import Conflict


class GoogleStorage:
    """google storage class"""

    def __init__(self, project, bucket, service_account, credential):
        self.project = project
        self.bucket_name = bucket
        self.service_account = service_account
        self.credential = credential
        self.storage_client = storage.Client()

        try:
            self.bucket = self.storage_client.create_bucket(self.bucket_name)
        except Conflict:
            logging.debug("create bucket failed, bucket alread exist")
            self.bucket = self.storage_client.bucket(self.bucket_name)

    # upload to google storage, return new http_src
    def upload_img(self, image_path_name):
        print("upload image", image_path_name)

        # only filename as destination file name
        basename = os.path.basename(image_path_name)

        blob = self.bucket.blob(basename)

        blob.upload_from_filename(image_path_name)  # will overwrite existing
        blob.make_public()  # public to share

        print(f"image name:{basename}, public url:{blob.public_url}")

        return blob.public_url
