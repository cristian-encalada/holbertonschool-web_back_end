import handleProfileSignup from './6-final-user';

handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg')
  .then((resultArray) => {
    console.log(resultArray);
  })
  .catch((error) => {
    console.error(error);
  });
