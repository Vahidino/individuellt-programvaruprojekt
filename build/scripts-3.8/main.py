import argparse
import json
import corrector as corrector

def main():
  parser = argparse.ArgumentParser(prog='myprogram',
  description='Lintercleanter.', add_help=False)

  parser.add_argument('file', type=str, help='File to be corrected')
  parser.add_argument('-l', "--linebreaks", type=int, help='Number of linebreaks')
  parser.add_argument('-t', "--tabs", type=int, help='Number of tabs')
  parser.add_argument('-o', "--output", type=str, help='Output file')
  parser.add_argument('-h', "--help", action='help', help='Help')

  arg = parser.parse_args()

  config_path = __file__

  config_path = config_path.replace("main.py", "config.json")

  # Get config from JSON
  json_file = open(config_path, "r", encoding="utf-8").read()
  json_data = json.loads(json_file)

  new_line_size = json_data["new_line_size"]
  tab_size = json_data["tab_size"]

  file_dir = arg.file

  output_file = file_dir.split('.')[0] + '_corrected.' + file_dir.split('.')[1]

  if arg.output:
    output_file = arg.output

  file = open(file_dir, "r", encoding="utf-8").read()

  #override config file
  if arg.linebreaks:
    new_line_size = arg.linebreaks
  if arg.tabs:
    tab_size = arg.tabs

  new_text = corrector.add_new_lines(file, new_line_size)
  new_text = corrector.add_space_after_comment(new_text, tab_size)
  new_text = corrector.add_new_line_after_sections(new_text, new_line_size)
  new_text = corrector.add_new_line_after_chapter(new_text, new_line_size)
  new_text = corrector.add_tabs_between_env_blocks(new_text, tab_size)

  with open(output_file, 'w') as f:
    f.write(new_text)