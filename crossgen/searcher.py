import json


class SearchPattern:
    def __init__(self, set_name):

        wordfile_j = open("dictonaries/" + set_name + "/word.txt", "r")
        meanfile_l = open("dictonaries/" + set_name + "/meaning.txt", "r")
        posfile_j = open("dictonaries/" + set_name + "/position.txt", "r")

        self.posfile = json.loads(posfile_j.readline())
        self.wordfile = json.loads(wordfile_j.readline())
        self.meanfile = json.loads(meanfile_l.readline())

    def findfull(self, characters, brd_beg=20, brd_end=20):
        pointer_pos = 0
        char = characters[0][0]
        wordlist = [[], []]

        end_borders = characters.copy()
        end_borders.append(("_", brd_end))

        while self.posfile[char][pointer_pos]:
            for word_pos in self.posfile[char][pointer_pos]:
                correct = 1
                word = self.wordfile[word_pos]
                for key, chval_pos in enumerate(characters):
                    if (
                            len(word) < pointer_pos + chval_pos[1] + 1
                            or pointer_pos >= brd_beg + 1
                            or word[pointer_pos + chval_pos[1]] != chval_pos[0]
                    ):
                        break
                    elif (len(word) - pointer_pos) < (end_borders[key + 1][1] + 1):
                        interact = {
                            "word": word,
                            "indent": pointer_pos,
                            "answer": self.meanfile[word_pos],
                        }
                        if correct < len(wordlist):
                            wordlist[correct].append(interact)
                        else:
                            wordlist.insert(correct, [interact])
                    correct += 1
            pointer_pos += 1
        return wordlist

