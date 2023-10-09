function hasValuesFromArray(set, arr) {
  // Check if all elements in the array are in the set
  return arr.every((element) => set.has(element));
}

export default hasValuesFromArray;
