import csv

ls = []
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row[1])
        ls.append(row[1]+"\n")
leng=len(ls)
for i in range(1):
    with open('username.csv', 'a') as fd:
        fd.writelines(ls)
        print("remaining", leng-i)


