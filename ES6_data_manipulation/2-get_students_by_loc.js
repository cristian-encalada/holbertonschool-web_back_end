export default function getStudentsByLocation(students, city) {
  // Filter students by the specified city
  return students.filter((student) => student.location === city);
}
