import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': open("D://chicago.csv"),
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Please chose from those cities (Chicago, New York City, Washington ) data to explore: ")
    city = input("You can type 'ch' for chicago, 'ny' for New York City and 'wa' for Washington ").lower()
         
    while city not in(CITY_DATA.keys()):

        print("You provided invaled city name")
        city = input("You can type 'ch' for chicago, 'ny' for New York City and 'wa' for Washington: ").lower()
       
        
    date_filter = input("Would you like to filter the data by month, day, both, or not at all? Type 'none' for no time filter. ").lower()
    while date_filter not in ['month','day','both','none']:
       print("You provided invalid filter")
       date_filter = input("Would you like to filter the data by month, day, both, or not at all? Type 'none' for no time filter ").lower()
   

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
    if date_filter == 'month' or date_filter == 'both':
       print ( "which month? you can type the first three letters for the chosen month")
       month = input('Type Jan, Feb, Mar, Apr, May, or Jun? ').lower()
       while month not in months:
           print("You provided invalid month")
           month = input('type Jan, Feb, Mar, Apr, May, or Jun? ').lower()
           
    else: 
       month = "all"


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday','tuseday','wednesday','thursday','friday','saturday']
    if date_filter == 'day' or date_filter == 'both':
       day = input("Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday? ").lower()
       while day not in days:
           print("You provided invalid day")
           day = input("Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday").lower()
    else:
        day = 'all'

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
     
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
    
    month = df['month'].mode()[0]
    print (f'The most common month is: {months[month-1]}')
    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print (f'The most common month is: {day}')
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    rush_hour = df['hour'].mode()[0]
    print (f'The most common start hour is:{rush_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most popular start station is:{popular_start_station}')
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most popular end station is:{popular_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + df['End Station']
    print(f'The most popular trip is: {popular_trip.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = total_duration.days
    hours = total_duration.seconds   //  (60 * 60)
    minutes = total_duration.seconds %   (60 * 60) //60
    seconds = total_duration.seconds %   (60 * 60) % 60
    print (f'Total travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    # TO DO: display mean travel time
    mean_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days = mean_duration.days
    hours = mean_duration.seconds   //  (60 * 60)
    minutes = mean_duration.seconds %   (60 * 60) //60
    seconds = mean_duration.seconds %   (60 * 60) % 60
    print (f'mean tavel time: {days} days {hours} hours {minutes} minutes {seconds} seconds')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print (df['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        print (df['Gender'].value_counts())
    else:
        print ("Sorry there is no gender data to explore")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
       year = df['Birth Year']
       print (f'Earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most common birth year is: {year.mode()[0]}')
              


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city,User_input):
   
   while User_input == 'yes':
     try:
        for chunk in pd.read_csv(CITY_DATA[city] , chunksize=5):
            print(chunk)
        
            User_input = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n')
            if User_input != 'yes':
                print('Thank You')
                break #breaking out of the for loop
        break
     except KeyboardInterrupt:
        print('Thank you')

def main():
    while True:
        
        city,month,day = get_filters()
        df = load_data(city, month, day)
        print (df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        User_input = input ('May you want to have a look on the raw data? Enter yes or no? ')
        display_raw_data(city,User_input)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
