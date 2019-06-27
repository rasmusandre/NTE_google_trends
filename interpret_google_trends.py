
""" This script is for obtaining Pearson correlation coefficients between Google Trends data
    and NordPool spot prices in Trondheim for weeks 1-52 in 2018. The script also allows
    for simple visualization of the data.
    27.06.18
    R. A. Tranås
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

keywords_from_trends = {'NTE': 'Nord-Trøndelag elektrisitetsverk', 'GE': 'Gudbrandsdal Energi',
                        'HA': 'Hafslund', 'AMS': 'Avanserte Måle- og Styringssystemer (AMS)', 'SP': 'Strømpris'}

trends = pd.read_csv('google_trends.csv')  # Import data from google trends

el_spot = pd.read_excel('el_spot_prices.xlsx')  # Import prices from NordPool

el_spot_trondheim = np.array(el_spot['Tr.heim'])  # Extract local data

my_check = 0

for obj in trends:

    if obj != 'Uke':
        print(obj)
        #  Do not include week 1 from trends, as it is not included in NordPool prices
        correlation_matrix = np.corrcoef(el_spot_trondheim, trends[obj][1:])
        print(correlation_matrix)

        if np.abs(correlation_matrix[0][1]):

            my_check = obj  # Find largest correlation trend (both negative and positive are of interest)


"""NOTE! my_check can be set to any of the keys in keywords_from_trends to examine other search terms
than the one with the highest correlation with the spot price. e.g. my_check = 'NTE' or my_check = 'AMS'
"""
#my_check = 'NTE'

df_col = np.array(trends[my_check][1:])  # Extract trend which had the largest correlation with spot price
normalized_max_trend = df_col/np.max(df_col)  # Normalize trend data
el_spot_trondheim = el_spot_trondheim/np.max(el_spot_trondheim)  # Normalize spot prices

slope, intercept, r_value, p_value, std_err = stats.linregress(el_spot_trondheim,normalized_max_trend)  # Linear regg.
print('Standard error estimate from linear regression: {}'.format(std_err))

edge_values = np.array([0,1])
lin_reg = np.array([intercept + slope*ev for ev in edge_values])

plt.figure(0)
plt.plot(el_spot_trondheim, normalized_max_trend, 'bo', fillstyle='none',
         label='Spot price vs search frequency for: ' + keywords_from_trends[my_check])  # Plot spot price vs max trend
plt.xlabel('Spot price in Trondheim', fontsize=14)
plt.ylabel('Google search frequency for: ' + keywords_from_trends[my_check], fontsize=14)
plt.xlim([0.9*np.min(el_spot_trondheim), 1.025*np.max(el_spot_trondheim)])  # Set appropriate limit
plt.ylim([0.9*np.min(normalized_max_trend), 1.025*np.max(el_spot_trondheim)])  # Set appropriate limit

plt.plot(edge_values, lin_reg, 'g', label='Linear regression')  # Plot obtained linear regression

plt.legend(fancybox=True, shadow=True, framealpha=0.95)  # Make fancy legend. Just because we can!

actual_weeks = [i for i in range(2, 53)]  # Compensate for the week lost in the NordPool data

plt.figure(1)
plt.plot(actual_weeks, el_spot_trondheim, 'r', label='Spot price in Trondheim')  # Plot spot price per week
plt.plot(actual_weeks, normalized_max_trend, 'b', label='Google search frequency for: ' + keywords_from_trends[my_check])  # max trend
plt.xlabel('Week', fontsize=14)
plt.ylabel('Search frequency/spot price', fontsize=14)
plt.legend(fancybox=True, shadow=True, framealpha=0.95)  # Make fancy legend. Just because we can!

plt.show()
