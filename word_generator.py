import random

words = ["banana", "armario", "cachorro"] 
word_list_cnt = len(words)

class WordGenerator:
    __level = 0
    __masked_word = ""
    __word_to_guess = ""
    __characters_to_hide = list()

    @staticmethod
    def __generate_masked_word(word, level = 1):
        WordGenerator.__level = level
        WordGenerator.__word_to_guess = word

        for idx in (1, level):
            WordGenerator.__characters_to_hide.append(word[random.randint(0, len(word) - 1)])
        
        WordGenerator.__masked_word = word
        for idx, char_to_hide in enumerate(WordGenerator.__characters_to_hide):
            WordGenerator.__masked_word = WordGenerator.__masked_word.replace(char_to_hide, "_")
        
        return WordGenerator.__masked_word

    @staticmethod
    def get_word(level = 1):
        word_to_guess = words[random.randint(0, word_list_cnt - 1)] 
        WordGenerator.__generate_masked_word(word_to_guess)
        print(WordGenerator.__masked_word)

    @staticmethod
    def guess_char(input_try):
        if WordGenerator.__characters_to_hide.__contains__(input_try):
            WordGenerator.__hit(input_try)
        else: 
            print("Errou")
            WordGenerator.guess_char(input()[0])
        return WordGenerator.__characters_to_hide.__contains__(input_try)

    @staticmethod
    def __hit(input_char):
        str_arr = list(WordGenerator.__masked_word)
        for idx, character in enumerate(WordGenerator.__word_to_guess):
            if(character == input_char):
                str_arr[idx] = character
        print("".join(str_arr))
                
        WordGenerator.__characters_to_hide.remove(input_char)
        if(len(WordGenerator.__characters_to_hide) == 0):
            print("Acertou! A palavra é", WordGenerator.__word_to_guess, sep=" ")
            exit()
        
        WordGenerator.__masked_word = "".join(str_arr)
        WordGenerator.guess_char(input())