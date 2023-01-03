# tutorial
# 7003

import sys
import grpc

sys.path.append("./service_spec")
import adr_pb2 as pb2
import adr_pb2_grpc as pb2_grpc


# TEST_CODE
def doSomething(channel):

    # Read in input
    r = sys.argv[1]
    p = sys.argv[2]
    k = sys.argv[3]

    # Passing the input to the service
    stub = pb2_grpc.ServiceDefinitionStub(channel)
    response = stub.adr(pb2.InputString(r=r, p=p, k=k))
    print("Accuracy: {:.4f}, Decisiveness: {:.4f}, Robustness: {:.4f}, Generalized Mean: {:.4f}".format(response.a, response.d, response.r, response.g))
    return response


def main():
    # Connect to the server
    with grpc.insecure_channel('localhost:7003') as channel:
        # Call TEST_CODE
        doSomething(channel)


if __name__ == '__main__':
    main()
