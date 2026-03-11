# Houston Weather Analysis (2017)

A compact weather data analysis project for Houston using daily observations from 2017.

## Overview

This notebook explores daily weather patterns and basic relationships between rainfall, wind speed, and temperature.

Main tasks in the analysis:
- Load and inspect daily Houston weather data from Excel.
- Convert `TempMin` and `TempMax` from Fahrenheit to Celsius using NumPy vectorization.
- Visualize yearly min/max temperature trends.
- Identify the top 3 windiest days.
- Measure Pearson correlation between daily rain and average wind.
- Fit a simple linear regression (`TempMin_C` -> `TempMax_C`).

## Dataset

File: `houston_2017.xlsx`

- Rows: 365 (one full year)
- Date range: 2017-01-01 to 2017-12-31
- Columns:
  - `Station`
  - `Name`
  - `Date`
  - `Month`
  - `DailyRain`
  - `AvgWind`
  - `TempMin`
  - `TempMax`

## Key Results

- Pearson correlation (`DailyRain` vs `AvgWind`): `0.222`
  - Interpretation: weak positive relationship.
- Linear regression R-squared (`TempMin_C` predicting `TempMax_C`): `0.753`
- Regression slope: `0.783`
- Top 3 windiest days:
  - 2017-08-28: 23.49
  - 2017-08-29: 21.70
  - 2017-04-29: 18.57

## Repository Structure

```
├── main.py                  # Entry point script
├── README.md                # Project documentation
├── data/
│   └── houston_2017.xlsx    # Input dataset
├── figures/
│   ├── Linear-Regression.png
│   └── Temperature-Trends-in-Houston.png
├── notebooks/
│   └── houston_analysing.ipynb  # Complete notebook analysis
└── src/
    ├── preprocess.py        # Data loading & Fahrenheit→Celsius conversion
    ├── analysis.py          # Correlation, windiest days analysis
    └── modeling.py          # Linear regression modeling
```

## Run Locally

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install numpy pandas scipy matplotlib jupyter openpyxl
```

3. Launch Jupyter:

```bash
jupyter notebook houston_analysing.ipynb
```

## Notes

- Temperatures are converted in-notebook from Fahrenheit to Celsius.
- The project focuses on exploratory analysis and simple baseline statistical modeling.
