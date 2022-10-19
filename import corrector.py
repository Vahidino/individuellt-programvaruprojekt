import corrector

def test_add_new_lines():
    text = "Hej.Jag heter John. Jag är 25 år.\nJag gillar att spela fotboll."
    buster = 1
    expected = "Hej.\n Jag heter John.\n Jag är 2.5 år.\n Jag gillar att spela fotboll."
    actual = corrector.add_new_lines(text, buster)
    assert actual == expected

def test_add_space_after_comment():
    text = "%hej this is a comment"
    custer = 1
    expected = "% hej this is a comment"
    actual = corrector.add_space_after_comment(text, custer)
    assert actual == expected

def test_add_space_after_operator():
    text = "\\begin{document}\nhello world\n\\end{document}"
    buster = 1
    expected = "\\begin{document}\n\nhello world\n\\end{document}"
    actual = corrector.add_space_after_operator(text, buster)
    assert actual == expected