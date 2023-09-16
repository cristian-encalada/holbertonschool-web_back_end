export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  toString() {
    // Change the string representation of an Airport object
    return `[object ${this._code}]`;
  }
}
