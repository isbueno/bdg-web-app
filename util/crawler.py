import requests
from model import DNA


def get_data_from_sequencia(database):
    dna1 = DNA(sequencia=str("ATGC"))
    database.session.add(dna1)
    database.session.commit()

    dna2 = DNA(sequencia=str("TACG"))
    database.session.add(dna2)
    database.session.commit()
