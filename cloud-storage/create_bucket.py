# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "google-cloud-storage>=3.17.1",
# ]
# ///
import argparse
from google.cloud import storage

def main():
    parser = argparse.ArgumentParser(description="Create a GCP bucket.")
    parser.add_argument("bucket_name", type=str, help="Name of the bucket to create")
    args = parser.parse_args()

    bucket_name = args.bucket_name
    print(f"Bucket name received: {bucket_name}")
    # Aquí puedes agregar la lógica para crear el bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"
    new_bucket = storage_client.create_bucket(bucket, location="us-central1")
    print(f"Bucket {new_bucket.name} created in {new_bucket.location} with class {new_bucket.storage_class}")


if __name__ == "__main__":
    main()