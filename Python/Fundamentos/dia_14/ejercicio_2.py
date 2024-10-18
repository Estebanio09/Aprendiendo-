from typing import Counter
from countries_data import countries

"""
Usa el archivo countries_data.py y realiza las siguientes tareas:
Ordena los países por nombre, capital y población.
Ordena los diez idiomas más hablados por ubicación.
Ordena los diez países más poblados.
"""


def data(_list):
    filtered_data = list(
        map(
            lambda x: {
                "name": x["name"],
                "capital": x["capital"],
                "population": x["population"],
            },
            _list,
        )
    )

    # Ordenar por nombre
    sorted_by_name = sorted(filtered_data, key=lambda x: x["name"])
    # Ordenar por capital
    sorted_by_capital = sorted(filtered_data, key=lambda x: x["capital"])
    # Ordenar por población
    sorted_by_population = sorted(
        filtered_data, key=lambda x: x["population"], reverse=True
    )

    return {
        "sorted_by_name": sorted_by_name,
        "sorted_by_capital": sorted_by_capital,
        "sorted_by_population": sorted_by_population,
    }


result = data(countries)
# print(result["sorted_by_name"])


def get_top_10_languages(countries):
    languages = []
    for country in countries:
        languages.extend(country["languages"])

    languages_counts = Counter(languages)
    sorted_languages = languages_counts.most_common(10)
    return sorted_languages


get_top_10_languages(countries)
