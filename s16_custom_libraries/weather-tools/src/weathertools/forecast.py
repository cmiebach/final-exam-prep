"""Weather forecast management."""

from datetime import datetime


class WeatherForecast:
    """Stores daily weather forecasts for a city and provides summary statistics.

    Args:
        city: Name of the city.

    Attributes:
        city: Name of the city.
        days: List of daily forecast dictionaries.
    """

    def __init__(self, city):
        self.city = city
        self.days = []

    def add_day(self, date, high, low, condition="Unknown"):
        """Add a daily forecast.

        Args:
            date: Date string in 'YYYY-MM-DD' format.
            high: High temperature in Celsius.
            low: Low temperature in Celsius.
            condition: Weather condition (e.g., 'Sunny', 'Rainy').
        """
        self.days.append({
            "date": datetime.strptime(date, "%Y-%m-%d"),
            "high": high,
            "low": low,
            "condition": condition,
        })

    def average_high(self):
        """Calculate the average high temperature across all days."""
        if not self.days:
            return 0
        return sum(d["high"] for d in self.days) / len(self.days)

    def average_low(self):
        """Calculate the average low temperature across all days."""
        if not self.days:
            return 0
        return sum(d["low"] for d in self.days) / len(self.days)

    def hottest_day(self):
        """Return the day with the highest temperature."""
        if not self.days:
            return None
        return max(self.days, key=lambda d: d["high"])

    def coldest_day(self):
        """Return the day with the lowest temperature."""
        if not self.days:
            return None
        return min(self.days, key=lambda d: d["low"])

    def summary(self):
        """Return a formatted summary of the forecast."""
        if not self.days:
            return f"No forecast data for {self.city}."

        hottest = self.hottest_day()
        coldest = self.coldest_day()

        lines = [
            f"Weather Forecast for {self.city} ({len(self.days)} days)",
            "=" * 45,
            f"  Average high: {self.average_high():.1f} °C",
            f"  Average low:  {self.average_low():.1f} °C",
            f"  Hottest day:  {hottest['date']:%Y-%m-%d} ({hottest['high']} °C, {hottest['condition']})",
            f"  Coldest day:  {coldest['date']:%Y-%m-%d} ({coldest['low']} °C, {coldest['condition']})",
        ]
        return "\n".join(lines)

    def __repr__(self):
        return f"WeatherForecast('{self.city}', days={len(self.days)})"

    def __str__(self):
        return self.summary()
