file = open("brouillon_ZHOU/exemple_ada_sujet", "r")

table_idf = []

keywords = ['+','-','*','/',':=', None, None,
                "access", "and", "begin", "else", "elsif", "end",
                "false", "for", "function", "if", "in", "is",
                "loop", "new", "not", "null", "or", "out",
                "procedure", "record", "rem", "return", "reverse", "then",
                "true", "type", "use", "while", "with", ':', '(', ')', ',', ';', '=', '.', "'"]

def tokeniser_ada(code):
    lignes_a_tokeniser = []
    tokens = []
    for line in file:
        lignes_a_tokeniser.append(line)

    ##lignes à tokeniser

    for ligne in lignes_a_tokeniser:
        

    in_string = False

    for char in code:
        if char == '"':
            in_string = not in_string
            current_token += char
        elif char.isspace() and not in_string:
            if current_token:
                if current_token in keywords:
                    table_idf.append(('KEYWORD', current_token))
                elif re.match(r'^\d+$', current_token):
                    table_idf.append(('INTEGER', int(current_token)))
                elif re.match(r'^\d+\.\d+$', current_token):
                    table_idf.append(('FLOAT', float(current_token)))
                else:
                    table_idf.append(('IDENTIFIER', current_token))
            current_token = ''
        else:
            current_token += char

    return table_idf


table_idf = tokeniser_ada(file)
for token in tokens:
    print(token)
