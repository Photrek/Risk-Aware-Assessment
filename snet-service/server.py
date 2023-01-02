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

# SERVICE_API
class ServiceDefinition(pb2_grpc.ServiceDefinitionServicer):

    def __init__(self):
        self.accuracy = 0.0
        self.decisiveness = 0.0
        self.reobustness = 0.0
        self.s = ''
        self.response = None

    def adr(self, request, context):
        # Parsing input string
        self.s = request.s
        input_array = np.asarray(self.s.split(','), dtype=float)

        # Calculating metrics
        self.accuracy = accuracy(input_array)
        self.decisiveness = decisiveness(input_array)
        self.robustness = robustness(input_array)
        
        # Filling out response values
        self.response = pb2.ADRReturnFloat()
        self.response.a = self.accuracy
        self.response.d = self.decisiveness
        self.response.r = self.robustness

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
