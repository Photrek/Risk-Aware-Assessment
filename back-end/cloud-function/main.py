import functions_framework
import numpy as np
from google.cloud import storage
import matplotlib.pyplot as plt

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")

    # Only run if file uploaded is csv
    if '.csv' in name:
        # Downloading data
        download_blob(bucket, name, 'data_temp.csv')
        
        # Reading in data
        data = np.genfromtxt('data_temp.csv', delimiter=',')
        print(f"Mean of data: {np.mean(data)}")

        # Generating plot and saving locally
        plot(data)

        # Upload image to bucket
        upload_blob(bucket, 'hist.png', 'hist.png')

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

# Defining generalised mean functions
def decisiveness(x):
    # Decisiveness = Arithmetic mean
    result = np.mean(x) 
    return result
    
def accuracy(x):
    # Accuracy = Geometric mean
    n = len(x)
    result = np.exp(np.sum(np.log(x)/n))
    return result

def robustness(x):
    # Robustness = -2/3 Mean
    n = len(x)
    result = np.sum((x ** (-2/3))/n) ** (-3/2)
    return result

def plot(data):
    """Calculates metrics and saves plot locally"""

    # Calculating metrics
    decisiveness_res = decisiveness(data)
    accuracy_res = accuracy(data)
    robustness_res = robustness(data)

    print(f"Decisiveness of data: {decisiveness_res}")
    print(f"Accuracy of data: {accuracy_res}")
    print(f"Robustness of data: {robustness_res}")

    # Creating plot
    x_log_prob = np.log(data)

    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Plot in logscale, so convert the metric as logs as well
    log_dec = np.log(decisiveness_res)
    log_acc = np.log(accuracy_res)
    log_rob = np.log(robustness_res)
    
    dec_txt = f'{decisiveness_res:0.2e}'
    acc_txt = f'{accuracy_res:0.2e}'
    rob_txt = f'{robustness_res:0.2e}'
    
    # Adding the generalised mean values to the plot
    plt.axvline(log_dec, color='r', linestyle='dashed', linewidth=2)
    plt.text(log_dec, 10*12, dec_txt, color='r', size='large', weight='bold')
    plt.axvline(log_acc, color='b', linestyle='dashed', linewidth=2)
    plt.text(log_acc, 10*12, acc_txt, color='b', size='large', weight='bold')
    plt.axvline(log_rob, color='g', linestyle='dashed', linewidth=2)
    plt.text(log_rob, 10*12, rob_txt, color='g', size='large', weight='bold')
    
    # Plotting the histogram, inputs are log probabilities, frequencies are calculated on the log scale
    plt.hist(
                x_log_prob,
                log=True, 
                bins=100, 
                facecolor='white', 
                edgecolor='black'
                )
    
    # Adding labels
    plt.xlabel('Probabilities', fontdict = {'fontsize' : 35, 'weight': 'normal'})
    
    plt.ylabel(
        "Frequency", 
        fontdict = {'fontsize' : 35, 'weight': 'normal'}
        )
    
    # Converting ticks to probability scale post-hoc
    locs, labels = plt.xticks(fontsize=20)
    locs = locs[:-1] # Don't need last tick mark
    prob_x_ticks = [np.exp(loc) for loc in locs]
    plt.xticks(locs, [f'{prob:0.0e}' for prob in prob_x_ticks])

    # setting yticks
    plt.yticks(fontsize=20)
    
    # Save file locally
    plt.savefig('hist.png')