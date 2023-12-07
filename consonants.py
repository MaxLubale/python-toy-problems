def solve(s):
    vowels = "aeiou"
    consonant_values = {letter: index + 1 for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz") if letter not in vowels}
    
    def get_consonant_value(substring):
        return sum(consonant_values[char] for char in substring)
    
    max_value = 0
    current_substring = ""

    for char in s:
        if char not in vowels:
            current_substring += char
        elif current_substring:
            max_value = max(max_value, get_consonant_value(current_substring))
            current_substring = ""

    # Check for the last substring in case the string ends with a consonant
    if current_substring:
        max_value = max(max_value, get_consonant_value(current_substring))

    return max_value

# Examples
print(solve("zodiacs"))  
print(solve("strength"))  


