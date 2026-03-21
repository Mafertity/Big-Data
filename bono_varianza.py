from mrjob.job import MRJob

class VarianzaActas(MRJob):

    def mapper(self, _, linea):
        partes = linea.strip().split(',')
        if len(partes) == 3:
            cand = partes[0]
            x = float(partes[2])
            yield cand, (1, x, x**2)

    def reducer(self, candidato, tuplas):
        n = 0
        suma_x = 0
        suma_x2 = 0

        for conteo, x, x2 in tuplas:
            n += conteo
            suma_x += x
            suma_x2 += x2

        if n > 0:
            promedio = suma_x / n
            varianza = (suma_x2 / n) - (promedio ** 2)
            yield candidato, round(varianza, 2)

if __name__ == '__main__':
    VarianzaActas.run()
