function getResponseFromAPI() {
  return Promise.resolve();
}

/* Another way to create a new promise (with the executor function)
  return new Promise((resolve) => {
  resolve(); // Resolves immediately with no value
});
*/
export default getResponseFromAPI;
