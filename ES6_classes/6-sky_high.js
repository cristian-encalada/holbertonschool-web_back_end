import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    // call the constructor of the parent class (Building)
    super(sqft);
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
