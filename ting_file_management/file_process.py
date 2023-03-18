import sys
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance):
    for element in instance.data:
        if element["nome_do_arquivo"] == path_file:
            return None

    txt_data = txt_importer(path_file)

    report = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_data),
        "linhas_do_arquivo": txt_data,
    }

    instance.enqueue(report)

    print(report)


def remove(instance):
    try:
        path_file = instance.get()["nome_do_arquivo"]

        instance.dequeue()

        print(f"Arquivo {path_file} removido com sucesso")

    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position: int):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
