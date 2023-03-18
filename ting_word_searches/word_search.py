from ting_file_management.file_process import process
from ting_file_management.queue import Queue


queue = Queue()
process("statics/nome_pedro.txt", queue)


def exists_word(word, instance):
    result = list()

    for item in instance.data:
        word_ocurrencies = list()

        for line in item["linhas_do_arquivo"]:
            if line.lower().find(word) != -1:
                index = item["linhas_do_arquivo"].index(line)
                word_ocurrencies.append({"linha": index + 1})

        if word_ocurrencies:
            result.append(
                {
                    "palavra": word,
                    "arquivo": item["nome_do_arquivo"],
                    "ocorrencias": word_ocurrencies,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
