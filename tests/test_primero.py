import yaml

from src.mdm.consulta import Consulta


def test_primero():
    consultas = open("configuracion/consultas.yaml", "r", encoding="utf-8")
    consultas = yaml.safe_load(consultas)
    consulta = Consulta(consultas)
