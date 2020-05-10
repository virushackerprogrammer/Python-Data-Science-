import pandas as pd
import numpy as np
my_list = np.array([1,2,3,4,5])
my_list1 = np.array([6,7,8,9,10])
#creating a pandas series from a list using pd.Series(<array_or_a_list>)
data_series_1 = pd.Series(my_list)
data_series_2 = pd.Series(my_list1)
print(data_series_1)
print(data_series_2)
print(data_series_1+data_series_2)
#the same as above with 2d lists
my_list2 = np.array([1,2,3,4,5])
data_series_3 = pd.Series(my_list2)
print(data_series_3)
#the .sort_values() method
my_unordered_list = np.array([5,2,4,1,3])
data_series_4 = pd.Series(my_unordered_list)
my_ordered_dataframe1 = data_series_4.sort_values()


