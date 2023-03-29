bracket_map = {
            "{" : "}",
            "[" : "]",
            "(" : ")"

        }
s = input()
allkeys = bracket_map.keys()
is_valid = False
    #iterating through the string
for i in range(len(s)):
    if s[i] in bracket_map.keys():
             if s[i+1] == bracket_map.get(s[i]) and len(s[i+1]) < len(s):
                    is_valid = True
                    
print(is_valid)
    
