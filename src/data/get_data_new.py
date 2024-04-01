from google.cloud import storage
import os
from tqdm import tqdm
from pathlib import Path
# os.environ["GCLOUD_PROJECT"] = "rising-theater-416315"
# bucket_name = 'wikipedia_project_bucket'
# dl_dir = r'D:\Big Data Course Project\raw_data'

# storage_client = storage.Client()
# bucket = storage_client.get_bucket(bucket_name)
# blobs = tqdm(bucket.list_blobs())  # Get list of files
# for blob in blobs:
#     filename = blob.name
#     blobs.set_postfix_str(filename)
#     blob.download_to_filename(dl_dir + filename)  # Download

# for file in Path(r'D:\Big Data Course Project\raw_data').glob('*'):
#     print(f'{file} -> {file.parent / file.name.replace('raw_data', '')}')
#     os.rename(str(file), str(file.parent / file.name.replace('raw_data', '')))
