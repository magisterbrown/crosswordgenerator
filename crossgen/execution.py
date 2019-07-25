import sys
import os
import crossgen.crossword as cr
import crossgen.generator as gn



class Project:
    def __init__(self, words):

        if not words:
            sys.exit()
        creator = gn.Generator(words + "_set")
        self.crossword = creator.generate()

    def display_loop(self):
        input_ans = ""
        while True:
            print("\n")
            self.crossword.display_crossword()
            print("\n")

            self.crossword.display_answers(input_ans)
            input_ans = input("Answer:")
            self.input_checkup(input_ans)

    def input_checkup(self, input_ans):
        result = cr.split_input(input_ans)
        if result:
            self.crossword.check_input(result[0] - 1, result[1])
            if not self.crossword.answers:
                print("\ncomplete")
                sys.exit()


def data_sets(show):
    if show:
        sets = os.listdir("dictonaries")
        print("Sets:\n")
        for val in sets:
            if val[-3:] == "set":
                print(val[:-4])
