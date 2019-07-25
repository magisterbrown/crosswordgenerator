from string import ascii_lowercase as alphabet
import random as rn
import sys
import crossgen.searcher as ps
import crossgen.crossword as cr



class Generator:
    def __init__(self, data_set):
        self.finder = ps.SearchPattern(data_set)

        input_x = input("SizeX:")
        input_y = input("SizeY:")
        words_amount = input("Words:")

        if not (input_x.isdigit() and input_y.isdigit() and words_amount.isdigit()):
            sys.exit("inputs should be int")

        self.y_height = int(input_y)+1
        self.x_width = int(input_x)+1
        self.words = int(words_amount)
        self.crs = cr.Crossword(self.x_width, self.y_height)

    def generate(self):

        self.gen_first_word()

        genwords = 1
        while genwords < self.words and self.crs.filled:
            spot = rn.choice(self.crs.filled)
            axis = self.y_height if spot["word_disp"] == "y" else self.x_width
            interactions, brd_left, brd_right = self.find_inter(spot, axis, self.crs)

            if interactions:
                wordlist = self.finder.findfull(interactions, brd_left, brd_right)
                if wordlist and wordlist[-1]:
                    res = rn.choice(wordlist[-1])
                    if spot["word_disp"] == "y":
                        y_point = spot["y"] - res["indent"]
                        x_point = spot["x"]
                    else:
                        y_point = spot["y"]
                        x_point = spot["x"] - res["indent"]

                    out = self.crs.load_answer(
                        [
                            res["word"],
                            spot["word_disp"],
                            y_point,
                            x_point,
                            res["answer"],
                        ]
                    )

                    if out:
                        genwords += 1
                        print(genwords, "/", self.words)
            self.crs.filled = [el for el in self.crs.filled if el != spot]
        return self.crs

    def gen_first_word(self):
        x_half = self.x_width // 2
        y_half = self.y_height // 2
        tries = 0
        while True:
            tries += 1
            if tries > 80:
                sys.exit("no words")
            suitable_words = self.finder.findfull(
                [(rn.choice(alphabet), 0)], x_half-1, x_half-2
            )
            if suitable_words[1]:
                break
        f_word = rn.choice(suitable_words[1])
        self.crs.load_answer([f_word["word"], "x", y_half//2, x_half//2, f_word["answer"]])

    @staticmethod
    def find_inter(spot, axis, crs):

        f_check = False
        brd_left = 0
        brd_right = axis - 1
        interactions = []
        f_inter = 0

        for pos in range(axis):
            inty, intx = (
                (pos, spot["x"]) if spot["word_disp"] == "y" else (spot["y"], pos)
            )
            cell = crs.crossword[inty][intx]
            if inty == spot["y"] and intx == spot["x"] and cell[0] == "x":
                f_inter = pos
                f_check = True

            if crs.crossword[inty][intx][0] == "x" or cell[0].isdigit():
                if not f_check:
                    brd_left = pos
                elif cell[2] != spot["word_disp"]:
                    interactions.append((cell[1], pos - f_inter))
                else:
                    brd_right = pos
                    break
        return (interactions, f_inter - brd_left, brd_right - f_inter)
