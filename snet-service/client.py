# tutorial
# 7003

import os
import sys
import grpc

sys.path.append("./service_spec")
import adr_pb2 as pb2
import adr_pb2_grpc as pb2_grpc


def get_filepath(filename, extension):
    return f'{filename}{extension}'

def read_iterfile(filepath, chunk_size=1024):
    split_data = os.path.splitext(filepath)
    filename = split_data[0]
    extension = split_data[1]

    metadata = pb2.MetaData(filename=filename, extension=extension)
    yield pb2.UploadFileRequest(metadata=metadata)
    with open(filepath, mode='rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if chunk:
                entry_request = pb2.UploadFileRequest(chunk_data=chunk)
                yield entry_request
            else:
                return

def run():
    with grpc.insecure_channel('localhost:7003') as channel:
        stub = pb2_grpc.ServiceDefinitionStub(channel)

        filename = sys.argv[1]
        response = stub.ADR(read_iterfile(filename))
        print(response.message)

        for entry_response in stub.DownloadFile(pb2.MetaData(filename='hist', extension='.png')):
            with open('hist.png', mode="ab") as f:
                f.write(entry_response.chunk_data)
    
if __name__ == '__main__':
    run()
