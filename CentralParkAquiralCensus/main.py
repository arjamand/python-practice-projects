# 2022-12-15 20:19:58

# with open("weather-data.csv") as weather_data:
#     data=weather_data.readlines()

# import csv
# with open("weather-data.csv") as weather_data:
#     w_data_list=csv.reader(weather_data)
#     only_temp_as_int=[]
#     print(w_data_list)
#     for row in w_data_list:
#         if row[1] == "temp":
#             pass
#         else:
#             only_temp_as_int.append(int(row[1]))
#         print(row)

#     print(only_temp_as_int)

# import pandas
# data=pandas.read_csv("./Day 25/weather-data.csv")

# data_list=(data["temp"]).to_list()

# average=sum(data_list)/len(data_list)

# print(round(average,2))

# max_val=(data["temp"]).max()
# # max_value=data.max(name="temp")

# print(max_val)

# print(data["day"])

# print(data[data.temp==(data.temp).max()])

# monday=data[data.day=="Monday"]
# monday_temp=(monday.temp)


# m=(monday_temp*9/5+32)
# print(m)


import pandas

data = pandas.read_csv(
    "228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv"
)

data_list = (data["Primary Fur Color"]).to_list()

gray = 0
black = 0
cinnamon = 0

for fur in data_list:
    if fur == "Gray":
        gray += 1
    elif fur == "Black":
        black += 1
    elif fur == "Cinnamon":
        cinnamon += 1

data_dict = {"Colours": ["Gray", "Black", "Cinnamon"], "No.": [gray, black, cinnamon]}

d = pandas.DataFrame(data_dict)
print(d)
d.to_csv("./Day 25/Coulour_Data.csv")
# data_dict.to_csv()


# print(data_dict)

# for fur in data_list:
