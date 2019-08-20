# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'},inplace=True)

data.head(10)
#Code starts here



# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter'))

better_event = data['Better_Event'].value_counts().nlargest(1).index[0]


# --------------
#Code starts here

def top_ten(df,col_name):
    country_list = df.nlargest(10, col_name)
    return country_list['Country_Name'].values.tolist()


top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(top_countries.index[-1], inplace=True)

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))


# --------------
#Code starts here
import matplotlib.pyplot as plt

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

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



# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df.Gold_Summer/summer_df.Total_Summer
max_index = summer_df['Golden_Ratio'].idxmax()
summer_max_ratio = round(summer_df.loc[max_index, ["Golden_Ratio"]].astype(float).values[0], 2)
summer_country_gold = summer_df.loc[max_index, ["Country_Name"]].astype(str).values[0]


winter_df['Golden_Ratio'] = winter_df.Gold_Winter/winter_df.Total_Winter
max_index = winter_df['Golden_Ratio'].idxmax()
winter_max_ratio = round(winter_df.loc[max_index, ["Golden_Ratio"]].astype(float).values[0], 2)
winter_country_gold = winter_df.loc[max_index, ["Country_Name"]].astype(str).values[0]


top_df['Golden_Ratio'] = top_df.Gold_Total/top_df.Total_Medals
max_index = top_df['Golden_Ratio'].idxmax()
top_max_ratio = round(top_df.loc[max_index, ["Golden_Ratio"]].astype(float).values[0], 2)
top_country_gold = top_df.loc[max_index, ["Country_Name"]].astype(str).values[0]



# --------------
#Code starts here

data_1 = data.drop(index=data.index[-1], axis=0)

data_1['Total_Points'] = data_1.Gold_Total * 3 + data_1.Silver_Total * 2 + data_1.Bronze_Total 

max_index = data_1.Total_Points.idxmax()

most_points = data_1.loc[max_index, ['Total_Points']].astype(int).values[0]

best_country = data_1.loc[max_index, ['Country_Name']].astype(str).values[0]

print(most_points)

print(best_country)


# --------------
#Code starts here

best = data[data['Country_Name'] == 'United States'].loc[:,['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()

plt.xlabel('United States')

plt.ylabel('Medals Tally')

plt.xticks(rotation=45)

plt.show()




