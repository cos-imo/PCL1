class data_exporter:
    def __init__(self):
        pass

    def create_dump_file(self, tokens, dump_mode):
        with open("dump_file", "w+") as file:
            for token in tokens:
                file.write(str(token))
