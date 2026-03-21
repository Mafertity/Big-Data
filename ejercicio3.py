from mrjob.job import MRJob

class EscrutinioEficiente(MRJob):

    def mapper(self, _, linea):
        voto = linea.strip()
        if voto in ['Cepeda', 'Paloma', 'Fajardo', 'Abelardo']:
            yield voto, 1

    def combiner(self, candidato, conteos_locales):
        yield candidato, sum(conteos_locales)

    def reducer(self, candidato, conteos_totales):
        yield candidato, sum(conteos_totales)

if __name__ == '__main__':
    EscrutinioEficiente.run()
