import re
def extract_code_blocks(text):
    """
    Extrahiert Codeblöcke aus dem Text.
    """
    code_blocks = re.findall(r'```([\s\S]*?)```', text)
    return code_blocks