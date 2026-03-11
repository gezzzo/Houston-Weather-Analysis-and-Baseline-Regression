from src.preprocess import load_data, convert_temperature_columns
from src.analysis import plot_temperature_trends, get_top_windy_days, calculate_rain_wind_correlation
from src.modeling import fit_linear_regression, plot_regression


def main():
    df = load_data("data/houston_2017.xlsx")
    df = convert_temperature_columns(df)

    top_windy_days = get_top_windy_days(df)
    corr, p_val_corr = calculate_rain_wind_correlation(df)

    slope, intercept, r_value, p_value, std_err = fit_linear_regression(df)

    print("Top 3 windiest days:")
    print(top_windy_days)
    print()

    print("Rain/Wind Pearson correlation:")
    print((corr, p_val_corr))
    print()

    print("Regression info:")
    print((slope, intercept, r_value, p_value, std_err))

    plot_temperature_trends(df)
    plot_regression(df, slope, intercept, r_value)


if __name__ == "__main__":
    main()