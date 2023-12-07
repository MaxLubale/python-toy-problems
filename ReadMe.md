# PYTHON TOY PROBLEMS

## Overview
  This repository contains solutions to three Python challenges for Phase 3 Week 1. The challenges focus on various aspects of Python programming, including string manipulation, conditional statements, and function definition.

## Challenges

## Challenge 1: Converting 12-hour time to 24-hour time
 - This challenge involves converting a 12-hour time format (e.g., "8:30 am" or "8:30 pm") to a 24-hour time format (e.g., "0830" or "2030"). The task requires defining a function that takes an hour (in the range of 1 to 12), a minute (in the range of 0 to 59), and a period ("am" or "pm") as input. The function returns a four-digit string encoding the time in 24-hour format.
   ## Examples
convert_to_24_hour(8, 30, "am")  # Output: "0830"
convert_to_24_hour(8, 30, "pm")  # Output: "2030"


## Challenge 2: Two numbers are positive
 - The goal of this challenge is to write a function that takes three integers (a, b, and c) as arguments and returns True if exactly two of the three integers are positive numbers (greater than zero) and False otherwise.
 
  ## Examples
is_two_positive(2, 4, -3)  # Output: True
is_two_positive(-4, 6, 8)  # Output: True
is_two_positive(4, -6, 9)  # Output: True
is_two_positive(-4, 6, 0)  # Output: False
is_two_positive(4, 6, 10)  # Output: False
is_two_positive(-14, -3, -4)  # Output: False

## Challenge 3: Consonant value
- This challenge involves creating a function that takes a lowercase string containing only alphabetic characters (no spaces). The function should return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou." Each consonant is assigned a value, such as a = 1, b = 2, c = 3, and so on.

  ## Examples
highest_consonant_value("zodiacs")  # Output: 26
highest_consonant_value("strength")  # Output: 57

- For the word "zodiacs," the consonant substrings are "z," "d," and "cs," with values 26, 4, and 22, respectively. The highest is 26.
- For the word "strength," the consonant substrings are "str" and "ngth," with values 57 and 49, respectively. The highest is 57.

## How to Use
- Clone this repository to your local machine.
- Review the Python files for each challenge to understand the solutions.
- Run the Python files and test the functions with additional examples if desired.
- Contribution
-  Feel free to contribute by suggesting improvements, optimizations, or additional challenges. Open an issue or create a pull request with your suggestions.

Happy coding!

## License
This project is licensed under the MIT License - see the [LICENSE] file for details.