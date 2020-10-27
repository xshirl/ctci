function solution(S) {
  let arr = S.split(" ");
  let error = 0;
  let stack = arr.reduce((stack, operation) => {
    if (/^\d+$/.test(operation)) {
      stack.push(parseInt(operation));
    }
    if (operation == "DUP") {
      const lastNum = stack[stack.length - 1] || null;
      if (lastNum != null) {
        stack.push(lastNum);
      }
    }
    if (operation == "POP") {
      if (stack.length > 0) {
        stack.pop();
      }
    }
    if (operation == "+") {
      if (stack.length >= 2) {
        const firstNum = stack.pop();
        const secondNum = stack.pop();
        stack.push(firstNum + secondNum);
      } else {
        error = -1;
      }
    }
    if (operation == "-") {
      if (stack.length >= 2) {
        const firstNum = stack.pop();
        const secondNum = stack.pop();
        stack.push(firstNum - secondNum);
      } else {
        error = -1;
      }
    }
    return stack;
  }, []);
  if (error == -1) {
    return error;
  } else {
    return stack.pop();
  }
}

console.log(solution("3 DUP 5 - -"));
console.log(solution("1 3 -"));
console.log(solution(" 5 DUP + "));
console.log(solution("5 6 + -"));
console.log(solution("15 POP 9 DUP - DUP 2 + + DUP POP DUP +"));
