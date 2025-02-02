def reverse_words(sentence):
    words = sentence.split()  # Split sentence into list of words
    reversed_sentence = ' '.join(reversed(words))  # Reverse list of words and join them back into a sentence
    return reversed_sentence

string = input("Enter a sentence: ")
print("Reversed sentence:", reverse_words(string))