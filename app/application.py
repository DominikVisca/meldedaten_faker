from faker import Faker
import datetime
import random
import overpy
import pandas as pandas

def generate():
    records = 10000

    api = overpy.Overpass()
    response = api.query("""[out:json][timeout:200];
    (
    way(poly:"50.666582972805926 8.305402116810889 
        50.67057130716934 8.32040906983932 
        50.694230917799743 8.321625849814598 
        50.696596878862785 8.310066440049455 
        50.695008305006169 8.305875309023497 
        50.694298516687255 8.305537314585921 
        50.692929639215066 8.303644545735487 
        50.691172068139664 8.302715061032151 
        50.686964037391832 8.298743626390618 
        50.686119051297887 8.298050737793584 
        50.684581176606919 8.289448779357244 
        50.682772906365884 8.286356130253411 
        50.681082934177994 8.285156250000012 
        50.677314296199008 8.284023968634129 
        50.673883652657594 8.284040868356007 
        50.671095198547576 8.285832238875166 
        50.667258961681078 8.302478464925846 
        50.667258961681078 8.302478464925846 
        50.666582972805926 8.305402116810889")[building]["addr:street"];
    );out meta;>;out meta qt;""")

    table = []

    for way in response.ways:
        table.append(generate_single_record(way))

    for i in range(records-len(table)):
        random_way = random.choice(response.ways)
        table.append(generate_single_record(random_way))

    data_frame = pandas.DataFrame(table)
    data_frame.to_csv("fake_meldedaten.csv", header=["Geburtsjahr", "Geschlecht", "Strasse", "Hausnummer", "PLZ", "Ort"], index=False)

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