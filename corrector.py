def addNewLines(text):
    """Add new lines to text after , and . if there is not already a new line"""
    newText = ""
    for i in range(len(text)):
        if text[i] == "," or text[i] == ".":
            if text[i+1] != "\n":
                newText += text[i] + "\n"
            else:
                newText += text[i]
        else:
            newText += text[i]
    return newText


def addSpaceAfterComment(text):
    """Add a space after % if there is no space"""
    newText = ""
    for i in range(len(text)):
        if text[i] == "%":
            if text[i+1] != " ":
                newText += text[i] + " "
            else:
                newText += text[i]
        else:
            newText += text[i]
    return newText


def addSpaceAfterOperator(text):
    """Add new line after operators if there is no new line allready"""

    start = text.find("\\begin{document}") # indexet för början av texten vi ska ändra
    end = text.find("\\end{document}")  # indexet för slutet av texten vi ska ändra

    textToEdit = text[start:end] # texten vi ska ändra
    lines = textToEdit.splitlines() # dela upp texten i en lista med en sträng för varje rad

    newText = ""

    for line in lines:
        if "\\" in line:
            # if the next line is not a \n add a \n
            nextLine = lines[lines.index(line) + 1]
            if nextLine != "":
                line += "\n"
        newText += line + "\n"
    
    newText = text[:start] + newText + text[end:]
    return newText
    