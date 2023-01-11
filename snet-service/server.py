# tutorial
# 7003

import sys
import os
from concurrent import futures
import time

import grpc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append("./service_spec")
import adr_pb2 as pb2
import adr_pb2_grpc as pb2_grpc

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

def generalized_mean(x, r):
    n = len(x)
    result = np.sum((x**(r))/n) ** (1/r)
    return result

def generalized_mean(x, r):
    n = len(x)
    result = np.sum((x**(r))/n) ** (1/r)
    return 

def get_filepath(filename, extension):
    return f'{filename}{extension}'

def get_source_probs(data):
    """"""
    # Class index (last column)
    # Subtract 1 to convert to zero index
    true_event_index = data.iloc[:,-1].values - 1

    # Take everything except last column
    probs_array_ = data.iloc[:, :-1].values

    # Normalize so it sums to 1
    probs_array = probs_array_/np.expand_dims(np.sum(probs_array_,1),1)

    # Applying mask to get probability of event that actually happened
    source_probs = np.take_along_axis(probs_array, np.expand_dims(true_event_index,1), 1)

    return source_probs

def plot(data):
    """Calculates metrics and saves plot locally"""

    # Need to handle 0s
    if 0 in data:
        second_smallest = np.unique(data)
        floor_value = second_smallest[1] ** 2
        data = np.where(data == 0, floor_value, data)


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
    plt.axvline(log_dec, color='r', linestyle='dashed', linewidth=2, label='Decisiveness')
    plt.text(log_dec, 10*12, dec_txt, color='r', size='large', weight='bold')
    plt.axvline(log_acc, color='b', linestyle='dashed', linewidth=2, label='Accuracy')
    plt.text(log_acc, 10*12, acc_txt, color='b', size='large', weight='bold')
    plt.axvline(log_rob, color='g', linestyle='dashed', linewidth=2, label='Robustness')
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
    plt.legend(fontsize=20)
    
    # Save file locally
    plt.savefig('hist.png')

class ServiceDefinition(pb2_grpc.ServiceDefinitionServicer):
    
    def UploadFile(self, request_iterator, context):
        data = bytearray()
        filepath = 'dummy'

        for request in request_iterator:
            if request.metadata.filename and request.metadata.extension:
                filepath = get_filepath(request.metadata.filename, request.metadata.extension)
                continue
            data.extend(request.chunk_data)
        
        print(data)
        with open(filepath, 'wb') as f:
            f.write(data)
        return pb2.StringResponse(message='Success!')
    
    def ADR(self, request_iterator, context):

        # Receive data from client
        data = bytearray()
        filepath = 'dummy'

        for request in request_iterator:
            if request.metadata.filename and request.metadata.extension:
                filepath = get_filepath(request.metadata.filename, request.metadata.extension)
                continue
            data.extend(request.chunk_data)
        
        # Write data to csv file locally
        with open('data.csv', 'wb') as f:
            f.write(data)
        
        # Read in local csv file and transform
        data = pd.read_csv('data.csv')
        source_probs = get_source_probs(data)

        # Generate plot locally
        plot(source_probs)

        message = f'Accuracy: {accuracy(source_probs):.4f}, Decisiveness: {decisiveness(source_probs):.4f}, Robustness: {robustness(source_probs):.4f}'
        return pb2.StringResponse(message=message)
        
    def DownloadFile(self, request, context):
        chunk_size=1024

        filepath = f'{request.filename}{request.extension}'
        if os.path.exists(filepath):
            with open(filepath, mode='rb') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if chunk:
                        entry_response = pb2.FileResponse(chunk_data=chunk)
                        yield entry_response
                    else:
                        return


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ServiceDefinitionServicer_to_server(ServiceDefinition(), server)
    server.add_insecure_port('[::]:7003')
    server.start()
    print("Server listening on 0.0.0.0:{}".format(7003))
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()
