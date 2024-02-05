# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:06:07 2024

@author: lenovo
"""

#Question 1

#Loading the pfile


import pandas as pd

df=pd.read_csv("C:/Users/lenovo/Desktop/CSS 2024/Week 1/Projects/movie_dataset.csv")


#Removing redundant index column and getting the file information

df=pd.read_csv("C:/Users/lenovo/Desktop/CSS 2024/Week 1/Projects/movie_dataset.csv", index_col=0)

print(df.info())

print(df.describe())

#viewing the entire rows

pd.set_option('display.max_rows',None)

print(df)

x = df["Revenue (Millions)"].mean()

#Filling the empty cells

df["Revenue (Millions)"].fillna(x, inplace = True)

x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace = True)

####################################################

#Highest rated movie

highest_rated_movie = df[df['Rating'] == df['Rating'].max()]

print("Highest-rated movie:")
print(highest_rated_movie[['Title', 'Rating']])

################################


#Average revenue

average_revenue = df['Revenue (Millions)'].mean()

print(average_revenue)

##############################################

#Average revenue from 2015 to 2017
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# Movies released between 2015 and 2017
filtered_df = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')]

average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

print(average_revenue_2015_to_2017)

################################################
#movies released in 2016


movies_2016 = df[df['Year'] == 2016]

num_movies_2016 = len(movies_2016)

print(num_movies_2016)

###################################

# Chris Nolan's movies 

chris_movies = df[df['Director'] == 'Christopher Nolan']

num_chris_movies = len(chris_movies)

print(num_chris_movies)



#####################################
#moviess rated >=8

high_rated_movies = df[df['Rating'] >= 8.0]

number_of_high_rated_movies = len(high_rated_movies)

print(number_of_high_rated_movies)

###################################################

#median of christopher Nolan movies 

chris_movies = df[df['Director'] == 'Christopher Nolan']

median_rating_chris_movies = chris_movies['Rating'].median()

print(median_rating_chris_movies)


###########################################################
#Highest average rating

average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(year_highest_average_rating)

#############################################################

movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

count_2006 = len(movies_2006)
count_2016 = len(movies_2016)

#Percentage increase

percentage_increase = ((count_2016 - count_2006) / count_2006) * 100
print(percentage_increase)

###############################################################


#Most common actor 

actors_df = df['Actors'].str.split(', ', expand=True)

actors_list = actors_df.values.flatten()

actors_count = pd.Series(actors_list).value_counts()

most_common_actor = actors_count.idxmax()

print(most_common_actor)




#################################################
# Unique genre counts

genres_df = df['Genre'].str.split(', ', expand=True)

genres_list = genres_df.values.flatten()

unique_genres_count = len(set(genres_list))

print(unique_genres_count)







