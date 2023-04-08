# import os, csv, pandas
# filedir = os.path.dirname(__file__)
# with open(os.path.join(filedir, "./weather_data.csv")) as csvinputfile:
#     data = csv.reader(csvinputfile)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    
#     print(temperatures)
# from statistics import mean
import pandas, os
# filedir = os.path.dirname(__file__)
# file = os.path.join(filedir, "./weather_data.csv")
# # data = pandas.read_csv(file)

# temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())

#Get Data in Row
# monday = (data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()] )
# monday_temp_f = (int(monday.temp) * 9/5) + 32

#Create Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
