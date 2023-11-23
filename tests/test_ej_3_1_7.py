from src.ej_3_1_7 import eliminar_multiplos_3
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], ['A', 'B', 'D', 'E', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'S', 'T', 'V', 'W', 'Y', 'Z'])
    ]
)
def test(input_n1, expected):
    assert eliminar_multiplos_3(input_n1) == expected