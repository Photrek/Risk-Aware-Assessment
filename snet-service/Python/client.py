#!/usr/bin/python3

import sys
import grpc

sys.path.append(".")
import adr_pb2 as pb2
import adr_pb2_grpc as pb2_grpc


# TEST_CODE
def doSomething(channel):

    # Read in input
    s = sys.argv[1]

    # Passing the input to the service
    stub = pb2_grpc.ServiceDefinitionStub(channel)
    response = stub.adr(pb2.InputString(s=s))
    print("Accuracy: {:.4f}, Decisiveness: {:.4f}, Robustness: {:.4f}".format(response.a, response.d, response.r))
    return response


def main():
    server_port = 7003 
    #server_port = 8088
    #server_host = 'localhost' 
    server_host = '127.0.0.1' 
    ca_cert = '/home/blake_anderton/raa/cfssl/ca.pem' # a.k.a. "root certificate"
    # credentials = grpc.ssl_channel_credentials(open(ca_cert,'rb').read())

    # Connect to the server
    if 1: # no TLS/SSL-secured communication (i.e., over HTTP)
        with grpc.insecure_channel(f'{server_host}:{server_port}') as channel:
            doSomething(channel)
    elif 0:  # TLS/SSL-secured communication (i.e., over HTTPS) directly to service
        with grpc.secure_channel(f'{server_host}:{server_port}',credentials) as channel:
            doSomething(channel)
    elif 1:  # TLS/SSL-secured communication (i.e., over HTTPS) to daemon
        server_host, server_port = '127.0.0.1', 8088
        credentials = grpc.ssl_channel_credentials(open('/home/blake_anderton/snetd_test/ca.pem','rb').read())
        with grpc.secure_channel(f'{server_host}:{server_port}',credentials) as channel:
            doSomething(channel)
        


if __name__ == '__main__':
    main()