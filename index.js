console.log("RUNNING");
// console.log(process.argv[2]);

function sayMyName() {
  return `My name is ${process.argv[2]}`;
}

function checkAge(age, ...args) {

  if (age > 20) {
    return 'You can drink!';
  } else {
    return 'No drank fa ya!';
  }
}

// console.log(sayMyName());
console.log(checkAge(+process.argv[2]));
