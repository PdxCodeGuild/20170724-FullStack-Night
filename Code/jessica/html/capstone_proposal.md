#Capstone Proposal:  Visualize Food Access by County in the United States
##Product Overview: 
Visualize food access data by county in each state. 
##Specific Functionality:
Plot by color (heat-map) percent of population with low access to food on map of the United States by specific counties in each state.
##Data Model: 
The data model contains a list of floats where the percent of population with low access to food at the county level. Low access is defined as: "Number of people in a county living more than 1 mile from a supermarket, supercenter
or large grocery store if in an urban area, or more than 10 miles from a supermarket or
large grocery store if in a rural area." This data is from the Food Environment Atlas from the USDA Economic Research Service. 
https://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads/
##Technical Components:
1. Open excel data in python using pandas package (pandas.read_excel)
2. Put data into database using SQLite
3. Visualize data using D3. D3 supports SVG which will be used in the process of mapping the counties in each state. 
 
##Schedule:

##Further Work:
Other things to calculate using pandas package in python, transfer data from python to database using SQLite, and visualize data using D3:
1. Correlations between food access and health outcomes (pandas.DataFrame.corr)
2. Calculate access % change over five years (pandas.DataFrame.pct_change)
3. Visualize food insecurity over time by state


