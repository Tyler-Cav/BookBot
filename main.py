def main (): 
            
    bookCharacterCounts =	{}

    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        def howManyWords(): 
            words = file_contents.split()
            print(f'{len(words)} words found in the document')
        
        # Looping over dictionary to check if the character key already exists
        lowerCase = file_contents.lower()
        for z in lowerCase:
            if bookCharacterCounts.get(z) == None:
                bookCharacterCounts[f'{z}'] = 1
            else: 
                bookCharacterCounts[z] += 1
        # print(bookCharacterCounts)
        print ('--Begin report of books/frankenstein.txt--')
        howManyWords()
        for char in bookCharacterCounts:
            if char.isalpha() == True:
                print(f'The {char} character was found {bookCharacterCounts[char]} times')
            
main()

  