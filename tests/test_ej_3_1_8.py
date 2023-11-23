from src.ej_3_1_8 import es_palidromo
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("Hola", False),
    ("ama", True),
    ("oso", True),
    ("Hello", False)
    ]
)
def test(input_n1, expected):
    assert es_palidromo(input_n1) == expected