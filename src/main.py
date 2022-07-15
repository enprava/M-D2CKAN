import yaml

from src.mdm.consulta import Consulta

if __name__ == '__main__':
    consultas = open("configuracion/consultas.yaml", "r", encoding="utf-8")
    consultas = yaml.safe_load(consultas)
    consulta = Consulta(consultas)