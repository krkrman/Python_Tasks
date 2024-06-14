import os


def countNumber4(list):
    counter = 0
    for num in list:
        if num == 4:
            counter += 1
    print("number 4 counts = ", counter)


def checkIfVowel(letter: str):
    if letter.lower() in ["a", "e", "i", "o", "u"]:
        print("The letter is Vowel")
    else:
        print("The letter is not vowel")

def print_environment_variable(variable_name):
    
    variable_value = os.environ[variable_name]
    print(f"{variable_name}: {variable_value}")


countNumber4([1, 2, 3, 4, 5, 4, 8, 4, 96, 4])
checkIfVowel("O")
checkIfVowel("s")
print_environment_variable("PATH")