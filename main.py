"""LinterCleanter"""
import sys # vi använder detta för att kunna ta in parameter från när vi kör programmet
import json
import corrector

def main():
    """Om vi har mindre än 2 argument, dvs. bara programnamnet"""
if len(sys.argv) < 2:
    print("Usage: main.py <file> [options]")
    sys.exit(1)

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("Usage: main.py [OPTION] [FILE]")
    print("  -l, --linebreaks\tAdd line breaks to the text")
    print("  -t, --tabs\t\tAdd tabs to the text")
    print("Example: main.py -l text.txt")
    sys.exit(0)

# json config file
json_file = open("config.json", "r", encoding="utf-8").read()
json_data = json.loads(json_file) # läser in json filen och gör om den till en dictionary

# file to edit
file = open(sys.argv[1], "r", encoding="utf-8").read()
new_line_size = json_data["new_line_size"]
tab_size = json_data["tab_size"]
  #github test
  # implementera argv
  #override config file
  #sys.argv[2] = "new_line_size"
  #sys.argv[3] = " new_tab_size"
  #om ingen input normal values från json
  #[4] newlinesize = 4
  #problem:
  #Using PEP8 as standard
new_linesize = json_data["new_lineSize"]
  #kallar på funktionen i corrector.py
new_text = corrector.add_new_lines(file, new_line_size)
new_text = corrector.add_space_after_comment(new_text, tab_size)
new_text = corrector.add_space_after_operator(new_text, new_line_size)
print(new_text)

if __name__ == "__main__":
    main()
