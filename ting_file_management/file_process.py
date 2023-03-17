import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


project = Queue()
path = "statics/arquivo_teste.txt"

def process(path_file: str, instance: Queue):
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

def remove(instance: Queue):
    if not len(instance):
        print("Não há elementos")        
        
    path_file = instance.data[0]["nome_do_arquivo"]  
    
    instance.dequeue()

    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
