import pandas as pd

def create_rolling_features(df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    """Ejemplo de medias móviles por columnas numéricas."""
    return df.rolling(window=window).mean()