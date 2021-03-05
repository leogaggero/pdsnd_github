# Explore US Bikeshare Data
*Created on feb 28, 2021*

### Description
A Python script to analyze bikeshare data from 3 mayor US cities. The user can filter the data by city, month and/or day
using a simple numbered menu - no need for typing -  
The script provides a variety of statistics about the use of shared bicycles in the cities of Chicago, New York and Washington.
Raw data is offered to the user at the end of the analysis.

## Statistics and Analysis calculated by the script
1. Popular times of travel  
    * Most common month  
    * Most common day of week  
    * Most common hour of day  


2. Popular stations and trip  
    * Most common start station  
    * Most common end station  
    * Most common trip from start to end  


3. Trip duration  
    * Total travel time  
    * Average travel time  


4. User info  
    * Counts of each user type  
    * Counts of each gender  
    * Earliest, most recent, most common year of birth  

### Files used
* bikeshare.py  
* chicago.csv (dataset)  
* new_york_city.csv (dataset)  
* washington.csv (dataset)  

*Datasets are not provided in this repository because of the large size.  
Original datasets can be found in [capitalbikeshare](https://www.capitalbikeshare.com/system-data)*

### Software needed
Package | Version | Included in | Version  
--------|---------|-------------|---------
Python 3|    3.6.3|  
NumPy   |1.12.1   |Conda        |4.6.14
Pandas  |0.23.3   |Conda        |4.6.14

### How to run the software
```$ python bikeshare.py```  


### The input menu
```
Hello! Let's explore some US bikeshare data!

Which city do you want to explore?
1) Chicago
2) New York City
3) Washington
Please, enter a number from the list: 1

Would you like to filter by day, month, both or none?
1) month
2) day
3) both
4) none
Please, enter a number from the list: 3

Select the month to filter by:
1) January
2) February
3) March
4) April
5) May
6) June
Please, enter a number from the list: 2

Select the day to filter by:
1) Monday
2) Tuesday
3) Wednesday
4) Thursday
5) Friday
6) Saturday
7) Sunday
Please, enter a number from the list: 4

Selected city is Chicago and filtering for February and Thursday
----------------------------------------------------------------
```

### Credits
[pandas.pydata.org](https://pandas.pydata.org/pandas-docs/stable/index.html)  
[docs.python.org](https://docs.python.org/3/)  
[stackoverflow.com](https://stackoverflow.com)  
[knowledge.udacity.com](https://knowledge.udacity.com)  
