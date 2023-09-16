export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // code attribute

  get code() {
    return this._code;
  }

  set code(NewCode) {
    this._code = NewCode;
  }

  // name attribute

  get name() {
    return this._name;
  }

  set name(NewName) {
    this._name = NewName;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
