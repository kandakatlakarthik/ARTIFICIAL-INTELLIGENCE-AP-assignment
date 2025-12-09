/**
 * Takes an array of student names and prints each name to the console.
 * @param {string[]} students - An array of student names.
 */
function printStudents(students) {
  console.log("Student List:");
  students.forEach(student => {
    console.log(student);
  });
}

// Sample data
const studentNames = ["Alice", "Bob", "Charlie"];

// Test the function
printStudents(studentNames);
