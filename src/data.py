import pandas as pd

def load_raw_train(path):
    """Carga el fichero raw de entrenamiento y devuelve un DataFrame."""
    df = pd.read_csv(path, sep='\s+', header=None)
    return df