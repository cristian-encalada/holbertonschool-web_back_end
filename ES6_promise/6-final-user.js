import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  // Create promises for signUpUser and uploadPhoto functions
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);
  // Promise.allSettled waits for both promises
  return Promise.allSettled([signUpPromise, uploadPromise])
    .then((results) => {
      // Extract and format the result of the signUpPromise
      const signUpResult = {
        status: results[0].status,
        value: results[0].value,
      };
      // Extract and format the result of the uploadPromise
      const uploadResult = {
        status: results[1].status,
        // Convert the error to a string (for uniformity)
        value: results[1].reason.toString(),
      };
      // Return an array containing both results
      return [signUpResult, uploadResult];
    });
}

export default handleProfileSignup;
