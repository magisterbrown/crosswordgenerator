import argparse
from crossgen.execution import Project, data_sets
from crossgen.dictionary import create_set



def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a",
        "--add",
        metavar="",
        nargs=2,
        help="add new data set [set name] [words file]",
    )
    parser.add_argument(
        "-s", "--start", metavar="", help="run with selected data set [set name]"
    )
    parser.add_argument(
        "-g", "--getlist", action="store_true", help="get list of data sets"
    )
    return parser.parse_args()


if __name__ == "__main__":
    PROP = arguments()
    create_set(PROP.add)
    data_sets(PROP.getlist)

    V = Project(PROP.start)
    V.display_loop()
