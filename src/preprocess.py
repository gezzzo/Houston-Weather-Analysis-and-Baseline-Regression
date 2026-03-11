import pandas as pd
import numpy as np


def load_data(file_path="houston_2017.xlsx"):
    df = pd.read_excel(file_path)
    return df


def convert_temperature_columns(df):
    temp_max_f = df['TempMax'].to_numpy()
    temp_min_f = df['TempMin'].to_numpy()

    temp_max_c = (temp_max_f - 32) * 5 / 9
    temp_min_c = (temp_min_f - 32) * 5 / 9

    df['TempMax_C'] = temp_max_c
    df['TempMin_C'] = temp_min_c

    return df