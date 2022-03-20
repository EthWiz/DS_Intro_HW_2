def reverse(sentence, reverse_word):
    words_in_sentence = sentence.split()
    if reverse_word in words_in_sentence:
        for word in words_in_sentence:
            if reverse_word == word:
                reversedstring=''.join(reversed(word))
                print(reversedstring, end = ' ') 
            else:
                print(word, end = ' ')
    elif isinstance(reverse_word, str) == false:
            print("invalid input")
    else:
        print("no match word found")
      