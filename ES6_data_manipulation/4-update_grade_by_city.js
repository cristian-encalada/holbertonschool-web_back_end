function updateStudentGradeByCity(students, city, newGrades) {
  return students
    // filter students based on the specified city
    .filter((student) => student.location === city)
    .map((student) => {
      // find the grade in the newGrades array based on the student's id
      const matchedGrade = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        // If a grade matched is found,  assign the grade to the student.
        grade: matchedGrade ? matchedGrade.grade : 'N/A',
      };
    });
}

export default updateStudentGradeByCity;
