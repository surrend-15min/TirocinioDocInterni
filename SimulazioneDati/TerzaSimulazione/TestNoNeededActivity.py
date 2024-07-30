import pandas as pd
import random
from datetime import datetime, timedelta

def generate_timestamp(start_time, duration_range):
    if 'minutes' in duration_range:
        duration = random.randint(duration_range['minutes'][0], duration_range['minutes'][1])
        return start_time + timedelta(minutes=duration)
    elif 'days' in duration_range:
        duration = random.randint(duration_range['days'][0], duration_range['days'][1])
        return start_time + timedelta(days=duration)
    else:
        raise ValueError("Durata non valida")
    
def add_activity(data, activity_name, timestamp, product):
    activity_id = product_id
    data.append([activity_id, activity_name, timestamp, product])
    duration_range = activity_durations[activity_name]
    return generate_timestamp(timestamp, duration_range)

def generate_random_start_time(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    random_seconds = random.randrange(86400) # 86400 = numero secondi in un giorno
    random_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return random_date

start_date = datetime(2019, 1, 1)
end_date = datetime(2020, 12, 31)

data = []

product_types = [f"Scarpe tipo {i}" for i in range(1, 31)]

activity_ids = {
    "Conferma ordine": 0,
    "Creazione progetto": 1,
    "Modifica progetto": 2,
    "Ordine fornitore": 3,
    "Arrivo offerta fornitore": 4,
    "Ordine annullato": 5,
    "Ordine sospeso": 6,
    "Conferma ordine fornitore": 7,
    "Ordine arrivato": 8,
    "Creazione movimento di magazzino": 9,
    "Movimento di magazzino": 10,
    "Stampa scheda di produzione": 11,
    "Inizio ciclo di produzione": 12,
    "Termine ordine di produzione": 13,
    "Consegna": 14,
    "Controllo qualità non necessario": 15,
    "Ri-lavorazione non necessaria": 16
}

activity_durations = {
    "Conferma ordine": {'minutes': (5, 15)},
    "Creazione progetto": {'minutes': (15, 30)},
    "Modifica progetto": {'minutes': (10, 20)},
    "Ordine fornitore": {'minutes': (20, 40)},
    "Arrivo offerta fornitore": {'days': (1, 3)},
    "Ordine annullato": {'minutes': (5, 15)},
    "Ordine sospeso": {'minutes': (10, 20)},
    "Conferma ordine fornitore": {'days': (1, 2)},
    "Ordine arrivato": {'days': (2, 5)},
    "Creazione movimento di magazzino": {'minutes': (30, 50)},
    "Movimento di magazzino": {'minutes': (40, 60)},
    "Stampa scheda di produzione": {'minutes': (5, 15)},
    "Inizio ciclo di produzione": {'days': (3, 7)},
    "Termine ordine di produzione": {'days': (5, 10)},
    "Consegna": {'minutes': (15, 30)},
    "Controllo qualità non necessario": {'minutes': (5, 10)},
    "Ri-lavorazione non necessaria": {'days': (1, 20)}
}

def generate_cycle(product_id, start_time):
    product = product_types[product_id % len(product_types)]
    timestamp = start_time

    timestamp = add_activity(data, "Conferma ordine", timestamp, product)

    timestamp = add_activity(data, "Creazione progetto", timestamp, product)

    n = random.randint(1, 5)
    for _ in range(n):
        timestamp = add_activity(data, "Modifica progetto", timestamp, product)
    
    y = random.randint(1, 3)
    for _ in range(y):
        z = random.randint(0, 3)
        for _ in range(z):
            for activity in ["Ordine fornitore", "Arrivo offerta fornitore", "Ordine annullato"]:
                timestamp = add_activity(data, activity, timestamp, product)

        x = random.randint(0, 3)
        for _ in range(x):
            for activity in ["Ordine fornitore", "Arrivo offerta fornitore", "Ordine sospeso"]:
                timestamp = add_activity(data, activity, timestamp, product)
        
        for activity in ["Ordine fornitore", "Arrivo offerta fornitore", "Conferma ordine fornitore", "Ordine arrivato", "Creazione movimento di magazzino", "Movimento di magazzino"]:
            timestamp = add_activity(data, activity, timestamp, product)

    timestamp = add_activity(data, "Stampa scheda di produzione", timestamp, product)

    timestamp = add_activity(data, "Inizio ciclo di produzione", timestamp, product)

    # Aggiunta di attività non necessarie in modo casuale
    if random.random() < 0.2:  # 20% di probabilità di aggiungere un controllo qualità non necessario
        timestamp = add_activity(data, "Controllo qualità non necessario", timestamp, product)
    if random.random() < 0.1:  # 10% di probabilità di aggiungere una ri-lavorazione non necessaria
        timestamp = add_activity(data, "Ri-lavorazione non necessaria", timestamp, product)

    timestamp = add_activity(data, "Termine ordine di produzione", timestamp, product)

    timestamp = add_activity(data, "Consegna", timestamp, product)

    return timestamp

min_products = 300
max_products = 500
num_products = random.randint(min_products, max_products)

product_id = 1

while len(data) < 2000 or product_id <= num_products:
    initial_start_time = generate_random_start_time(start_date, end_date)
    initial_start_time = generate_cycle(product_id, initial_start_time)
    product_id += 1

df = pd.DataFrame(data, columns=["ID attività", "Nome attività", "Timestamp attività", "Prodotto"])

df.to_csv("test_unwanted_activities.csv", index=False)

print("File CSV creato con successo. Numero di righe:", len(df))
