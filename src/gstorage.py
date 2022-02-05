import logging
import os

from google.cloud import storage
from google.cloud.exceptions import Conflict


class GoogleStorage:
    """google storage class"""

    def __init__(
        self, project, image_bucket, markdown_bucket, service_account, credential
    ):
        self.project = project
        self.image_bucket_name = image_bucket
        self.markdown_bucket_name = markdown_bucket
        self.service_account = service_account
        self.credential = credential
        self.storage_client = storage.Client()

        try:
            self.image_bucket = self.storage_client.create_bucket(
                self.image_bucket_name
            )
        except Conflict:
            logging.debug("create image bucket failed, image bucket alread exist")
            self.image_bucket = self.storage_client.bucket(self.image_bucket_name)

        try:
            self.markdown_bucket = self.storage_client.create_bucket(
                self.markdown_bucket_name
            )
        except Conflict:
            logging.debug("create markdown bucket failed, markdown bucket alread exist")
            self.markdown_bucket = self.storage_client.bucket(self.markdown_bucket_name)

    # upload mk from data string
    def upload_md_from_string(self, data_string, filename):
        try:
            blob = self.markdown_bucket.blob(filename)
            blob.upload_from_string(data_string)
            blob.make_public()  # public to share
        except Exception as e:
            logging.error(e)

        return blob.public_url

    # upload image from file
    # filepath: file with path
    # filename: pure filename , with prefix as directory.like /markdownimage/dog.png
    def upload_image_from_file(self, filepath):
        basename = os.path.basename(filepath)

        try:
            blob = self.image_bucket.blob(basename)
            blob.make_public()
            blob.upload_from_filename(filepath)  # will overwrite existing
            blob.make_public()  # public to share
        except Exception as e:
            logging.error(e)
            return ""  # upload failed ,return ""

        return blob.public_url
