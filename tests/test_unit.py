from cmd import PROMPT
import corrector

def test_add_new_lines():
    """Testar att lägga till nya rader efter . , ; : ? !"""
    text = "Hej jag är en test text, jag ska testa om det funkar att lägga till nya rader i mig. här får du en random siffra 2.7"
    new_text = corrector.add_new_lines(text, 1)
    assert new_text == "Hej jag är en test text,\njag ska testa om det funkar att lägga till nya rader i mig.\nhär får du en random siffra 2.7"

def test_add_space_after_comment():
    """Testar att lägga till ett mellanslag efter %"""
    text = "%jag är en kommentar"
    new_text = corrector.add_space_after_comment(text, 1)
    assert new_text == "% jag är en kommentar"

def test_add_new_line_after_sections():
    """Testar att lägga till nya rader efter \\section"""
    text = "\\section{Jag är en section}"
    new_text = corrector.add_new_line_after_sections(text, 1)
    assert new_text == "\\section{Jag är en section}\n\n"

def test_add_new_line_after_chapter():
    """Testar att lägga till nya rader efter \\chapter"""
    text = "\\chapter{Jag är en chapter}"
    new_text = corrector.add_new_line_after_chapter(text, 1)
    assert new_text == "\\chapter{Jag är en chapter}\n\n"

def test_add_tabs_between_env_blocks():
    """Testar att lägga till tabbar mellan \\begin{[env]}"""
    text = "\\begin{itemize}\n\\item Jag är en item\n\\end{itemize}"
    new_text = corrector.add_tabs_between_env_blocks(text, 1)
    assert new_text == "\\begin{itemize}\n \\item Jag är en item\n\\end{itemize}\n"

def test_add_tabs_between_env_blocks_document():
    """Testar att lägga till tabbar mellan \\begin{document}"""
    text = "\\begin{document}\nhello world\\end{document}"
    new_text = corrector.add_tabs_between_env_blocks(text, 1)
    assert new_text == "\\begin{document}\nhello world\\end{document}\n"