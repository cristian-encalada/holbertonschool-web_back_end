export default function createReportObject(employeesList) {
  return {
    // Use spread syntax to create a copy of the employeesList object
    allEmployees: { ...employeesList },
    // Receive an employeesList and return the number of departments
    getNumberOfDepartments: () => Object.keys(employeesList).length,
  };
}
