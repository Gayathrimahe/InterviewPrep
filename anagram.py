"""" check if the given strings are anagrams or not---->
if the jumbled word makes a new word ,then its a anagram
The sorted() function returns a sorted list of the specified iterable object."""


def finding_anagram(s1, s2):
    if (sorted(s1)==sorted(s2)):
        print(f"{s1},{s2} are anagrams")
    else:
        print(f"{s1}, {s2} are not anagrams")

finding_anagram('travis', 'resist')
finding_anagram('silent', 'listen')