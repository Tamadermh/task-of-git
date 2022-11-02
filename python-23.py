'''
def numbers_to_words (number):
    number2word = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
            '7': "seven", '8': "eight", '9': "nine", '0': "zero"}
    return " ".join(map(lambda i: number2word[i], str(number)))

number=int(input("enter number to transfer to print as string "))
print(numbers_to_words(number))

print("Number to words . Create a python function that takes an integer number and print the number in words")
number=int(input("enter number to transfer to print as string "))
def number_to_word(number):
    if type(number)==int and number<=10 and number>=0:  
        match number:
            case 0:
                return "zero"
            case 1:
                return "one"
            case 2:
                return"two"
            case 3:
                return"three"
            case 4:
                return"four"
            case 5:
                return"five"
            case 6:
                return"sex"
            case 7:
                return"seven"
            case 8:
                return"eight"
            case 9:
                return"nine"
            case 10:
                return"ten"
    else :
        return"the number not found"
    
print(number_to_word(number))
'''

