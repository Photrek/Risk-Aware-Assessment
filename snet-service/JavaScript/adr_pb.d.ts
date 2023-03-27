// package: adr
// file: adr.proto

import * as jspb from "google-protobuf";

export class InputString extends jspb.Message {
  getS(): string;
  setS(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InputString.AsObject;
  static toObject(includeInstance: boolean, msg: InputString): InputString.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InputString, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InputString;
  static deserializeBinaryFromReader(message: InputString, reader: jspb.BinaryReader): InputString;
}

export namespace InputString {
  export type AsObject = {
    s: string,
  }
}

export class ADRReturnFloat extends jspb.Message {
  getA(): number;
  setA(value: number): void;

  getD(): number;
  setD(value: number): void;

  getR(): number;
  setR(value: number): void;

  getImg(): string;
  setImg(value: string): void;

  getNumr(): number;
  setNumr(value: number): void;

  getNumc(): number;
  setNumc(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ADRReturnFloat.AsObject;
  static toObject(includeInstance: boolean, msg: ADRReturnFloat): ADRReturnFloat.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ADRReturnFloat, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ADRReturnFloat;
  static deserializeBinaryFromReader(message: ADRReturnFloat, reader: jspb.BinaryReader): ADRReturnFloat;
}

export namespace ADRReturnFloat {
  export type AsObject = {
    a: number,
    d: number,
    r: number,
    img: string,
    numr: number,
    numc: number,
  }
}

