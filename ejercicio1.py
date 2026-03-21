from mrjob.job import MRJob

class EscrutinioNacional(MRJob):

    def mapper(self, _, linea):
        voto = linea.strip()
        yield voto, 1

    def reducer(self, candidato, conteos):
        total = sum(conteos)
        yield candidato, total

if __name__ == '__main__':
    EscrutinioNacional.run()
