# CrosswordGenerator
Crossword Generator is a programm that allows to generate crosswords from custom word sets and solve them.<br/>
At preinstalled word sets dictionarry meanings are used as a questions. 
# Usage
CLI structure: `main.py [-h] [-a ] [-s] [-g]`

optional arguments:<br/>
  `-h, --help`     show this help message and exit<br/>
  `-a  , --add`    add new data set [set name] [words file]<br/>
  `-s , --start`     run with selected data set [set name]<br/>
  `-g, --getlist`  get list of data sets<br/>
  
To get list of avalable word sets run `python main.py -g`<br/>
`Sets:`<br/>
`basic`<br/>
`biology`<br/>
`literature`

Than to strat generation process run `python main.py -s [set name]` with name of one word set.<br/>
Set proportions:<br/>
`SizeX:[int val]`<br/>
`SizeY:[int val]`<br/>
`Words:[int val]`

All word are encrypted like `[question num]xxxxx`. For example word  `home` would look like `1xxx`.
To answer the question write `Answer:``[question num].[anwer]`. All answers are exactly one word.</br>
If answer is incorrect, word place at crossword will be shaded with red. Otherwise word would be inserted at its place.
To find words place write `[question num].`

Commands of `Answer:` field:<br/>
`get_hint` allows to see all answers to questions<br/>
`exit_cr` allows to break execution of programm
