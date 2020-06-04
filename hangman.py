from word_generator import WordGenerator

def play(level = 1):
    print("##########################")
    print("####Let's play hangman####")
    print("##########################")
    WordGenerator.get_word()
    WordGenerator.guess_char(input()[0])

if(__name__ == "__main__"):
    play(2)