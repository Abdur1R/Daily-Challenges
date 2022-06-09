# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

import re
from typing import List

def solution(s: str, query: List[str]) -> List[str]:
    pattern = re.compile(s)
    res = []
    for q in query:
        r = re.match(pattern, q)
        if r:
            res.append(r.string)
    return res
