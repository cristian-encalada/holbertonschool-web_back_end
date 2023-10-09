function updateUniqueItems(map) {
  // Function that returns an updated map for all items with initial quantity at 1
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // For each entry of the map where the quantity is 1, update the quantity to 100
  for (const [item, quantity] of map.entries()) {
    if (quantity === 1) {
      map.set(item, 100);
    }
  }
}

export default updateUniqueItems;
