// source: adr.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = (function() {
  if (this) { return this; }
  if (typeof window !== 'undefined') { return window; }
  if (typeof global !== 'undefined') { return global; }
  if (typeof self !== 'undefined') { return self; }
  return Function('return this')();
}.call(null));

goog.exportSymbol('test_risk_aware_assessment_photrek.ADRReturnFloat', null, global);
goog.exportSymbol('test_risk_aware_assessment_photrek.InputString', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
test_risk_aware_assessment_photrek.InputString = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(test_risk_aware_assessment_photrek.InputString, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  test_risk_aware_assessment_photrek.InputString.displayName = 'test_risk_aware_assessment_photrek.InputString';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
test_risk_aware_assessment_photrek.ADRReturnFloat = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(test_risk_aware_assessment_photrek.ADRReturnFloat, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  test_risk_aware_assessment_photrek.ADRReturnFloat.displayName = 'test_risk_aware_assessment_photrek.ADRReturnFloat';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
test_risk_aware_assessment_photrek.InputString.prototype.toObject = function(opt_includeInstance) {
  return test_risk_aware_assessment_photrek.InputString.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!test_risk_aware_assessment_photrek.InputString} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
test_risk_aware_assessment_photrek.InputString.toObject = function(includeInstance, msg) {
  var f, obj = {
    s: jspb.Message.getFieldWithDefault(msg, 1, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!test_risk_aware_assessment_photrek.InputString}
 */
test_risk_aware_assessment_photrek.InputString.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new test_risk_aware_assessment_photrek.InputString;
  return test_risk_aware_assessment_photrek.InputString.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!test_risk_aware_assessment_photrek.InputString} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!test_risk_aware_assessment_photrek.InputString}
 */
test_risk_aware_assessment_photrek.InputString.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setS(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
test_risk_aware_assessment_photrek.InputString.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  test_risk_aware_assessment_photrek.InputString.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!test_risk_aware_assessment_photrek.InputString} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
test_risk_aware_assessment_photrek.InputString.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getS();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
};


/**
 * optional string s = 1;
 * @return {string}
 */
test_risk_aware_assessment_photrek.InputString.prototype.getS = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!test_risk_aware_assessment_photrek.InputString} returns this
 */
test_risk_aware_assessment_photrek.InputString.prototype.setS = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.toObject = function(opt_includeInstance) {
  return test_risk_aware_assessment_photrek.ADRReturnFloat.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!test_risk_aware_assessment_photrek.ADRReturnFloat} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.toObject = function(includeInstance, msg) {
  var f, obj = {
    a: jspb.Message.getFloatingPointFieldWithDefault(msg, 1, 0.0),
    d: jspb.Message.getFloatingPointFieldWithDefault(msg, 2, 0.0),
    r: jspb.Message.getFloatingPointFieldWithDefault(msg, 3, 0.0),
    img: jspb.Message.getFieldWithDefault(msg, 4, ""),
    numr: jspb.Message.getFieldWithDefault(msg, 5, 0),
    numc: jspb.Message.getFieldWithDefault(msg, 6, 0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!test_risk_aware_assessment_photrek.ADRReturnFloat}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new test_risk_aware_assessment_photrek.ADRReturnFloat;
  return test_risk_aware_assessment_photrek.ADRReturnFloat.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!test_risk_aware_assessment_photrek.ADRReturnFloat} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!test_risk_aware_assessment_photrek.ADRReturnFloat}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setA(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setD(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setR(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setImg(value);
      break;
    case 5:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setNumr(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setNumc(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  test_risk_aware_assessment_photrek.ADRReturnFloat.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!test_risk_aware_assessment_photrek.ADRReturnFloat} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getA();
  if (f !== 0.0) {
    writer.writeFloat(
      1,
      f
    );
  }
  f = message.getD();
  if (f !== 0.0) {
    writer.writeFloat(
      2,
      f
    );
  }
  f = message.getR();
  if (f !== 0.0) {
    writer.writeFloat(
      3,
      f
    );
  }
  f = message.getImg();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = message.getNumr();
  if (f !== 0) {
    writer.writeInt32(
      5,
      f
    );
  }
  f = message.getNumc();
  if (f !== 0) {
    writer.writeInt32(
      6,
      f
    );
  }
};


/**
 * optional float a = 1;
 * @return {number}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.getA = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 1, 0.0));
};


/**
 * @param {number} value
 * @return {!test_risk_aware_assessment_photrek.ADRReturnFloat} returns this
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.setA = function(value) {
  return jspb.Message.setProto3FloatField(this, 1, value);
};


/**
 * optional float d = 2;
 * @return {number}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.getD = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 2, 0.0));
};


/**
 * @param {number} value
 * @return {!test_risk_aware_assessment_photrek.ADRReturnFloat} returns this
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.setD = function(value) {
  return jspb.Message.setProto3FloatField(this, 2, value);
};


/**
 * optional float r = 3;
 * @return {number}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.getR = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 3, 0.0));
};


/**
 * @param {number} value
 * @return {!test_risk_aware_assessment_photrek.ADRReturnFloat} returns this
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.setR = function(value) {
  return jspb.Message.setProto3FloatField(this, 3, value);
};


/**
 * optional string img = 4;
 * @return {string}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.getImg = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/**
 * @param {string} value
 * @return {!test_risk_aware_assessment_photrek.ADRReturnFloat} returns this
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.setImg = function(value) {
  return jspb.Message.setProto3StringField(this, 4, value);
};


/**
 * optional int32 numr = 5;
 * @return {number}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.getNumr = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 5, 0));
};


/**
 * @param {number} value
 * @return {!test_risk_aware_assessment_photrek.ADRReturnFloat} returns this
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.setNumr = function(value) {
  return jspb.Message.setProto3IntField(this, 5, value);
};


/**
 * optional int32 numc = 6;
 * @return {number}
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.getNumc = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 6, 0));
};


/**
 * @param {number} value
 * @return {!test_risk_aware_assessment_photrek.ADRReturnFloat} returns this
 */
test_risk_aware_assessment_photrek.ADRReturnFloat.prototype.setNumc = function(value) {
  return jspb.Message.setProto3IntField(this, 6, value);
};


goog.object.extend(exports, test_risk_aware_assessment_photrek);