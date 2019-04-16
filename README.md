# Health-Data-Analytics
INTRODUCTION
The objective of this project is to collect, clean, visualize and analyze Health data collected from various resources like UNICEF, WHO, and World Bank. The visualizations are created using technologies like Tableau, Django, Plotly, Matplotlib etc. 

QUESTIONS TO ANSWER:
1) How does Gross Nation Income per capita for selected country affect their Percentage Immunization? Is there a co-relation ?
2) How is BCG Immunization related to Tuberculosis Mortality in selected Country?
3) Can we predict the Mortality due to Tuberculosis in selected Country based on GNP, BCG Immunization, Tuberculosis Incidents and Tuberculosis Mortality data?

The breakdown of the project is as follow:
1) Collect Immunizaton data from UNICEF website, clean and create a time line graph for percentage BCG vaccine data for various counties using Plotly. 
2) Create a Django app to showcase the interactive timeline grpah for different vaccines, and countries with the drop down. Deploy the app through HEROKU.
3) For further analysis Tuberculosis data is collected from WHO website. As WHO data was available from year 2000 to year 2017, the data, BCG immunization data(the vaccine that helps prevent Tuberculosis) is extracted for the similar years using Python Jupyter notebook and pandas library. Similarly, GNP data is collected from World bank website and screened for a selected country to get a precide dataframe to work with.
4) Further analytics is done using Python's Matplotlib library, and Machine Learning library called scikit-learn.

RESOURCES:
1) UNICEF: https://data.unicef.org/topic/child-health/immunization/
2) WHO: https://www.who.int/tb/country/data/download/en/
3) World Bank: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD?view=chart

TECHNOLOGIES USED: Python, Django, Pandas, Plotly, Matplotlib, scikit-learn.
