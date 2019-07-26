# CrosswordGenerator
Crossword Generator is a programm that allows to generate crosswords from custom word sets and solve them.<br/>
At preinstalled word sets dictionarry meanings are used as a questions. 
# Usage
CLI structure: `main.py [-h] [-a ] [-r] [-g]`

optional arguments:<br/>
  `-h, --help`     show this help message and exit<br/>
  `-a  , --add`    add new data set [set name] [words file]<br/>
  `-r , --run`     run with selected data set [set name]<br/>
  `-g, --getlist`  get list of data sets<br/>
  
To get list of avalable word sets run `python main.py -g`<br/>
`Sets:`<br/>
`basic`<br/>
`biology`<br/>
`literature`

Than to strat generation process run `python main.py -r [set name]` with name of one word set.<br/>
Set proportions:<br/>
`SizeX:[int val]`<br/>
`SizeY:[int val]`<br/>
`Words:[int val]`<br/>

