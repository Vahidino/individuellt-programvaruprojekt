def addNewLines(text, newLineSize):
    """lägger en ny rad efter varje punkt och komma om inte det finns redan en."""
    
    newText = ""
    newLines = "\n" * newLineSize
    
    for i in range(len(text)):
        if text[i] == "," or text[i] == "." or text[i] == "!" or text[i] == "?":
            """if text[i] == "." is between two numbers dont ad \n
               if text[i+1] != "int" and text[i-1] != int             
            """
            if text[i+1] != "\n":
                newText += text[i] + newLines
            else:
                newText += text[i]
        else:
            newText += text[i]
    return newText


def addSpaceAfterComment(text, tabSize):
    """lägger till ett mellanslag efter % om det inte finns redan ett mellanslag"""

    newText = ""
    tab = " " * tabSize
    for i in range(len(text)):
        if text[i] == "%":
            if text[i+1] != " ":
                newText += text[i] + tab
            else:
                newText += text[i]
        else:
            newText += text[i]
    return newText

"""
coding guidelines
"""
def addSpaceAfterOperator(text, newLineSize):
        #Add new line after operators if there is no new line allready
        start = text.find("\\begin{document}") # indexet för början av texten vi ska ändra
        end = text.find("\\end{document}")  # indexet för slutet av texten vi ska ändra

        textToEdit = text[start:end] # texten vi ska ändra
        lines = textToEdit.splitlines() # dela upp texten i en lista med en sträng för varje rad

        newText = ""

        newLines = "\n" * newLineSize

        for line in lines:
            if "\\" in line:
            # if the next line is not a \n add a \n
                nextLine = lines[lines.index(line) + 1]
            if nextLine != "":
                line += newLines
        newText += line + "\n"
    
        newText = text[:start] + newText + text[end:]
        return newText

    