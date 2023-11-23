from src.ej_3_1_9 import contar_veces
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("Hola", (['a', 1], ['e', 0], ['i', 0], ['o', 1], ['u', 0])),
    ("ama", (['a', 2], ['e', 0], ['i', 0], ['o', 0], ['u', 0])),
    ("oso", (['a', 0], ['e', 0], ['i', 0], ['o', 2], ['u', 0])),
    ("Hello", (['a', 0], ['e', 1], ['i', 0], ['o', 1], ['u', 0]))
    ]
)
def test(input_n1, expected):
    assert contar_veces(input_n1) == expected