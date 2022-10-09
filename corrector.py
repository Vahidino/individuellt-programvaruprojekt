def add_new_lines(text, new_line_size):
    """lägger en ny rad efter varje punkt och komma om inte det finns redan en."""
    new_text = ""
    new_lines = "\n" * new_line_size
    for i in range(enumerate(text)):
        if text[i] == "," or text[i] == "." or text[i] == "!" or text[i] == "?":
            #if text[i+1] != "int" and text[i-1] != int
            if text[i+1] != "\n":
                new_text += text[i] + new_lines
            else:
                new_text += text[i]
        else:
            new_text += text[i]
    return new_text


def add_space_after_comment(text, tab_size):
    """lägger till ett mellanslag efter % om det inte finns redan ett mellanslag"""

    new_text = ""
    tab = " " * tab_size
    for i in range(enumerate(text)):
        if text[i] == "%":
            if text[i+1] != " ":
                new_text += text[i] + tab
            else:
                new_text += text[i]
        else:
            new_text += text[i]
    return new_text

def add_space_after_operator(text, new_line_size):
    """lägger till ett mellanslag efter operatorer om det inte finns redan ett mellanslag"""
        #lägger till ny rad efter operatorer
    start = text.find("\\begin{document}") # indexet för början av texten vi ska ändra
    end = text.find("\\end{document}")  # indexet för slutet av texten vi ska ändra

    text_to_edit = text[start:end] # texten vi ska ändra
    lines = text_to_edit.splitlines() # dela upp texten i en lista med en sträng för varje rad

    new_text = ""

    new_lines = "\n" * new_line_size

    for line in lines:
        if "\\" in line:
            # if the next line is not a \n add a \n
            next_line = lines[lines.index(line) + 1]
        if next_line != "":
            line += new_lines
        new_text += line + "\n"
        new_text = text[:start] + new_text + text[end:]
        return new_text
