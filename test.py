def validPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    count = 0
    while l <= r:
        if s[l] == s[r]:
            print(s[l], s[r])
            l += 1
            r -= 1
        elif s[l + 1] == s[r]:
            print(s[l + 1], s[r])
            l += 2
            r -= 1
            count += 1

        elif s[l] == s[r - 1]:
            print(s[l], s[r - 1])
            l += 1
            r -= 2
            count += 1
        else:
            print(s[l], s[r])
            return False
    return count <= 1


s = """aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"""

b = validPalindrome(s)
print(b)
