""" PYTHON PROJECT - Explore US Bikeshare Data - Programming for Data Science Nanodegree Program - Student: Leonardo Gaggero """

import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { "chicago": "chicago.csv",
              "new york city": "new_york_city.csv",
              "washington": "washington.csv" }


def select_options(options):
    """
    Print a numbered list with options for the user to select.
    The list of options is an input parameter.
    Using this menu makes user experience faster and avoids possible typing errors.

    Returns:
        (str) option selected from the input list.
    """
    counter = 1
    for option in options:
        print("{}) {}".format(counter, option))
        counter += 1
        
    while True:
        try:
            user_selection = int(input("Please, enter a number from the list: "))
        except:
            print("That is not a valid input. Use only integer numbers.")
            continue
        if (user_selection < 1) or (user_selection > len(options)):
            print("You have not entered a number from the list. Please, try again.")
        else:
            break
    return  options[user_selection - 1]
    # Substract 1 because the list positions start at 0, not 1 like the options menu. 
    # But for user interface looks better to start at 1.


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # Initialize variables
    city_options = ["Chicago","New York City","Washington"]
    filter_options = ["month","day","both","none"]
    month_options = ["January","February","March","April","May","June"]
    day_options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        
    print("-"*40)
    print("Explore US Bikeshare Data")
    print("-"*40)
    print("\nWelcome! Let\'s dive into some data analysis!\n")

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("\nWhich city do you want to explore?")
    city = select_options(city_options)
    
    #ask about day, month, both or not at all?
    print("\nWould you like to filter by day, month, both or none?")
    filter = select_options(filter_options)

    # get user input for month
    if filter == "month":
        print("\nSelect the month to filter by:")
        month = select_options(month_options)
        day = "all" #set day filter to all because it´s not used.
        print("\nSelected city is {} and filtering for {} ".format(city, month))

    # get user input for day of week
    elif filter == "day":
        print("\nSelect the day to filter by:")
        day = select_options(day_options)
        month = "all" #set month filter to all because it´s not used.
        print("\nSelected city is {} and filtering for {} ".format(city, day))

    elif filter == "both":        
        print("\nSelect the month to filter by:")
        month = select_options(month_options)
        print("\nSelect the day to filter by:")
        day = select_options(day_options)
        print("\nSelected city is {} and filtering for {} and {} ".format(city, month, day))
        
    # if no filter is needed then set variables to "all"
    elif filter == "none":
        month = "all"
        day = "all"
        print("\nSelected city is {} and no filtering set.".format(city))
    
    print("-"*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Replace spaces in city name by underscores to make it filename standard. Also make it lowercase.
    # The city name is changed only in the scope of this function.
    city = city.replace(" ","_").lower()
    try:
        df = pd.read_csv("./{}.csv".format(city))
    except:
        print("ERROR: There was a problem when loading {}.csv".format(city))
        exit()
        
    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # extract month, week_day and hour from the Start Time column to create new columns
    df["month"] = df["Start Time"].dt.month_name()
    df["week_day"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    if (month != "all") & (day != "all"):
        df = df.loc[(df.month == month) & (df.week_day == day)]
    elif (month == "all") & (day != "all"):
        df = df.loc[df.week_day == day]
    elif (month != "all") & (day == "all"):
        df = df.loc[df.month == month]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time() #this is used at the end to calculate the processing time for the function.

    # display the most common month
    most_month = df["month"].mode()[0]
    most_month_count = df["month"].value_counts()
    print("Most common month: {}. With a count of: {} trips.".format(most_month, most_month_count[most_month]))
    
    # display the most common day of week
    most_day = df["week_day"].mode()[0]
    most_day_count = df["week_day"].value_counts()
    print("Most common day: {}. With a count of: {} trips.".format(most_day, most_day_count[most_day]))

    # display the most common start hour
    most_hour = df["hour"].mode()[0]
    most_hour_count = df["hour"].value_counts()
    print("Most common hour: {}. With a count of: {} trips.".format(most_hour, most_hour_count[most_hour]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    frequent_start = df["Start Station"].mode()[0]
    frequent_start_count = df["Start Station"].value_counts()
    print("Most common Start Station: {}. With a count of: {} trips.".format(frequent_start, frequent_start_count[frequent_start]))

    # display most commonly used end station
    frequent_end = df["End Station"].mode()[0]
    frequent_end_count = df["End Station"].value_counts()
    print("Most common End Station: {}. With a count of: {} trips.".format(frequent_end, frequent_end_count[frequent_end]))

    # display most frequent combination of start station and end station trip
    frequent_combination = ("START: " + df["Start Station"] + " - END: " + df["End Station"]).mode()[0]
    frequent_combination_count = ("START: " + df["Start Station"] + " - END: " + df["End Station"]).value_counts()
    print("Most common trip: {}. With a count of: {} trips.".format(frequent_combination, frequent_combination_count[frequent_combination]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_travel_time_sec = int(df["Trip Duration"].sum())
    total_travel_time_formated = str(datetime.timedelta(seconds = total_travel_time_sec))
    print("Total travel time: {}".format(total_travel_time_formated))
        
    # display mean travel time
    mean_travel_time_sec = int(df["Trip Duration"].mean())
    mean_travel_time_formated = str(datetime.timedelta(seconds = mean_travel_time_sec))    
    print("Mean travel time: {}".format(mean_travel_time_formated))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()
    
    # Display counts of user types
    user_type_count = df["User Type"].value_counts()
    print("Count of users by group type:")
    # convert result to a list to avoid printing of "Name: User Type, dtype: int64" at the end.
    for i in range(len(user_type_count.index.values)):
        print(user_type_count.index.values[i], ": ", list(user_type_count)[i])

    # Display counts of gender (only available for NYC and Chicago)
    try:
        gender_count = df["Gender"].value_counts()
        print("\nCount of users by gender:")
        for i in range(len(gender_count.index.values)):
            print(gender_count.index.values[i], ": ", list(gender_count)[i])
    except KeyError:
        print("\nSorry, no gender information for this city.")

    # Display earliest, most recent, and most common year of birth (only available for NYC and Chicago)
    try:
        year_min = int(df["Birth Year"].min(skipna=True))
        year_max = int(df["Birth Year"].max())
        year_common = int(df["Birth Year"].mode()[0])
        print("\nUsers birth year stats:")
        print("Earliest: {}".format(year_min))
        print("Most recent: {}".format(year_max))
        print("Most common: {}".format(year_common))
    except KeyError:
        print("\nSorry, no birth year information for this city.")        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)


def show_raw_data(df):
    """Displays 5 rows at a time and asks the user to show 5 more or exit."""
    
    # Remove extra columns created by previous functions.
    df.drop(["month", "week_day", "hour"], axis = 1, inplace = True)
    start_row = 0

    print("Do you want to see the first 5 rows of data?")
    while select_options(["yes","no"]) == "yes":
        # modify Pandas configuration to avoid hidding of columns.
        pd.set_option('display.max_columns', None)
        #conditional to avoid a out of bound error.
        if (start_row + 5 > len(df.index) - 1):
            #don´t show first column since it´s only index number.
            print(df.iloc[start_row:len(df.index), 1: ])
            break
        print(df.iloc[start_row: start_row + 5, 1: ])
        start_row += 5
        print("Do you want to see 5 more rows?")       

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        print("-"*40)
        print("\nProgram finished, what would you like to do?")
        if select_options(["restart","exit"]) == "exit":
            break
            

if __name__ == "__main__":
	main()
