import csv

name_age_list = []

with open('csv_location.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)

    for row in reader:
        name = row[0]
        age = int(row[1])
        name_age_list.append((name, age)) 

name_age_list.sort(key=lambda x: x[1])

num_groups = 5
num_individuals = len(name_age_list)
individuals_per_group = num_individuals // num_groups

groups = [[] for _ in range(num_groups)]

for i, (name, age) in enumerate(name_age_list):
    group_idx = i % num_groups
    groups[group_idx].append((name, age))

output_file = 'output_groups.csv' #output in user logged in folder if not given specific path

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Group', 'Name', 'Age'])

    for i, group in enumerate(groups):
        for name, age in group:
            writer.writerow([f'Group {i + 1}', name, age])

print(f'Exported Successfully {output_file}')