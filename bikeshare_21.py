import time
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.parser import parse
import datetime as dt
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv' }

def get_filters():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = ''
    while city != 'city':
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n').lower()
        if city == 'chicago' :
            return 'chicago.csv'
        elif city == 'new york':
            return 'new_york_city.csv'
        elif city == 'washington':
            return 'washington.csv'
        else:
            print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York, or Washington.')

def filter_type():

#    """ 
#     Asks user to specify a city, month, and day to analyze.

#     Returns:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     """
#     print('Hello! Let\'s explore some US bikeshare data!')
#     # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#     # TO DO: get user input for month (all, january, february, ... , june)
    filter_type=''
    while filter_type != 'filter_type':
        filter_type=input('\n Would you like to filter the data by month, day,both or no filters?'
                            '\nType none for no  time filter\n').lower()
        if filter_type == 'month':
            return ['month',get_month()]
        elif filter_type == 'day':
            return ['day',get_day()]
        elif filter_type == 'none':
            return ['none','no filter']
        elif filter_type == 'both':
            return(['month',get_month()],['day',get_day()])

        else:
            print("I am not sure how you wanted to filter data.Let's try again ")
    

def get_month():
    month=''
    while month != 'month_input':
        months_dict={'january' : 1,'february' : 2,'march' : 3,'april' :4,'may' :5,'june' :6}

        month=input("\n Which Month you want to searh by"
                        "\n january, february, march, april, may or june\n").lower()
        if month not in months_dict:
            print("sorry ! Please type in a month between january and june")
            return get_month()
        else:
            if month == 'january':
                return 'january'
            elif month == 'february':
                return 'february'
            elif month == 'march':
                return 'march'
            elif month == 'april':
                return 'april'
            elif month == 'may':
                return 'may'
            elif month == 'june':
                return 'june'
        
            

      


