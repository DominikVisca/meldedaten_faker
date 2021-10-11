from faker import Faker
import datetime
import random
import overpy
import geojson
import pandas as pandas

def generate():
    records = 10000

    api = overpy.Overpass()
    response = api.query(build_query())

    table = []

    for way in response.ways:
        table.append(generate_single_record(way))

    for i in range(records-len(table)):
        random_way = random.choice(response.ways)
        table.append(generate_single_record(random_way))

    data_frame = pandas.DataFrame(table)
    data_frame.to_csv("fake_meldedaten.csv", header=["Geburtsjahr", "Geschlecht", "Strasse", "Hausnummer", "PLZ", "Ort"], index=False)

def build_query():
    prefix = """[out:json][timeout:200];("""
    suffix = """[building]['addr:street'];);out meta;>;out meta qt;"""
    q = """way(poly:'""" + create_poly() + """')"""

    query = prefix + q + suffix
    return query

def create_poly():
    file = open('./test.geojson',)
    data = geojson.load(file)
    coords = []

    # if FeatureCollection
    for row in data.features[0].geometry.coordinates[0]:
        row[0], row[1] = str(row[1]), str(row[0])
        row = " ".join(row)
        coords.append(row)
    
    coords_string = " ".join(coords)
    return coords_string

def generate_single_record(way):
    fake = Faker('de_DE')

    record = []
    record.append(fake.date(pattern="%Y"))
    record.append(random.choice(["w", "m"]))
    record.append(way.tags['addr:street'])
    record.append(way.tags['addr:housenumber']) if 'addr:housenumber' in way.tags else record.append("")
    record.append(way.tags['addr:postcode']) if 'addr:postcode' in way.tags else record.append("")
    record.append(way.tags['addr:city']) if 'addr:city' in way.tags else record.append("")
    return record