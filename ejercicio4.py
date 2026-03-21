from mrjob.job import MRJob

class MaximoPorCandidato(MRJob):

    def mapper(self, _, linea):
        partes = linea.strip().split(',')
        if len(partes) == 3:
            candidato = partes[0]
            votos = int(partes[2])
            yield candidato, votos

    def reducer(self, candidato, votos_de_todas_las_mesas):
        record = max(votos_de_todas_las_mesas)
        yield candidato, record

if __name__ == '__main__':
    MaximoPorCandidato.run()
