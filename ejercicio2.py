from mrjob.job import MRJob

class EscrutinioLimpio(MRJob):

    def mapper(self, _, linea):
        voto = linea.strip()
        candidatos_oficiales = ['Cepeda', 'Paloma', 'Fajardo', 'Abelardo']

        if voto in candidatos_oficiales:
            yield voto, 1

    def reducer(self, candidato, conteos):
        yield candidato, sum(conteos)

if __name__ == '__main__':
    EscrutinioLimpio.run()
