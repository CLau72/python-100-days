
import csv

# with open("weather_data.csv",mode="r",encoding="UTF-8") as f:
#     data = f.readlines()
# 
# print(data)

# with open("weather_data.csv",mode="r",encoding="UTF-8") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temperatures.append(int(temp))
#     print(temperatures)
# 
import pandas
# 
# data = pandas.read_csv("weather_data.csv")
# 
# average_temp = data["temp"].mean()
# high_temp = data["temp"].max()
# 
# print(f"The average temperature is: {average_temp}")
# print(f"The weekly high temperature is {high_temp}")
# 
# 
# # Get Data from a Row
# 
# print(data[data.day == "Monday"])
# 
# print(data[data.temp == data.temp.max()])
# 
# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")