from mrjob.job import MRJob

class PromedioActas(MRJob):

    def mapper(self, _, linea):
        partes = linea.strip().split(',')
        if len(partes) == 3:
            candidato = partes[0]
            votos = int(partes[2])
            yield candidato, (votos, 1)

    def reducer(self, candidato, valores_tuplas):
        suma_total = 0
        cantidad_mesas = 0

        for votos, un_acta in valores_tuplas:
            suma_total += votos
            cantidad_mesas += un_acta

        promedio = suma_total / cantidad_mesas
        yield candidato, round(promedio, 2)

if __name__ == '__main__':
    PromedioActas.run()
