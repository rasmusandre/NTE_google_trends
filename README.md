# NTE_google_trends
Python script and data (.xlsx/.csv) for analyzing linear correlations between Google search trends and el spot prices in Trondheim for 2018. The search frequencies are obtained from https://trends.google.com/trends/?geo=US Feel free to clone this project and use it on your own.

The google search trends analyzed are: 'Nord-Trøndelag elektrisitetsverk', 'Gudbrandsdal Energi', 'Hafslund', 'AMS', 'strømpris'

From these different Google search trends, 'strømpris' was found to have the greatest correlation with the el spot price in Trondheim. The significant correlation coefficient between the two data sets was found to be 0.372. 

Note that the data is only normalized against the max value found in the data sets, z_i = x_i/max({x}). Thus, the data is not spaced between 0 and 1. To acheive such a normalization, z_i = (x_i - min({x}))/(max({x}) - min({x})), could be used instead.

![time_series](https://user-images.githubusercontent.com/32704599/60349561-28e03c00-99c2-11e9-8fb2-83b020fdce3e.png)

![search_freq_vs_price](https://user-images.githubusercontent.com/32704599/60349688-5cbb6180-99c2-11e9-9484-884df9fb0c25.png)
