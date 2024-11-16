class Car {
    #engineOn = false; // private field
  
    constructor(make, model) {
      this.make = make;
      this.model = model;
    }
  
    startEngine() {
      this.#engineOn = true;
      console.log(`Engine started for ${this.make} ${this.model}.`);
    }
  
    isEngineOn() {
      return this.#engineOn;
    }
  }
  
  const myCar = new Car('Tesla', 'Model S');
  myCar.startEngine();  // Output: Engine started for Tesla Model S.
  console.log(myCar.isEngineOn()); // Output: true
  


//In JavaScript, we can create private variables by using closures or 
//by using the new # (private fields) syntax.