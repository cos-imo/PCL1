def create_dump_file(data, dump_type):
    print("dump service started")
    if (dump_type=="token_liste"):
        with open("token_liste_dump", "a") as file:
            for element in data:
                file.write(element)
        print("dump file created")
