class Solution:
    def generateParenthesis(self, n: int):
        return self._genParenHelper(n, 0, 0, "")

    def _genParenHelper(self, n, left, right, str):
        if left + right == 2 * n:
            return [str]

        res = []

        if left < n:
            res += self._genParenHelper(n, left+1, right, str+"(")
        if left > right:
            res += self._genParenHelper(n, left, right+1, str+")")

        return res
