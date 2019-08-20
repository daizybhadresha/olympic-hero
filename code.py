# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'},inplace=True)

data.head(10)

# ---------------------
# Finding out which olympic event(Summer/ Winter/ Both) does a country perform better in

#Creating new column 'Better_Event'
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter'))

#Finding the value with max count in 'Better_Event' column
better_event = data['Better_Event'].value_counts().nlargest(1).index[0]

#Printing the better event
print('Better_Event=', better_event)

# ---------------------
# Finding out the best performing countries across all events : Which are the top 10 performing teams at summer event (with respect to total medals), winter event and overall?
# How many teams are present in all of the three lists above?

#Function for top 10
def top_ten(df,col_name):
    country_list = df.nlargest(10, col_name)
    return country_list['Country_Name'].values.tolist()

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#Dropping the last row
top_countries.drop(top_countries.index[-1], inplace=True)

# Calling the function for Top 10 in Summer
top_10_summer = top_ten(top_countries, 'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

#Calling the function for Top 10 in Winter
top_10_winter = top_ten(top_countries, 'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

#Calling the function for Top 10 in both the events
top_10 = top_ten(top_countries, 'Total_Medals')
print("Top 10:\n",top_10, "\n")

#Extracting common country names from all three lists
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print('Common Countries :\n', common, "\n")

# ---------------------
# Plot the medal count of the top 10 countries

# Creating the dataframes
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

# Plotting the bar graph
summer_df.plot(x = 'Country_Name', y='Total_Summer', kind='bar', color='red')
plt.xlabel('Country Names')
plt.ylabel('Total Medals')
plt.title('Top 10 Countries for Summer Event')
plt.show()

winter_df.plot(x = 'Country_Name', y='Total_Winter', kind='bar', color='blue')
plt.xlabel('Country Names')
plt.ylabel('Total Medals')
plt.title('Top 10 Countries for Winter Event')
plt.show()

top_df.plot(x = 'Country_Name', y='Total_Medals', kind='bar', color='green')
plt.xlabel('Country Names')
plt.ylabel('Total Medals')
plt.title('Top 10 Countries for Summer & Winter Event')
plt.show()

# ---------------------
# Top performing country(Gold)
# Winning silver or bronze medals is a big achievement but winning gold is bigger.
# Finding out which country has had the best performance with respect to the ratio between gold medals won and total medals won.

#For Summer List
#Creating new column 'Golden_Ratio'
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']

#Finding the max value of 'Golden_Ratio' column
summer_max_ratio=max(summer_df['Golden_Ratio'])

#Finding the country assosciated with the max value of 'Golden_Ratio' column
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

#For Winter List
#Creating new column 'Golden_Ratio'
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']

#Finding the max value of 'Golden_Ratio' column
winter_max_ratio=max(winter_df['Golden_Ratio'])

#Finding the country assosciated with the max value of 'Golden_Ratio' column
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

#For Overall List
#Creating new column 'Golden_Ratio'
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']

#Finding the max value of 'Golden_Ratio' column
top_max_ratio=max(top_df['Golden_Ratio'])

#Finding the country assosciated with the max value of 'Golden_Ratio' column
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print("Top Summer Country:", summer_country_gold, " with a ratio of %.2f" %summer_max_ratio )
print("Top Winter Country:", winter_country_gold, " with a ratio of %.2f" %winter_max_ratio )
print("Top Country:", top_country_gold, " with a ratio of %.2f" %top_max_ratio )

# ---------------------
# Best in the world
# Winning Gold is great but is winning most gold equivalent to being the best overall perfomer?

data_1 = data.drop(index=data.index[-1], axis=0)

#Creating a new column 'Total_Points'
data_1['Total_Points'] = data_1.Gold_Total * 3 + data_1.Silver_Total * 2 + data_1.Bronze_Total 

#Finding the maximum value of 'Total_Points' column
max_index = data_1.Total_Points.idxmax()

#Finding the country assosciated with the max value of 'Total_Column' column
most_points = data_1.loc[max_index, ['Total_Points']].astype(int).values[0]
best_country = data_1.loc[max_index, ['Country_Name']].astype(str).values[0]

print('The maximum points achieved is ', most_points, ' by ', best_country )


# ---------------------
# Plotting the medal counts of the winning country in olmpics (US)

#Subsetting the dataframe
best=data[data['Country_Name']==best_country]
best.reset_index(drop = True, inplace = True)
best=best[['Gold_Total','Silver_Total','Bronze_Total']]

#Plotting bar plot
best.plot.bar(stacked=True)

#Changing the x-axis label
plt.xlabel('United States')

#Changing the y-axis label
plt.ylabel('Medals Tally')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

#Updating the graph legend
l=plt.legend()
l.get_texts()[0].set_text('Gold_Total :' + str(best['Gold_Total'].values))
l.get_texts()[1].set_text('Silver_Total :' + str(best['Silver_Total'].values))
l.get_texts()[2].set_text('Bronze_Total :' + str(best['Bronze_Total'].values))

