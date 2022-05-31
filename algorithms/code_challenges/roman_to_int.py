def roman_to_int(self, s: str) -> int:
    roman_int_map = {'I': 1 , 'V': 5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M': 1000}
    i, result = 0, 0
    while i < len(s):
        if i == len(s)-1 or roman_int_map[s[i]] >= roman_int_map[s[i+1]]:
            result += roman_int_map[s[i]] 
            i+=1
        else:
            result += roman_int_map[s[i+1]] - roman_int_map[s[i]]
            i+=2
    return result