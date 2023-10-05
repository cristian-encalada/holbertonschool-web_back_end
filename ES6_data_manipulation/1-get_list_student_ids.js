function getListStudentIds(students) {
  // Check if the input is an array
  if (!Array.isArray(students)) {
    return [];
  }

  // Extract the 'id' values and return them as an array
  return students.map((student) => student.id);
}

export default getListStudentIds;
