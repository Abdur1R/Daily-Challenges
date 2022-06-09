# Implement regular expression matching with the following special characters:
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
# For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
# Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

def match(str, pat)
    str = str.split("") {!str.respond_to? "each"}
    matches = Array.new(str.length + 1){Array.new(pat.length + 1)}
    matches[0][0] = true 

    for i in 1..matches[0].length do
        matches[0][1] = matches[0][i-2] {pat[i-1].eql? "*"} 
    for i in 1...matches.length do
        for j in 1...matches[0].length do
            if pat[j-1].eql? '.' or pat[j-1].eql? str[i-1]
                matches[i][j] = matches[i-1][j-1]
            else if pat[j-1].eql? '*'
                matches[i][j] = matches[i][j-2]
                if pat[j-2].eql? '.' or pat[j-2].eql? str[i-1] 
                    matches[i][j] = matches[i][j] | matches[i-1][j]
            else  
                matches[i][j] = false 
    return matches[str.length][pat.length]

str = "ray"
pat = "ra."
puts match(str, pat)
