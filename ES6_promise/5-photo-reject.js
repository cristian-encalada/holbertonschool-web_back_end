export default function uploadPhoto(fileName) {
  // Using template literals for the error msg, backticks(``) != single quotes ('')
  return Promise.reject(new Error(`${fileName} cannot be processed`));
}
