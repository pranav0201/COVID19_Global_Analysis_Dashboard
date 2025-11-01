import pandas as pd

# Load latest COVID-19 dataset from Our World in Data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
covid_data = pd.read_csv(url)

# Select relevant columns for the Power BI dashboard
covid_data = covid_data[['location', 'date', 'total_cases', 'total_deaths', 'total_vaccinations', 'population']]

# Clean and rename columns
covid_data.columns = ['Country', 'Date', 'Total Cases', 'Total Deaths', 'Total Vaccinations', 'Population']

# Save to CSV file for Power BI
covid_data.to_csv('covid_data.csv', index=False)

print("✅ Data successfully saved as covid_data.csv")
