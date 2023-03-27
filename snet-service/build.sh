#!/bin/bash

python3 -m grpc_tools.protoc -I=./ --python_out=./Python --grpc_python_out=./Python ./adr.proto;

protoc \
--plugin=protoc-gen-ts=/home/hxyue1/Documents/snet/snet-dapp-raa/node_modules/.bin/protoc-gen-ts \
--js_out=import_style=commonjs,binary,namespace_prefix=adr:./JavaScript \
--ts_out=service=true:./JavaScript \
adr.proto;
