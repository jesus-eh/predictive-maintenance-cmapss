import pandas as pd

def load_cmapss_train(path):
    col_names = ['unit', 'time', 'op1', 'op2', 'op3'] + [f'sensor_{i}' for i in range(1, 22)]
    df = pd.read_csv(path, sep=r"\s+", header=None, names=col_names)
    return df

def filter_motor_data(df, motor_id):
    return df[df['unit'] == motor_id]
