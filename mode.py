from collections import Counter
import csv


with open('height_weight.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

data = Counter(new_data)
mode_data_for_range = {
    "100-120": 0,
    "120-140": 0,
    "140-160": 0
}

for weight,occurrence in data.items():
    if   100<float(weight)<120:
        mode_data_for_range["100-120"]+=occurrence
    elif 120<float(weight)<140:
        mode_data_for_range["120-140"]+=occurrence
    elif 140<float(weight)<160:
        mode_data_for_range["140-160"]+=occurrence
mode_range,mode_occurrence = 0,0
for range,occurrence in  mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range,mode_occurrence = [int(range.split("-")[0]),int(range.split("-")[1])],occurrence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")        

