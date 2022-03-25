#Reading Score.py
import pandas as pd
import statistics
import csv
df = pd.read_csv("E:\PYTHON projects\PRO-109\StudentsPerformance.csv")
RS_list = df["reading score"].to_list()
#Mean for RS and Weight
RS_mean = statistics.mean(RS_list)
#Median for RS and weight
RS_median = statistics.median(RS_list)
#Mode for RS and weight
RS_mode = statistics.mode(RS_list)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of RS is {}, {} and {} respectively".format(RS_mean, RS_median, RS_mode))
#Standard deviation for RS and weight
RS_std_deviation = statistics.stdev(RS_list)
print("Standard Deviation:",RS_std_deviation)
#1, 2 and 3 Standard Deviations for RS
RS_first_std_deviation_start, RS_first_std_deviation_end = RS_mean-RS_std_deviation, RS_mean+RS_std_deviation
RS_second_std_deviation_start, RS_second_std_deviation_end = RS_mean-(2*RS_std_deviation), RS_mean+(2*RS_std_deviation)
RS_third_std_deviation_start, RS_third_std_deviation_end = RS_mean-(3*RS_std_deviation), RS_mean+(3*RS_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for RS
RS_list_of_data_within_1_std_deviation = [result for result in RS_list if result > RS_first_std_deviation_start and result < RS_first_std_deviation_end]
RS_list_of_data_within_2_std_deviation = [result for result in RS_list if result > RS_second_std_deviation_start and result < RS_second_std_deviation_end]
RS_list_of_data_within_3_std_deviation = [result for result in RS_list if result > RS_third_std_deviation_start and result < RS_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for Weight
#Printing data for RS and weight (Standard Deviation)
print("{}% of data for RS lies within 1 standard deviation".format(len(RS_list_of_data_within_1_std_deviation)*100.0/len(RS_list)))
print("{}% of data for RS lies within 2 standard deviations".format(len(RS_list_of_data_within_2_std_deviation)*100.0/len(RS_list)))
print("{}% of data for RS lies within 3 standard deviations".format(len(RS_list_of_data_within_3_std_deviation)*100.0/len(RS_list)))
