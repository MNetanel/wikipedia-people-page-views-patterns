from google.cloud import storage
import os
from tqdm import tqdm
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
 
storage_client = storage.Client()
bucket = storage_client.get_bucket(os.getenv('BUCKET'))
blobs = tqdm(bucket.list_blobs())  # Get list of files
for blob in blobs:
    filename = blob.name
    blobs.set_postfix_str(filename)
    blob.download_to_filename(f'{os.getenv('RAW_DATA_DIR')}/{filename}')  # Download
