mots = ['+','-','*','/',':=', None, None,
        "access", "and", "begin", "else", "elsif", "end",
        "false", "for", "function", "if", "in", "is",
        "loop", "new", "not", "null", "or", "out",
        "procedure", "record", "rem", "return", "reverse", "then",
        "true", "type", "use", "while", "with", ':', '(', ')', ',', ';', '=', '.', "'", '>', '<', None
        ]

with open("rules.gramm", "r") as file:
    data = file.readlines()

    newData = []

    for line in data:
        newLine = line.split(" ")[:2]
        for mot in line.split(" ")[2:]:
            if mot in mots:
                newLine.append(str(mots.index(mot)))
            else:
                newLine.append(mot.rstrip())  # Remove trailing newline character
        print(' '.join(newLine), end="")
