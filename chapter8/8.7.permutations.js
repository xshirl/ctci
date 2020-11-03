function permuteString(string) {
  const answers = [];
  function recurse(currPerm, remainingChars) {
    if (remainingChars.length === 0) {
      answers.push(currPerm);
    } else {
      for (let i = 0; i < remainingChars.length; i++) {
        recurse(
          currPerm + remainingChars.charAt(i),
          remainingChars.slice(0, i) + remainingChars.slice(i + 1)
        );
      }
    }
  }
  recurse("", string);
  return answers;
}

console.log(permuteString("abcd"));
