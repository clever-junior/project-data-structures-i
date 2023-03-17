def txt_importer(path_file: str):
    if not path_file.endswith(".txt"):
        raise FileNotFoundError("Formato inválido")

    try:
        with open(path_file) as txt_file:
            lines = txt_file.readlines()

        for line in lines:
            line.replace("\\n", "\n")

        return lines

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {path_file} não encontrado")
