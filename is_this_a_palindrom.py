word = 'potop'

def is_it_a_palindrom(word):
    if type (word) != str:
        print("Input is not a strong, function won't work") 
    else:
        if word == word[::-1]:
            print(True)
        else:
            print(False)

is_it_a_palindrom(word)