export default class Building {
  constructor(sqft) {
    if (this.evacuationWarningMessage === undefined && this.constructor !== Building) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(Newsqft) {
    this._sqft = Newsqft;
  }
}
