//Eduardo, Mamudu, and Michele P worked together on this assignment
//We checked other Repos for guidance: Daiana, Tiffany, and Peter.

# Homework
Link to Code in P5: https://editor.p5js.org/Mamudu/sketches/PEPRXjk1x

class Perceptron {
  
  // parameter is number of inputs
  constructor(n){
  // initialize an array of weights here
    this.weights = []
    // should have same amount of weights as inputs
    // weights should be random values between -1 and 1
    for(let i = 0; i < n; i++) {
      this.weights.push(random(-1, 1))
    }
    // don't worry about this until writing training function
     this.learningRate = 0.1; 
  }
  
  // determine if sum of calculated weights and inputs is higher or lower than zero
  
  // return 1 if greater than zero
  // return -1 if less than zero
  activate(sum){
    if(sum > 0){
      return 1;
    } else {
      return -1
    }
  }
  
  //feedForward algorithm
  // 1. multiply each input by its corresponding weight
  // 2. sum all the weighted inputs
  // 3. pass sum through activation function
  
  feedForward(inputs){
  let sum = 0
  for(let i = 0; i < inputs.length; i++) {
    sum += this.weights[i]*inputs[i]
  }
    return this.activate(sum);
  }
  
  // finish training function for homework
  train(inputs, desired){
    // store result of feed forward here
  let guess = this.feedForward(inputs);
   
    
    // error is difference between desired result and guess
  let error = desired-guess;
    
    // adjust all weights by adding learning rate times error times inputs
    //weights1 = + learningRate*error*input1 
    // -> do same for all weights
     for (let i = 0; i < inputs.length; i++) {
      this.weights[i] = this.weights[i] + this.learningRate * error * inputs[i];

    
  }
  
}
}

# Asynch 
https://www.smartsheet.com/neural-network-applications?amp#real-world-and-industry-applications-of-neural-networks

Unsolved problems remain, even for the most sophisticated neural networks. For example, despite its best efforts, Facebook still finds it impossible to identify all hate speech and misinformation by using algorithms. The company employs thousands of human reviewers to resolve the problem. In general, because computers aren’t human, their ability to be genuinely creative — prove math theorems, make moral choices, compose original music, or deeply innovate — is beyond the scope of neural networks and AI.
