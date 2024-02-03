# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas


# data = pandas.read_csv("weather_data.csv")
# #print(data["temp"])
#
# data_dict = data.to_dict()
#
# #print(data_dict)
#
# data_temp = data["temp"].to_list()
# avg_temp = data["temp"].mean()
# #print(data_temp)
# print(avg_temp)
#
# avg = sum(data_temp) / len(data_temp)
#
# print(avg)
#
# max_temp = data["temp"].max()
#
# print(data[data.temp == max_temp])

data = pandas.read_csv("squirrel_data.csv")

red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

print(f"Red_Squirrel_Count: {red_count}")
print(f"Gray_Squirrel_Count: {gray_count}")
print(f"Black_Squirrel_Count: {black_count}")


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
