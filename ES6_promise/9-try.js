function guardrail(mathFunction) {
  // Array to store results and error messages
  const queue = [];

  try {
    // Execute the provided mathFunction
    const result = mathFunction();
    // Push the result to the queue
    queue.push(result);
  } catch (error) {
    // If an error is thrown, push the error message to the queue
    queue.push(error.toString());
  }
  // Always push the message to the queue
  queue.push('Guardrail was processed');
  return queue;
}

export default guardrail;