#     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
    day_input=''
    while  day_input != 'day_input':
        days_dict={'Monday' : 1,'Tuesday' : 2,'Wednesday' : 3,'Thursday' :4,'Friday' :5,'Saturday':6,'Sunday' :7}

        day_input=input("\n Which day of the week?"
           "\n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n" ).title()
        if day_input not in days_dict:
            print("sorry ! Please type a valid input")
            return get_day()
        else:
            if day_input == 'Monday':
                return 'Monday'
            elif day_input == 'Tuesday':
                return 'Tuesday'
            elif day_input == 'Wednesday':
                return 'Wednesday'
            elif day_input == 'Thursday':
                return 'Thursday'
            elif day_input == 'Friday':
                return 'Friday'
            elif day_input == 'Saturday':
                return 'Saturday'
            elif day_input == 'Saturday':
                return 'Saturday'
            elif day_input == 'Sunday':
                return 'Sunday'




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
    # Filter by city (Chicago, New York, Washington)
   
 # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    
   


    # filter by month and day
    if (month != 'all') and (day!= 'all'):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df=df.loc[(df['month']==month) & (df['day_of_week']== day)]
        
        return df
    #filter by month
    elif month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        return df

    # filter by day of week 
    elif day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
        
        return df
        #return unfiltered df 
    else:
        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
 
    df['time1'] = df['Start Time'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d %H:%M:%S'))
    
    df['time'] = df['time1'].apply(lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S'))
    
    
    df['Year1'] = df['time'].str[0]
    
    df['month1'] = df['time'].str[1]
   
    df['day1'] = df['time'].str[2]
 
    df['hour1'] = df['time'].str[3]
   
    # TO DO: display the most common month
    popular_month=df.groupby('month1')['Start Time'].count()
   
   

    print("Most popular month : " + calendar.month_name[int(popular_month.sort_values(ascending=False).index[0])])


    # TO DO: display the most common day of week
    popular_day=df.groupby('month1')['Start Time'].count()
    print("Most popular day : " + calendar.day_name[int(popular_day.sort_values(ascending=False).index[0])])


    # TO DO: display the most common start hour
    popular_hour=df.groupby('hour1')['Start Time'].count()
   
    popular = popular_hour.sort_values(ascending=False).index[0]
    
    
    if popular>12:
        popular=popular-12
        print (' the most common start hour: {} pm'.format(popular))
    else:
        print (' the most common start hour: {} am'.format(popular))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station_counts = df.groupby('Start Station')['Start Station'].count()
    sorted_start_stations = start_station_counts.sort_values(ascending=False)
    total_trips = df['Start Station'].count()
    most_popular_start_station = "\nMost popular start station: " + sorted_start_stations.index[0] + " "+'\nNo of Trips:'+" " + str(sorted_start_stations[0]) 
    print(most_popular_start_station)
    # TO DO: display most commonly used end station

    end_station_counts = df.groupby('End Station')['End Station'].count()
    sorted_end_stations = end_station_counts.sort_values(ascending=False)
    total_trips = df['End Station'].count()
    most_popular_end_station = "\nMost popular end station: " + sorted_end_stations.index[0] + " "+'\nNo of Trips:'+" " + str(sorted_end_stations[0]) 
    print(most_popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    station_counts = df.groupby('Start Station')['End Station'].count()
    sorted_stations =station_counts.sort_values(ascending=False)
    
    most_popular_combination_of_station = "\nMost popular combination of start station and end station trip: " + sorted_stations.index[0] + " "+'\nNo of Trips:'+" " + str(sorted_stations[0]) 
    print(most_popular_combination_of_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_trip_duration = df['Trip Duration'].sum()

    print('total travel time equals {} seconds'.format(total_trip_duration))
    # TO DO: display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print('mean travel time equals {} seconds'.format(avg_trip_duration))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_type = df.groupby('User Type')['User Type'].count()
    user_type_count = user_type.sort_values(ascending=False)
    user_type_count.head()
    most_popular_user_type = "\n user type: " + user_type_count.index[0] + " " +'count:'+" "+ str(user_type_count[0]) 
    print(most_popular_user_type)
    most_popular_user_type1 = "\n user type: " + user_type_count.index[1] + " "+'count:'+" " + str(user_type_count[1]) 
    print(most_popular_user_type1)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # TO DO: Display counts of gender
def gender_birth_year(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    gender_type = df.groupby('Gender')['Gender'].count()
    gender_count = gender_type.sort_values(ascending=False)
    gender_count.head()
    most_popular_gender_type = "\ngender: " + gender_count.index[0] + " " +'count'+" "+ str(gender_count[0]) 
    print(most_popular_gender_type)
    most_popular_gender_type1 = "\ngender: " + gender_count.index[1] + " " + 'count' + " " +str(gender_count[1]) 
    print(most_popular_gender_type1)


    # TO DO: Display earliest, most recent, and most common year of birth
 
    print('\nThe earliest birth year is {}.\nThe most recent birth year is {}.'
          '\nThe most common birth year is {}.'.format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df,current_line):
	display_input=''
	while display_input != 'yes' or display_input !='no':

		display_input=input('\n Would you like to see raw data? \n Type \'Yes\' Or\'No\'\n').lower()
		if display_input == 'yes':
			print(df.iloc[current_line:current_line+5])
			current_line += 5
			display=input('\n do you want to see more 5 lines of raw data? \nType \'Yes\' Or\'No\'\n').lower()
			if  display !='no' and display !='yes':
				print("\nI'm sorry, I'm not sure if you wanted to see more data or not. Let's try again.")
				return display_data(df, current_line)
			elif display == 'no':
				print("\nYou entered \'NO\'! Are you sure ??!")
				continue
				break

			while display == 'yes':
				if display == 'yes':
					print(df.iloc[current_line:current_line+5])
					current_line += 5
					display=input('\n do you want to see more 5 lines of raw data? \nType \'Yes\' Or\'No\'\n').lower()
					
					if display == 'yes':
						continue
					elif display == 'no':
						print("\nYou entered \'NO\'! Are you sure ??!")
						continue
						break

					elif display !='no' and display !='yes':
						print("\nI'm sorry, I'm not sure if you wanted to see more data or not. Let's try again.")
						return display_data(df, current_line)
			
		elif display_input == 'no':
			print("\nThank You ! Let's continue with further statistics !")
			break
		else:
			print("\nI'm sorry!, I'm not sure if you wanted to see more data or not. Let's try again.")
			return display_data(df, current_line)



    
def main():
    while True:
        value=filter_type()
        
        
        if value[0]=='month':
            month=value[1]
            day='all'
           
        elif value[0]=='day':
            day=value[1]
            month='all'

        elif value[1][0]=='day':
            month=value[0][1]
            day=value[1][1]
        else:
            month='all'
            day='all'
       
        city = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df,0)
        if city =='washington.csv':
            print('Gender and birth year details are not given in a dataset')
        else:
            gender_birth_year(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
