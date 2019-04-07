#main class used for translation app
import collections, random
import sys


class Check:
    def __init__(self):
        self.lang = ""
        self.dictionary = {}

    def set_lang(self):
        print("jaki język?")
        language = input().lower()
        polski = {"polski", "polish", "pl"}
        indo = {"indo", "indonezyjski", "indonesian"}
        while language not in (indo.union(polski)):
            if language in {"^quit", "^exit"}:
                sys.exit("koniec")
            print("wprowadz poprawny język")
            language = input().lower()
        if language in indo:
            self.lang = "indo"
        else:
            self.lang = "pl"

    def check_transl(self, word_in, word_out):
        print(word_in)
        x = input().lower()
        while x != word_out:
            if x in {"^quit", "^exit"}:
                sys.exit("koniec")
            print("źle")
            x = input().lower()
        print("dobrze")

    def check_all_util(self):
        if self.lang == "indo":
            print("tłumaczenie na polski: ")
        else:
            print("tłumaczenie na indo: ")
        keys = list(self.dictionary.keys())
        random.shuffle(keys)
        for word in keys:
            self.check_transl(word, self.dictionary[word])   #program gets right dictionary from get_from_file function
        print("the end")

    def check_all(self):
        print("Chcesz poćwiczyć?")
        if input().lower() in {"tak", "yes"}:
            self.get_from_file()
            self.check_all_util()

    def get_from_file(self):
        if self.lang == "indo":
            file_dict = open("indonesian/slownik_indo_to_pl", "r", encoding='utf-8')
        else:
            file_dict = open("indonesian/slownik_pl_to_indo", "r", encoding='utf-8')
        diction = file_dict.read().split()
        for index in range(0, len(diction), 2):
            self.dictionary.setdefault(diction[index], diction[index+1])
        file_dict.close()

    def write_to(self):
        print("Chcesz dopisać słowo?")
        while input().lower() in {"tak", "yes"}:
            words = input()
            word_list = {}
            word_list = words.split()
            self.write_to_util(word_list[0], word_list[1])
            print("Chcesz dopisać słowo?")

    def write_to_util(self, word, word_translation):
        if self.lang == "indo":
            file_dict = open("indonesian/slownik_indo_to_pl", "a", encoding='utf-8')
            file_dict.write("\n" + word + " " + word_translation)
            file_dict.close()
            file_dict = open("indonesian/slownik_pl_to_indo", "a", encoding='utf-8')
            file_dict.write("\n" + word_translation + " " + word)
            file_dict.close()
            print("dopisano indonezyjskie słowo")
        else:
            file_dict = open("indonesian/slownik_pl_to_indo", "a", encoding='utf-8')
            file_dict.write("\n" + word + " " + word_translation)
            file_dict.close()
            file_dict = open("indonesian/slownik_indo_to_pl", "a", encoding='utf-8')
            file_dict.write("\n" + word_translation + " " + word)
            file_dict.close()
            print("dopisano polskie słowo")
