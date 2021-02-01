import pandas as pd
from datetime import datetime
from .models import WcotaBaseNacional


def cleaner(dataset):
    dataset = dataset[~dataset.state.str.contains("TOTAL", na=False)]
    dataset = dataset.sort_values(by='date', ascending=False)
    dataset.reset_index(drop=True, inplace=True)
    return dataset


def catcher():
    url = ("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv")
    dataset = pd.read_csv(url, encoding='utf-8',
                          engine='python', error_bad_lines=False)

    dataset = cleaner(dataset)

    print(dataset.info())

    return dataset


def insert():
    dataset = catcher()
    records = dataset.to_records()

    for record in records:
        wcota = WcotaBaseNacional(
            country=record[1],
            state=record[2],
            city=record[3],
            ibgeid=record[4],
            cod_regiaodesaude=record[5],
            name_regiaodesaude=record[6],
            deaths=record[7],
            totalcases=record[8],
            deaths_per_100k_inhabitants=record[9],
            totalcases_per_100k_inhabitants=record[10],
            deaths_by_totalcases=record[11],
            field_source=record[12],
            date=record[13],
            newcases=record[14],
            newdeaths=record[15],
            last_info_date=record[16],
        )
        print(wcota.city, wcota.cod_regiaodesaude, wcota.date)
        wcota.save()

    return "Wcota Recorded"
