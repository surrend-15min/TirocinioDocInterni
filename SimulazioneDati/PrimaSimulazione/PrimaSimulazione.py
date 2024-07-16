import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Definizione dei cicli di attività
activity_cycles = [
    ['Receive Goods', 'Quality Check', 'Store in Warehouse'],
    ['Receive Goods', 'Quality Check', 'Store in Warehouse', 'Pick for Order', 'Order Cancellation'],
    ['Receive Goods', 'Quality Check', 'Store in Warehouse', 'Pick for Order', 'Receive Payment', 'Pack for Shipment', 'Ship to Customer', 'Customer Receive Goods'],
    ['Receive Goods', 'Quality Check', 'Store in Warehouse', 'Pick for Order', 'Receive Payment', 'Pack for Shipment', 'Ship to Customer', 'Customer Receive Goods', 'Customer Feedback'],
    ['Receive Goods', 'Quality Check', 'Store in Warehouse', 'Pick for Order', 'Receive Payment', 'Pack for Shipment', 'Ship to Customer', 'Customer Receive Goods', 'Customer Feedback', 'Return Processing']
]

# Funzione per generare una data casuale all'interno di un intervallo
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

# Generazione dei dati simulati
num_records = 1000
data = []

# Intervallo di date per la generazione dei timestamp
start_date = datetime.now() - timedelta(days=365)
end_date = datetime.now()

# Creazione di un dizionario per tracciare l'ultimo timestamp per ogni prodotto
product_last_timestamp = {}

# Creazione del dataset coerente
for product_id in range(1, 101):  # Assumiamo 100 ID di prodotti unici
    cycle = random.choice(activity_cycles)
    
    for activity_id, activity in enumerate(cycle, start=1):
        if product_id in product_last_timestamp:
            start = product_last_timestamp[product_id]
        else:
            start = start_date

        timestamp = random_date(start, end_date)
        product_last_timestamp[product_id] = timestamp
        data.append([activity_id, activity, timestamp, product_id])

# Creazione del DataFrame
df = pd.DataFrame(data, columns=['activity_id', 'activity', 'timestamp', 'product_id'])

# Ordinamento del DataFrame per prodotto e timestamp
df = df.sort_values(by=['product_id', 'timestamp'])

# Salvataggio in un file CSV
df.to_csv('activity_log.csv', index=False)

print("Dati simulati salvati in 'activity_log.csv'.")
