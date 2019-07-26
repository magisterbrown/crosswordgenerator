import sys
import ctypes


class Crossword:
    def __init__(self, input_number_x, input_number_y):
        self.crossword = []
        self.answers = []
        self.filled = []
        self.crossword = [[[" "] * 4] * input_number_x] * input_number_y

        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    def display_crossword(self):

        for line in range(len(self.crossword)):
            out = ""
            for char in range(len(self.crossword[0])):
                out = out + self.color(self.crossword[line][char])
                self.crossword[line][char][3] = " "
            if out != len(self.crossword[0]) * " ":
                print(out)

    def display_answers(self, hint):

        if hint == "get_hint":
            for val in self.answers:
                print(str(val["item_num"]) + "." + val["word"])
        elif hint == "exit_cr":
            sys.exit()
        else:
            for val in self.answers:
                print(str(val["item_num"]) + "." + val["question"])

    def load_answer(self, data):
        reserve_copy = [[[vl3 for vl3 in vl2] for vl2 in vl1] for vl1 in self.crossword]
        word_prop = {
            "word": data[0],
            "axis_disp": data[1],
            "y_pos": data[2],
            "x_pos": data[3],
            "question": data[4].strip("\n"),
            "item_num": len(self.answers) + 1,
        }

        for val in self.answers:
            if val["word"] == word_prop["word"]:
                return False

        y_pos = int(word_prop["y_pos"])
        x_pos = int(word_prop["x_pos"])

        output = self.insert_word(word_prop, reserve_copy, y_pos, x_pos)
        if output:
            self.crossword = output
            self.answers.append(word_prop)
        return output

    def insert_word(self, word_prop, reserve_copy, y_pos, x_pos):
        hidden_word = str(len(self.answers) + 1) + len(word_prop["word"]) * "x"
        filled_temp = []
        for letter in word_prop["word"]:
            real_holder = reserve_copy[y_pos][x_pos][0]

            if real_holder.isdigit() and hidden_word[0] != real_holder:
                return False

            if hidden_word[0] == "x":
                position = "x" if word_prop["axis_disp"] == "y" else "y"
                filled_temp.append({"y": y_pos, "x": x_pos, "word_disp": position})

            reserve_copy[y_pos][x_pos][1] = letter
            reserve_copy[y_pos][x_pos][2] = word_prop["axis_disp"]
            reserve_copy[y_pos][x_pos][0] = hidden_word[0]
            hidden_word = hidden_word[1:]

            if word_prop["axis_disp"] == "y":
                y_pos += 1
            else:
                x_pos += 1

        self.filled.extend(filled_temp)
        return reserve_copy

    def check_input(self, in_num, in_data):
        searcher = list(filter(lambda el: el["item_num"] - 1 == in_num, self.answers))
        if searcher:
            word_data = searcher[0]
            y_pos = int(word_data["y_pos"])
            x_pos = int(word_data["x_pos"])
            for character in word_data["word"]:
                if word_data["word"] == in_data.lower():
                    self.crossword[y_pos][x_pos][0] = character
                    self.crossword[y_pos][x_pos][3] = "green"
                else:
                    self.crossword[y_pos][x_pos][3] = "red"
                if word_data["axis_disp"] == "y":
                    y_pos += 1
                else:
                    x_pos += 1
            if word_data["word"] == in_data.lower():
                self.answers.remove(word_data)
    @staticmethod
    def color(value):
        colors = {
            "blue": "\033[94m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "red": "\033[91m",
        }
        if value[3] == " ":
            return value[0]
        return colors[value[3]] + value[0] + "\033[0m"


def split_input(input_number):
    num_out = input_number[: input_number.find(".")]
    word_out = input_number[input_number.find(".") + 1 :]
    if num_out.isdigit():
        return (int(num_out), word_out.lower())
    return False
