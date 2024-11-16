class Person {
    // Constructor to initialize object properties
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }
  
    // Method inside the class
    greet() {
      console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
  }
  
  // Creating an instance of the class
  const person1 = new Person('Alice', 30);
  
  // Calling the method
  person1.greet(); // Output: Hello, my name is Alice and I am 30 years old.
  