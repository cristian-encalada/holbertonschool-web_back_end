function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);

  const data = new DataView(buffer);

  // Store the Int8 value at the specified position
  data.setInt8(position, value);

  return data;
}

export default createInt8TypedArray;
