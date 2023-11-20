from src.ej_3_1_2 import listar_asignaturas
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (["Mates", "Lengua"], "Yo estudio Mates\nYo estudio Lengua\n"),
    (["Geografia"], "Yo estudio Geografia\n"),
    (["Historia"], "Yo estudio Historia\n"),
    (["Hola"], "Yo estudio Hola\n")
    ]
)
def test(input_n1, expected):
    assert listar_asignaturas(input_n1) == expected