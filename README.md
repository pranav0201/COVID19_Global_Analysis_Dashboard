# 🌍 COVID-19 Global Analysis Dashboard (Power BI)

This project presents an interactive Power BI Dashboard that visualizes key insights from the global COVID-19 dataset including total cases, deaths, vaccination trends, and country-level comparisons.  
The data is sourced directly from (https://ourworldindata.org/coronavirus), ensuring it stays current and reliable.


## Dashboard Preview
![Dashboard Screenshot](./Screenshots/final_dashboard.png)



##  Key Insights
- Total COVID-19 Cases, Deaths, and Vaccinations globally  
- Country-wise comparison using bar charts and maps  
- Trend analysis of new and total cases over time  
- Vaccination progress and recovery trends  

---

## Tools & Technologies
- Power BI Desktop
- Python (pandas)


##  How to Recreate the Dataset

1. Ensure you have Python 3 installed with `pandas`.  
   If not, install it using:
   
   pip install pandas
   

2. Run the following script to fetch and save the dataset:
   
   python Python_Script/fetch_covid_data.py
   

3. A file named "covid_data.csv" will be created in the same folder.

4. In Power BI:
   - Go to "Home → Get Data → Text/CSV"
   - Load the newly created `covid_data.csv` file
   - Apply transformations and visuals as shown in this dashboard



##  Last Updated
This dashboard reflects data as of the latest refresh date.



##  Author
Pranav Malik 
[LinkedIn Profile](https://www.linkedin.com/in/pranav-malik-b31884330)
