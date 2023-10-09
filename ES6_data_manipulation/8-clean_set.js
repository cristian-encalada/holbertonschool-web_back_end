function cleanSet(set, startString) {
  const cleanedValues = [];

  // Check if startString is not a string or is empty
  if (typeof startString !== 'string' || startString === '') {
    // Return an empty string
    return '';
  }

  for (const value of set) {
    if (value !== undefined && typeof startString === 'string' && value.startsWith(startString)) {
      // If the value starts with the startString, append the rest of the string to the array
      cleanedValues.push(value.substring(startString.length));
    }
  }

  // Join all values with "-" and return the result
  return cleanedValues.join('-');
}

export default cleanSet;
