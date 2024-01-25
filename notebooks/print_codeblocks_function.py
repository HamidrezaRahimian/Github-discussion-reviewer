def print_code_blocks(code_blocks):
    """
    Gibt die Liste der Codeblöcke in schöner Form aus.
    """
    print("Gefundene Codeblöcke:")
    for i, code_block in enumerate(code_blocks, start=1):
        print(f'Codeblock {i}:\n{code_block}\n{"-" * 30}')