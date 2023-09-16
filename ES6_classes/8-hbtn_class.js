export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  valueOf() {
    // Return the numeric representation of the object
    return this._size;
  }

  toString() {
    // Return the string representation of the object
    return this._location;
  }
}
