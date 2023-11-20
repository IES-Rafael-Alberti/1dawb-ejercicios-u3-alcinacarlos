from src.ej_3_1_1 import listar_asignaturas
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (["Mates", "Lengua"], "Mates, Lengua"),
    (["Geografia"], "Geografia"),
    (["Historia"], "Historia"),
    (["Hola"], "Hola")
    ]
)
def test(input_n1, expected):
    assert listar_asignaturas(input_n1) == expected