from email.mime import base
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

    # upload to google storage, return new http_src.
    # kind : image or markdown
    def upload_object(self, file_with_path, kind):
        # only filename as destination file name
        basename = os.path.basename(file_with_path)

        if kind == "image":
            blob = self.image_bucket.blob(basename)
        elif kind == "markdown":
            blob = self.markdown_bucket.blob(basename)
        else:
            logging.error("Unknown kind")

        try:
            blob.upload_from_filename(file_with_path)  # will overwrite existing
            blob.make_public()  # public to share
        except Exception as e:
            logging.error(e)

        logging.info("upload: %s, url:%s", basename, blob.public_url)

        return blob.public_url
