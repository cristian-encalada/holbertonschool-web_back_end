import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  // Create promises for signUpUser and uploadPhoto functions
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  // Promise.allSettled waits for both promises (resolve or reject)
  return Promise.allSettled([signUpPromise, uploadPromise])
    .then((results) => {
      const resultArray = [];
      for (const result of results) {
        resultArray.push({
          status: result.status,
          value: result.status === 'resolved' ? result.value : result.reason,
        });
      }
      return resultArray;
    });
}

export default handleProfileSignup;
