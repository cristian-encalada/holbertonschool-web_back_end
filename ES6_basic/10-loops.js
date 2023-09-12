export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];

  for (const value of array) {
    // Append the string to the current value and push it into the new array
    newArray.push(appendString + value);
  }

  return newArray;
}
