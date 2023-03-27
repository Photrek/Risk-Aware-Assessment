// package: adr
// file: adr.proto

var adr_pb = require("./adr_pb");
var grpc = require("@improbable-eng/grpc-web").grpc;

var ServiceDefinition = (function () {
  function ServiceDefinition() {}
  ServiceDefinition.serviceName = "adr.ServiceDefinition";
  return ServiceDefinition;
}());

ServiceDefinition.adr = {
  methodName: "adr",
  service: ServiceDefinition,
  requestStream: false,
  responseStream: false,
  requestType: adr_pb.InputString,
  responseType: adr_pb.ADRReturnFloat
};

exports.ServiceDefinition = ServiceDefinition;

function ServiceDefinitionClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}

ServiceDefinitionClient.prototype.adr = function adr(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(ServiceDefinition.adr, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
  return {
    cancel: function () {
      callback = null;
      client.close();
    }
  };
};

exports.ServiceDefinitionClient = ServiceDefinitionClient;

