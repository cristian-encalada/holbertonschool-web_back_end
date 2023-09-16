export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // create a new object using the constructor of the current instance
    return new this.constructor();
  }
}
