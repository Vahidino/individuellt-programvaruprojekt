from cgitb import text
import sys # vi använder detta för att kunna ta in parameter från när vi kör programmet
import json
import corrector

def main():

  if len(sys.argv) < 2: # Om vi har mindre än 2 argument, dvs. bara programnamnet
    print("Usage: main.py <file> [options]")
    sys.exit(1)

  if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("Usage: main.py [OPTION] [FILE]")
    print("  -l, --linebreaks\tAdd line breaks to the text")
    print("  -t, --tabs\t\tAdd tabs to the text")
    print("Example: main.py -l text.txt")
    sys.exit(0)

  # json config file
  jsonFile = open("config.json", "r").read()
  jsonData = json.loads(jsonFile)

 # file to edit
  file = open(sys.argv[1], "r").read()

  newText = corrector.addNewLines(file)
  newText = corrector.addSpaceAfterComment(newText)
  newText = corrector.addSpaceAfterOperator(newText)
  print(newText)

if __name__ == "__main__":
  main()