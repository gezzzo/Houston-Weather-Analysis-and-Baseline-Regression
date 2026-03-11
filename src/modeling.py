import scipy.stats as stats
import matplotlib.pyplot as plt


def fit_linear_regression(df):
    temp_min_c = df['TempMin_C'].to_numpy()
    temp_max_c = df['TempMax_C'].to_numpy()

    slope, intercept, r_value, p_value, std_err = stats.linregress(temp_min_c, temp_max_c)

    print(f"Linear Regression R-squared: {r_value**2:.3f}")
    print(slope, std_err, r_value)

    return slope, intercept, r_value, p_value, std_err


def plot_regression(df, slope, intercept, r_value):
    regression_line = slope * df['TempMin_C'] + intercept

    plt.figure(figsize=(12, 6))
    plt.grid()

    plt.scatter(df['TempMin_C'], df['TempMax_C'], alpha=0.5, label='Actual Data')
    plt.plot(df['TempMin_C'], regression_line, color='red', linewidth=2, label='Regression Line')

    plt.title(f'Linear Regression (R squared={r_value**2:.3f})')
    plt.xlabel('Min Temp (°C)')
    plt.ylabel('Max Temp (°C)')
    plt.legend()

    plt.tight_layout()
    plt.show()