// package: adr
// file: adr.proto

import * as adr_pb from "./adr_pb";
import {grpc} from "@improbable-eng/grpc-web";

type ServiceDefinitionadr = {
  readonly methodName: string;
  readonly service: typeof ServiceDefinition;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof adr_pb.InputString;
  readonly responseType: typeof adr_pb.ADRReturnFloat;
};

export class ServiceDefinition {
  static readonly serviceName: string;
  static readonly adr: ServiceDefinitionadr;
}

export type ServiceError = { message: string, code: number; metadata: grpc.Metadata }
export type Status = { details: string, code: number; metadata: grpc.Metadata }

interface UnaryResponse {
  cancel(): void;
}
interface ResponseStream<T> {
  cancel(): void;
  on(type: 'data', handler: (message: T) => void): ResponseStream<T>;
  on(type: 'end', handler: (status?: Status) => void): ResponseStream<T>;
  on(type: 'status', handler: (status: Status) => void): ResponseStream<T>;
}
interface RequestStream<T> {
  write(message: T): RequestStream<T>;
  end(): void;
  cancel(): void;
  on(type: 'end', handler: (status?: Status) => void): RequestStream<T>;
  on(type: 'status', handler: (status: Status) => void): RequestStream<T>;
}
interface BidirectionalStream<ReqT, ResT> {
  write(message: ReqT): BidirectionalStream<ReqT, ResT>;
  end(): void;
  cancel(): void;
  on(type: 'data', handler: (message: ResT) => void): BidirectionalStream<ReqT, ResT>;
  on(type: 'end', handler: (status?: Status) => void): BidirectionalStream<ReqT, ResT>;
  on(type: 'status', handler: (status: Status) => void): BidirectionalStream<ReqT, ResT>;
}

export class ServiceDefinitionClient {
  readonly serviceHost: string;

  constructor(serviceHost: string, options?: grpc.RpcOptions);
  adr(
    requestMessage: adr_pb.InputString,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: adr_pb.ADRReturnFloat|null) => void
  ): UnaryResponse;
  adr(
    requestMessage: adr_pb.InputString,
    callback: (error: ServiceError|null, responseMessage: adr_pb.ADRReturnFloat|null) => void
  ): UnaryResponse;
}

