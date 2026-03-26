# weathertools

A simple weather utilities library built as a learning exercise in PDA2.

## Features

- **Temperature conversion**: Celsius, Fahrenheit, Kelvin
- **Weather forecasts**: Store daily forecasts and compute statistics

## Installation

```bash
pip install -e .
```

## Usage

```python
from weathertools import celsius_to_fahrenheit, WeatherForecast

# Convert temperatures
print(celsius_to_fahrenheit(25))  # 77.0

# Work with forecasts
forecast = WeatherForecast("Madrid")
forecast.add_day("2026-02-23", high=12, low=4, condition="Cloudy")
forecast.add_day("2026-02-24", high=15, low=6, condition="Sunny")
print(forecast.summary())
```
