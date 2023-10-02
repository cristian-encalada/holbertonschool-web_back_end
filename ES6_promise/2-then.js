function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      return { status: 200, body: 'success' };
    })
    .catch(() => {
      console.error('Got a response from the API');
      return new Error(); // Return an empty Error object
    });
}

export default handleResponseFromAPI;
