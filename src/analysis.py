import scipy.stats as stats
import matplotlib.pyplot as plt


def plot_temperature_trends(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['TempMax_C'], label='Max Temp (°C)', color='red', alpha=0.7)
    plt.plot(df['Date'], df['TempMin_C'], label='Min Temp (°C)', color='blue', alpha=0.7)
    plt.title('Temperature Trends in Houston (2017)')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.show()


def get_top_windy_days(df):
    top_windy_days = df.nlargest(3, 'AvgWind')[['Date', 'AvgWind']]
    return top_windy_days


def calculate_rain_wind_correlation(df):
    rain = df['DailyRain'].to_numpy()
    wind = df['AvgWind'].to_numpy()

    corr, p_val_corr = stats.pearsonr(rain, wind)

    print(f"Pearson Correlation (Rain and Wind): {corr:.3f}")
    return corr, p_val_corr