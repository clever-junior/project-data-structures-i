from re import search
from pytest_dependency import pytest
from ting_file_management.file_management import txt_importer
from ting_file_management.file_process import process
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # inicializando variáveis
    priority_queue = PriorityQueue()
    mock = {
        "nome_do_arquivo": "test1.txt",
        "qtd_linhas": 9,
        "linhas_do_arquivo": ["..."],
    }
    mock1 = {
        "nome_do_arquivo": "test1.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["..."],
    }

    # Test enqueue does nothing
    priority_queue.enqueue(mock)
    assert len(priority_queue) == 1

    # Test inverted search
    priority_queue.enqueue(mock1)
    assert priority_queue.search(0) == mock1

    # Test dequeue does nothing
    given = priority_queue.dequeue()

    assert given == mock1

    # Test inverted priority
    assert priority_queue.is_priority(mock) == False

    # Test no priority
    assert priority_queue.is_priority(mock1) == True

    # Test search should raise index error
    with pytest.raises(IndexError):
        priority_queue.search(7)
