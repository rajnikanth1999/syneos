from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from datetime import datetime, timedelta

credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(account_url='https://iepdlz01devencur.blob.core.windows.net', credential=credential)

parquet_blobs = []
time_threshold = datetime.utcnow() - timedelta(days=1)

containers = blob_service_client.list_containers()

print("acquiring all the blobs from containers of data lake")

for container in containers:
    container_name = container.name
    print("Looking in -> ", container_name)
    container_client = blob_service_client.find_blobs(container_name, prefix="", name_ends_with=".parquet")

    for blob in container_client.list_blobs():
        blob_path = blob.name
        if blob_path.endswith('.parquet'):
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_path)
            properties = blob_client.get_blob_properties()
            last_modified = properties.last_modified
            print("found ",blob_path, "file in ", container_name, "last modified at", last_modified)
            
