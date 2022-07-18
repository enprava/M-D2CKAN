import requests


class Consulta:
    """Clase encargada de hacer una petición a la api del M&D Manager para obtener los Dataflows indicados
    en el fichero configuracion/consultas.yaml. Si no hay ninguno especificado obtendrá todos."""

    def __init__(self, consultas):
        if not consultas['Consultas']:

            requests.get("http://192.168.1.123/sdmx_172/NODE_API/dataflow")

        else:
            lista = []
            for ids in consultas['Consulta']:
                lista.append(
                    requests.get(f'http://192.168.1.123/sdmx_172/NODE_API/dataflow/{ids[0]}/{ids[1]}/{ids[2]}').headers)
