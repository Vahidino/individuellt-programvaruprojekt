#LinterCleanter
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
  jsonData = json.loads(jsonFile) # läser in json filen och gör om den till en dictionary

 # file to edit
  file = open(sys.argv[1], "r").read()
  newLineSize = jsonData["newLineSize"]
  tabSize = jsonData["tabSize"]

  # implementera argv
  """override 
  sys.argv[2] = "new linesize"
  sys.argv[3] = " new tabsize"
  om ingen input normal values från json
  [4] newlinesize = 4
  problem:
  hur ska man ställa inn tabs utan att skriva in linesize?
  Recommend pylint to see errors
  Using PEP8 as standard

  """

  #kallar på funktionen i corrector.py
  newText = corrector.addNewLines(file, newLineSize)
  newText = corrector.addSpaceAfterComment(newText, tabSize)
  #newText = corrector.addSpaceAfterOperator(newText, newLineSize)
  print(newText)

if __name__ == "__main__":
  main()