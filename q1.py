
#https://leetcode.com/problems/regular-expression-matching/solution/

def isMatch(text, pattern):
    memo = {}
    def dp(i, j):
        "Function loops over the entire set of possible i, j pairs"
        if (i, j) not in memo:
            if j == len(pattern):
                # Checks if the last character in text is the same character in pattern, if yes returns true
                ans = i == len(text)
            else:
                # If the ith character in text is not the last char and jth character in pattern is the any single char from text or ., then returns True
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                # checks if there is a repeat of the char before *
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    # * can allow zero or more occurences
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    # if there is a match for . and the previous portions of text and pattern are the same then dp(i+1, j+1) will be True otherwise False
                    ans = first_match and dp(i+1, j+1)
            # now memo only contains the truth value of the last comparison
            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

print(isMatch('sb', '.b'))
print(isMatch('ab', 'a*b'))
