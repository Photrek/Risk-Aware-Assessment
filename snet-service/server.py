# tutorial
# 7003

import sys
from concurrent import futures
import time

import grpc
import numpy as np

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

def parse_probabilities(p):
    """Converts string into array of probabilities."""
    # Split class probabilities by ;
    class_probs = p.split(';')

    # Split observation probabilities by ,. Result is a list of lists.
    ll_probs = [probs.split(',') for probs in class_probs]
    
    # All sub lists should be the same length
    assert all(len(probs) == len(ll_probs[0]) for probs in ll_probs)

    probs_array = np.asarray(ll_probs, dtype=float)

    # Transposing from k x n to n x k
    probs_array = np.transpose(probs_array)

    # Normalizing so forecast probabilities for an observation sum to 1
    probs_array = probs_array/np.expand_dims(np.sum(probs_array,1),1)

    return probs_array

# SERVICE_API
class ServiceDefinition(pb2_grpc.ServiceDefinitionServicer):

    def __init__(self):
        self.accuracy = 0.0
        self.decisiveness = 0.0
        self.reobustness = 0.0
        self.r = ''
        self.p = ''
        self.k = ''
        self.response = None

    def adr(self, request, context):
        # Parsing input string
        self.r = request.r
        self.p = request.p
        self.k = request.k
        

        probs_array = parse_probabilities(self.p)
        self.k = np.asarray(self.k.split(','), dtype=int)

        assert len(probs_array) == len(self.k)

        # Applying mask to get probability of event that actually happened
        source_probs = np.take_along_axis(probs_array, np.expand_dims(self.k,1), 1)


        # Calculating metrics
        self.accuracy = accuracy(source_probs)
        self.decisiveness = decisiveness(source_probs)
        self.robustness = robustness(source_probs)
        self.generalized_mean = generalized_mean(source_probs, float(self.r))
        
        # Filling out response values
        self.response = pb2.ADRReturnFloat()
        self.response.a = self.accuracy
        self.response.d = self.decisiveness
        self.response.r = self.robustness
        self.response.g = self.generalized_mean

        return self.response


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
