# 7003

import base64
from concurrent import futures
import datetime
import grpc
import io
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
from pdb import set_trace
import sys
import time



#sys.path.append("./service_spec")
sys.path.append(".")
#import tutorial_pb2 as pb2
import adr_pb2 as pb2
#import tutorial_pb2_grpc as pb2_grpc
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

def get_source_probs(data):
    """"""
    if 0:
        print("doing: np conv",flush=True)
        data_np=data.to_numpy()
        set_trace()

    # Class index (last column)
    # Subtract 1 to convert to zero index
    #print("doing: subtract 1",flush=True)
    true_event_index = data.iloc[:,-1].values - 1

    # Take everything except last column
    #print("doing: all but last column",flush=True)
    probs_array_ = data.iloc[:, :-1].values

    # Normalize so it sums to 1
    #print("doing: norm sum to 1",flush=True)
    probs_array = probs_array_/np.expand_dims(np.sum(probs_array_,1),1)

    # Applying mask to get probability of event that actually happened
    #print("doing: take_along_axis",flush=True)
    source_probs = np.take_along_axis(probs_array, np.expand_dims(true_event_index.astype(int),1), 1)

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
    mpl.rcParams['font.family'] = ['serif']
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Plot in logscale, so convert the metric as logs as well
    log_dec = np.log(decisiveness_res)
    log_acc = np.log(accuracy_res)
    log_rob = np.log(robustness_res)
    
    dec_txt = f'{decisiveness_res:0.2e}'
    acc_txt = f'{accuracy_res:0.2e}'
    rob_txt = f'{robustness_res:0.2e}'
    
    # Adding the generalised mean values to the plot
    plt.axvline(log_dec, color='g', linestyle='dashed', linewidth=2, label=f'Decisiveness {dec_txt}')
    #plt.text(log_dec, 10*12, dec_txt, color='g', size='large', weight='bold')
    plt.axvline(log_acc, color='b', linestyle='dashed', linewidth=2, label=f'Accuracy {acc_txt}')
    #plt.text(log_acc, 10*12, acc_txt, color='b', size='large', weight='bold')
    plt.axvline(log_rob, color='r', linestyle='dashed', linewidth=2, label=f'Robustness {rob_txt}')
    #plt.text(log_rob, 10*12, rob_txt, color='r', size='large', weight='bold')
    
    # Plotting the histogram, inputs are log probabilities, frequencies are calculated on the log scale
    if 0:
        plt.hist(
                    x_log_prob,
                    log=True, 
                    bins=100, 
                    facecolor='white', 
                    edgecolor='black'
                    )
    elif 1:
        plt.hist(x_log_prob, log=True, bins=100, facecolor='#d5ecf5')
    
    # Adding labels
    plt.xlabel('Prediction Probabilities', fontdict = {'fontsize' : 35, 'weight': 'normal'})
    
    plt.ylabel(
        "Frequency of Observed Outcomes", 
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

    # Adding logo
    im = plt.imread('photrek_logo.png')
    newax = fig.add_axes([0.45, 0.75, 0.1, 0.1], anchor='NE', zorder=0)
    #newax.imshow(im)
    newax.imshow(im,alpha=0.4)
    newax.axis('off')
    plt.show()
    #fig.savefig('plot.png', bbox_inches='tight')
    my_stringIObytes = io.BytesIO()
    fig.savefig(my_stringIObytes, bbox_inches='tight',format="png")
    my_stringIObytes.seek(0)
    my_base64pngData = base64.b64encode(my_stringIObytes.read())

    return my_base64pngData

# SERVICE_API
class ServiceDefinition(pb2_grpc.ServiceDefinitionServicer):

    def __init__(self):
        self.accuracy = 0.0
        self.decisiveness = 0.0
        self.reobustness = 0.0
        self.s = ''
        self.response = None

    def adr(self, request, context):
        
        #print(str(datetime.datetime.now()).split(".")[0] + "  Executing adr: s="+request.s)
        print(str(datetime.datetime.now()).split(".")[0] + "  Executing adr")
        #print("               decoded: "+base64.b64decode(request.s).decode('utf-8'))

        # Parsing input string
        #self.s = request.s
        #self.s = base64.b64decode(request.s).decode('utf-8')
        numRows = int(request.s.split(",")[0])
        numCols = int(request.s.split(",")[1])
        fileText = base64.b64decode(request.s.split(",")[2]).decode('utf-8')
        print(f"  {numRows} x {numCols}")
        data = pd.read_csv(io.StringIO(fileText),header=None,dtype=np.float64)
        #print(f"doing: get_source_probs",flush=True)
        source_probs = get_source_probs(data)
        #print(f"doing: plot",flush=True)
        #plot(source_probs)
        plot_b64 = plot(source_probs)
        #print(f"done")


        #input_array = np.asarray(self.s.split(','), dtype=float)

        # Calculating metrics
        if 1:
            if 0 in data:
                second_smallest = np.unique(data)
                floor_value = second_smallest[1] ** 2
                data = np.where(data == 0, floor_value, data)
            self.response = pb2.ADRReturnFloat()
            self.response.a = accuracy(source_probs)
            self.response.d = decisiveness(source_probs)
            self.response.r = robustness(source_probs)
            self.response.numr = numRows
            self.response.numc = numCols
            self.response.img = plot_b64
            #self.response.filename
            #self.response.filesize
            #self.response.processDuration
            return self.response
        
        # Filling out response values
        self.response = pb2.ADRReturnFloat()
        self.response.a = self.accuracy
        self.response.d = self.decisiveness
        self.response.r = self.robustness

        return self.response


def main():
    port_number = 7003
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ServiceDefinitionServicer_to_server(ServiceDefinition(), server)
    if 1: # unsecured comm (HTTP, no TLS/SSL)
        server.add_insecure_port(f'[::]:{port_number}')
        server.start()
        print("Server listening on 0.0.0.0:{} (w/o SSL-secured comm)".format(port_number))
    elif 0:  # TLS/SSL-secured comm (HTTPS)
        keyfile = '/home/blake_anderton/raa/cfssl/adr-service-server-key.pem'
        certfile = '/home/blake_anderton/raa/cfssl/adr-service-server.pem'
        credentials = grpc.ssl_server_credentials([(open(keyfile,'rb').read(), open(certfile,'rb').read())])
        server.add_secure_port(f"[::]:{port_number}", credentials)
        server.start()
        print("Server listening on 0.0.0.0:{} (w/ SSL-secured comm)".format(port_number))
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()