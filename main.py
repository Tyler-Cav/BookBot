def main (): 
            
    bookCharacterCounts =	{}

    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        def howManyWords(): 
            words = file_contents.split()
            print(len(words))
        howManyWords()
        
        # Looping over dictionary to check if the character key already exists
        lowerCase = file_contents.lower()
        for z in lowerCase:
            if bookCharacterCounts.get(z) == None:
                bookCharacterCounts[f'{z}'] = 1
            else: 
                bookCharacterCounts[z] += 1
        print(bookCharacterCounts)
                
main()

  