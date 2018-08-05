'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    directory = {}
    for character in text:
        if character in directory:
            directory[character] += 1
        else:
            directory[character] = 1


    for element in directory:
        print(str(element) + ' ' + str(directory[element]))





def count_char_insensitive(text):
    directory = {}
    text = text.lower()
    for character in text:
        if character in directory:
            directory[character] += 1
        else:
            directory[character] = 1

    for element in directory:
        print(str(element) + ' ' + str(directory[element]))



# bonus task:
def count_char_ordered(text):
    directory = {}
    for character in text.lower():
        if character in directory:
            directory[character] += 1
        else:
            directory[character] = 1
            
    y= sorted(directory.items(), key=lambda x: x[1], reverse=True)

    for element in y:
        print(str(element[0]) + ' ' + str(element[1]))
    

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)

