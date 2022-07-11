import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all','saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'friday']

# this Function To Get InFormation From Users
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    #check the name of city 
    # TO DO: get user input for City (chicago, new york city, washington) :
    while True:
        city= input("Please Enter The Name OF City : (chicago, new york city, washington):\n").lower()
        if city not in CITY_DATA:
            #Enter the correct Name
            print("Not able to get the city name please return entering name from these (chicago, new york city, washington):\n")
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june):
    while True:
        month= input("Please Enter The Month :(all, january, february, ... , june) :\n").lower()
        if month in 'all' and  month not in MONTH:
            print("Not able to get the Month please return entering name from these (all:(To Show ALL MONTHS), january, february, ... , june) :\n")
        else:
            break
    # TO DO: get user input for day of week ('all','saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'friday')
    while True:
        day= input("Please Enter The Days :('all','saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'friday')\n").lower()
        if day in 'all' and  day not in DAYS:
            print("Not able to get the Month please return entering name from these (all:(To Show ALL DAYS),saturday, sunday, monday,tuesday, wednesday,friday)\n")
        else:
            break

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    #load CSV Files
    df=pd.read_csv(CITY_DATA[city])
    #Convert start time into Datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extraction process
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = MONTH.index(month)
        # Filteration month To Create New Table
        df = df[df['month']==month]
    if day != 'all':
        # Filteration Day of Week To Create New Table
        df = df[df['day_of_week'] == day.title()]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    try:
        # display the most common month
        common_month = df['month'].value_counts().idxmax()
        print(f"The most common month is : {common_month}")
    except Exception as error:
        print(f"couldn\'t calculated {error}")
    try:
        # display the most common day of week
        common_day_of_week = df['day_of_week'].value_counts().idxmax()
        print(f"The most common day of week is : {common_day_of_week}")
    except Exception as error:
        print(f"couldn\'t calculated {error}")
    # display the most common start hour
    try:
        common_start_hour = df['hour'].value_counts().idxmax()
        print(f"The most common start hour is :{common_start_hour}")
    except Exception as error:
        print(f"couldn\'t calculated {error}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print(f"The common start station => {common_start_station}")

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print(f"Thecommonend station => {common_end_station}")

    # display most frequent combination of start station and end station trip
    common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print(f"The common start station and end station : {common_start_end_station[0]}, {common_start_end_station[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print(f"Total travel time =>  {total_travel}" )

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(f"Mean travel time => {mean_travel}")

    print("Travel time for each user type:\n")
    # display the total trip duration for each user type
    group_by_user_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print(f"each user typ => {group_by_user_trip.index[index]}:{user_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print(f"The count of user types => {str(count_user_types)}\n")
    # As washigton doesn't have Gender and Birth
    if city == 'chicago.csv' or city == 'new_york_city.csv':
    # TO DO: Display counts of gender
        count_gender = df['Gender'].value_counts()
        print(f"The count of user gender => {str(count_gender)}\n")

        # TO DO: Display earliest, most recent, and most common year of birth
        
        earliest_birth = df['Birth Year'].min()
        print(f'Earliest birth => {earliest_birth}\n')
        display_most_recent_birth = df['Birth Year'].max()
        print(f'Most recent birth => {display_most_recent_birth}\n')
        display_most_common_birth = df['Birth Year'].value_counts().idxmax()
        print(f'Most common birth => {display_most_common_birth}\n')
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw data on user request"""
    print(df.head())
    next = 0
    while True:
        view_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])
        
def main():
    while True:
        city, month ,day = get_filters()
        df = load_data(city, month ,day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        while True:
            view_data = input('\nWould you like to view first five row of raw data? Enter (yes) or (no).\n')
            if view_data.lower() != 'yes':
                break
            display_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
