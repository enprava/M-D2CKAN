import requests


class Consulta:
    """Clase encargada de hacer una petición a la api del M&D Manager para obtener los Dataflows indicados
    en el fichero configuracion/consultas.yaml. Si no hay ninguno especificado obtendrá todos."""

    def __init__(self, consultas):
        if not consultas['Consultas']:

            peticion = requests.get("http://192.168.1.123/sdmx_172/NODE_API/dataflow")

        else:
            list = []
            for id in consultas['Consulta']:
                list.append(
                    requests.get("http://192.168.1.123/sdmx_172/NODE_API/dataflow/{}/{}/{}".format(id[0], id[1]),
                                 id[2]))