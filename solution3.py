def solve(s):
    #Defining a function to calculate the value of a substring
    def substring_value(sub):
        return sum(ord(char)-ord('a') + 1 for char in sub)
    
    #Extracting the consonant substrings
    consonant_substrings = [sub for sub in s.split('a')if sub]

    #Calculating the values of consonant substrings and returning the maximum
    max_value =max(substring_value(sub)for sub in consonant_substrings)
    return max_value

#  result
print(solve("hello")) #result:52
print(solve("programming")) #result:111
print(solve("python")) #result:104
