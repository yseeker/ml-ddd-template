from google.cloud import storage
import os

class GCSStorage:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(bucket_name)

    def upload_file(self, file_path: str, destination_blob_name: str):
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(file_path)
        print(f"File {file_path} uploaded to {destination_blob_name}.")

    def download_file(self, source_blob_name: str, destination_file_path: str):
        blob = self.bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_path)
        print(f"File {source_blob_name} downloaded to {destination_file_path}.")

    def list_files(self, prefix: str = None):
        files = self.bucket.list_blobs(prefix=prefix)
        return [file.name for file in files]

    def delete_file(self, blob_name: str):
        blob = self.bucket.blob(blob_name)
        blob.delete()
        print(f"File {blob_name} deleted.")