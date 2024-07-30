import pandas as pd
import random

def shuffle_csv(input_file, output_file):
    # Leggi il file CSV
    df = pd.read_csv(input_file)
    
    # Estrai la prima riga (intestazione)
    header = df.iloc[0]
    
    # Estrai il resto delle righe
    rows = df.iloc[1:]
    
    # Mescola le righe in modo casuale
    shuffled_rows = rows.sample(frac=1).reset_index(drop=True)
    
    # Ricostruisci il DataFrame con l'intestazione
    shuffled_df = pd.concat([header.to_frame().T, shuffled_rows]).reset_index(drop=True)
    
    # Salva il nuovo DataFrame in un file CSV
    shuffled_df.to_csv(output_file, index=False)

# Esempio di utilizzo
input_file = 'test_unwanted_activities.csv'  # Nome del file di input
output_file = 'shuffled_test_unwanted_activities.csv'  # Nome del file di output

shuffle_csv(input_file, output_file)
