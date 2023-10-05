export default function getStudentIdsSum(students) {
  // Calculate the sum of all the student ids
  return students.reduce((sum, student) => sum + student.id, 0);
}
