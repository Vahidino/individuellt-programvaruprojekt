import argparse
import json
import corrector as corrector

def main():
  parser = argparse.ArgumentParser(prog='myprogram',
  description='Lintercleanter.', add_help=False) # add_help=False to remove the default help option from argparse and makes stnadard argument
  
  # the used arguments
  parser.add_argument('file', type=str, help='File to be corrected')
  parser.add_argument('-l', "--linebreaks", type=int, help='Number of linebreaks')
  parser.add_argument('-t', "--tabs", type=int, help='Number of tabs')
  parser.add_argument('-o', "--output", type=str, help='Output file')
  parser.add_argument('-h', "--help", action='help', help='Help')

  arg = parser.parse_args() #HÄMTAR ARGUMENTEN

  config_path = __file__ # variablen för cnfig path 

  config_path = config_path.replace("main.py", "config.json") # byter ut main.py med config.json

  # Get config from JSON
  json_file = open(config_path, "r", encoding="utf-8").read()
  json_data = json.loads(json_file)

  new_line_size = json_data["new_line_size"]
  tab_size = json_data["tab_size"]

  file_dir = arg.file #hämtar texten

  output_file = file_dir.split('.')[0] + '_corrected.' + file_dir.split('.')[1] # byter ut output filnamnet med _corrected

  if arg.output:
    output_file = arg.output # om output är satt så ändras outputfilen till det som är satt

  file = open(file_dir, "r", encoding="utf-8").read() # öppnar filen

  #override config file
  if arg.linebreaks:
    new_line_size = arg.linebreaks # om linebreaks är satt så ändras new_line_size till det som är satt
  if arg.tabs:
    tab_size = arg.tabs   # om tabs är satt så ändras tab_size till det som är satt

  new_text = corrector.add_new_lines(file, new_line_size)
  new_text = corrector.add_space_after_comment(new_text, tab_size)
  new_text = corrector.add_new_line_after_sections(new_text, new_line_size)
  new_text = corrector.add_new_line_after_chapter(new_text, new_line_size)
  new_text = corrector.add_tabs_between_env_blocks(new_text, tab_size)

  with open(output_file, 'w') as f: # skriver till outputfilen
    f.write(new_text)