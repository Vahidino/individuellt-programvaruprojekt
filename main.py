"""LinterCleanter"""
import sys # vi använder detta för att kunna ta in parameter från när vi kör programmet
import argparse
import json
import corrector

def main():
    """Om vi har mindre än 2 argument, dvs. bara programnamnet"""
if len(sys.argv) < 2:
    print("Usage: main.py <file> [options] or h for help")
    sys.exit(1)
parser = argparse.ArgumentParser(add_help=False)
parser = argparse.ArgumentParser(prog='myprogram',
description='Lintercleanter.')
parser.add_argument('-r','--rep',help= "Usage: main.py [FILE] [OPTION]\n"
  "-l, --linebreaks\tAdd line breaks to the text\n"
  "-t, --tabs\t\tAdd tabs to the text"
  "Example: main.py -l text.txt")
arg = parser.parse_args

# json config file
json_file = open("config.json", "r", encoding="utf-8").read()
json_data = json.loads(json_file) # läser in json filen och gör om den till en dictionary

# file to edit
file = open(sys.argv[1], "r", encoding="utf-8").read()

new_line_size = json_data["new_line_size"]
tab_size = json_data["tab_size"]

#override config file
def settings(json_data):
    """change the setting"""
    if sys.argv[3] and sys.argv[4] != 0:
        binput = sys.argv[3]
        cinput = sys.argv[4]
        buster = binput * new_line_size;
        custer = cinput * tab_size;
    else:
        buster = new_line_size;
        custer = tab_size;

    return buster, custer;

  # implementera argv
  #override config file
  #kallar på funktionen i corrector.py
new_text = corrector.add_new_lines(file, buster)
new_text = corrector.add_space_after_comment(new_text, custer)
new_text = corrector.add_space_after_operator(new_text, buster)
print(new_text)

if __name__ == "__main__":
    main()


"""
buster = input * new_line_size
custer = input * tab_size
"""