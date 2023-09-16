// import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  // amount attribute

  get amount() {
    return this._amount;
  }

  set amount(Newamount) {
    this._amount = Newamount;
  }

  // currency attribute

  get currency() {
    return this._currency;
  }

  set currency(NewCurrency) {
    this._currency = NewCurrency;
  }

  displayFullPrice() {
    // returns the attributes in this format: amount currency_name (currency_code).
    const { _name, _code } = this._currency;
    return `${this._amount} ${_name} (${_code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
