from pytest_dependency import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # inicializando variáveis
    priority_queue = PriorityQueue()
    mock = {
        "nome_do_arquivo": "...",
        "qtd_linhas": 9,
        "linhas_do_arquivo": ["..."],
    }
    mock1 = {
        "nome_do_arquivo": "...",
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
    assert not priority_queue.is_priority(mock)

    # Test no priority
    assert priority_queue.is_priority(mock1)

    # Test search should raise index error
    with pytest.raises(IndexError):
        priority_queue.search(7)
