/*
The function should return an object with the following format:
{
     $departmentName: [
          $employees,
     ],
}
*/
export default function createEmployeesObject(departmentName, employees) {
  // Use template literals to create the key
  return { [`${departmentName}`]: employees };
}
