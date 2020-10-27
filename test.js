const assert = require("assert");
const permutation = require("./chapter1/permutation.js");
const isUnique = require("./chapter1/isUnique.js");
// test("permutation works", () => {
//   expect(permutation("dog", "god")).toBeTruthy();
// });

it("should return true", () => {
  assert.equal(permutation("dog", "god"), true);
});

it("should return false", () => {
  assert.equal(isUnique("abbcd"), false);
});
