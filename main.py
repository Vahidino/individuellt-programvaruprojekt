from cgitb import text
import sys # vi använder detta för att kunna ta in parameter från när vi kör programmet

while True:
  if len(sys.argv) < 2: # Om vi har mindre än 2 argument, dvs. bara programnamnet
    print("Usage: main.py <file>")
    sys.exit(1)
  
  filePath = sys.argv[1] # vi sparar filnamnet/filvägen i en variabel
  file = open(filePath, "r") 

  finishedRes = ""

  for line in file:
    finishedRes += line # vi Läser in filen och lägger varje rad från filen i en variabel

  # write to file
  file = open(filePath, "w")
  print(finishedRes)
  file.write(finishedRes) # writing to file

def addLineBreaks():
  """
    code for making ned lines
  """
  if  input #if the settings are changed 


  elif no input #if not the settings changed then the normal setting will run
  file = open(filePath, "r")
  text = file.read()
  for } in text:
    if } == " ":
      text.replace(" ", " ")
  file = open(filePath, "w");
  file.write(text);
  file.close();
  pass

def addTabs():
  """
    code for making tabs
  """
  pass

def version():
  """
    output the edited version
  """
  pass

def main():
  
  main.printMenu()
  if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("Usage: main.py [OPTION] [FILE]")
    print("  -l, --linebreaks\tAdd line breaks to the text")
    print("  -t, --tabs\t\tAdd tabs to the text")
    print("  -s, --settings\t\tChange settings")
    print("  -v, --version\t\tPrint the version number")
    print("Example: main.py -l text.txt")
    sys.exit(0)
  choice = input("-->")

  while True:
    if choice == "l":
      addLineBreaks()
    elif choice == "t":
      addTabs()
    elif choice == "0":
      sys.exit()
    elif choice == "s":
      help()
    elif choice == "v":
      version()
    else:
      print("Invalid choice")
    main.printMenu()
    choice = input("-->")

#argparse

if __name__ == "__main__":
  main()