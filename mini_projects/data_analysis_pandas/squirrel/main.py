#Desired Output
# 0, grey, 2473
# 1, red, 392
# 2, black, 103

import pandas, os
filedir = os.path.dirname(__file__)
csvfile = os.path.join(filedir, "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data = pandas.read_csv(csvfile)
colors = data['Primary Fur Color'].to_list()
gray_count = colors.count('Gray')
red_count = colors.count('Cinnamon')
black_count = colors.count('Black')
color_count_dict = {
    'Fur Color' : ["gray", "red", "black"],
    'Count' : [ gray_count , red_count , black_count ]

}

df = pandas.DataFrame(color_count_dict)
df.to_csv("./squirrel_fur.csv")
