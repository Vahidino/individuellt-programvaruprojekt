#pylint: disable=consider-using-enumerate
import sys
import json


def add_new_lines(text, buster):
    """lägger en ny rad efter varje punkt och komma om inte det finns redan en."""
    new_text = ""
    new_lines = "\n" * buster
    for i in range(len(text)):
        if text[i] == "," or text[i] == "." or text[i] == "!" or text[i] == "?":
            if i+1 < len(text) and text[i+1] != "\n":
                # check if the element before and after is a number
                if i-1 > 0 and i+1 < len(text) and text[i-1].isdigit() and text[i+1].isdigit():
                    new_text += text[i]
                else:
                    new_text += text[i] + new_lines
            else:
                new_text += text[i]
        else:
            new_text += text[i]

    new_text = new_text.replace("\n ", "\n")

    return new_text


def add_space_after_comment(text, custer):
    """lägger till ett mellanslag efter % om det inte finns redan ett mellanslag"""

    new_text = ""
    tab = " " * custer
    for i in range(len(text)):
        if text[i] == "%":
            if text[i+1] != " ":
                new_text += text[i] + tab
            else:
                new_text += text[i]
        else:
            new_text += text[i]
    return new_text


def add_new_line_after_sections(text, amountNewLine=1):
    """Lägger nya rader efter \section blocket"""
    new_text = ""
    new_lines = "\n" * (amountNewLine + 1)
    
    lines = text.split("\n")

    for i in range(len(lines)):
        if "\\section" in lines[i]:
            new_text += lines[i] + new_lines
        else:
            new_text += lines[i] + "\n"
    return new_text

def add_new_line_after_chapter(text, amountNewLine=1):
    """Lägger nya rader efter \chapter blocket"""
    new_text = ""
    new_lines = "\n" * (amountNewLine + 1)
    
    lines = text.split("\n")

    for i in range(len(lines)):
        if "\\chapter" in lines[i]:
            new_text += lines[i] + new_lines
        else:
            new_text += lines[i] + "\n"
    return new_text

def add_tabs_between_env_blocks(text, tab_size = 1):
    """Lägger till tabbar mellan \begin{[env]} och \end{[env]} men inte i \begin{document} och \end{document}"""

    new_text = ""
    tab = " " * tab_size
    lines = text.split("\n")

    add_tabs = False

    for i in range(len(lines)):
        if "\\begin{" in lines[i] and "\\begin{document}" not in lines[i] and not add_tabs:
            add_tabs = True
            new_text += lines[i] + "\n"
            continue
        if "\\end{" in lines[i] and "\\end{document}" not in lines[i]:
            add_tabs = False
        
        if add_tabs:
            new_text += tab + lines[i] + "\n"
        else:   
            new_text += lines[i] + "\n"


    return new_text