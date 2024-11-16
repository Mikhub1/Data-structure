abstract class Shape {
    constructor(name) {
      this.name = name;
    }
  
    area() {
      console.log("The area depends on the shape");
    }
  }
  
  class Circle extends Shape {
    constructor(radius) {
      super('Circle');
      this.radius = radius;
    }
  
    area() {
      return Math.PI * this.radius * this.radius;
    }
  }
  
  class Rectangle extends Shape {
    constructor(width, height) {
      super('Rectangle');
      this.width = width;
      this.height = height;
    }
  
    area() {
      return this.width * this.height;
    }
  }
  
  const shapes = [new Circle(5), new Rectangle(4, 5), new Shape("Triangle")];
  
  shapes.forEach(shape => {
    console.log(`${shape.name} area: ${shape.area()}`);
  });

  //Polymorphism allows a method to do different things based on the object that calls it. We can achieve this through method
  // overriding (as shown above) or through object prototypes.
  