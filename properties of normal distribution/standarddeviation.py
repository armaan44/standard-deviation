import pandas as pd
import statistics
import csv

df=pd.read_csv("data.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_standard_deviation=statistics.stdev(height_list)
height_1_std_deviation,height_1_std_deviation_end=[height_mean-height_standard_deviation,height_mean+height_standard_deviation]
height_2_std_deviation,height_2_std_deviation_end=[height_mean-(2*height_standard_deviation),height_mean+(2*height_standard_deviation)]
height_3_std_deviation,height_3_std_deviation_end=[height_mean-(3*height_standard_deviation),height_mean+(3*height_standard_deviation)]
height_list_of_data_within_1_std_deviation=[result for result in height_list if result>height_1_std_deviation and result<height_1_std_deviation_end ]
print(format(len(height_1_std_deviation)*100/len(height_list)))
print(format(len(height_2_std_deviation)*100/len(height_list)))
print(format(len(height_3_std_deviation)*100/len(height_list)))