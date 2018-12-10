import csv

ls = []
#we have a very large file of 480 MB so we extract username name from it  [By Muahammad Ghous 59455]
with open('data.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',') 
    line_count = 0
    for row in csv_reader:
        print(row[1])
        ls.append(row[1]+"\n")
leng=len(ls)
#nov saving username to username .csv [By Muahammad Ghous 59455]
for i in range(1):
    with open('resources/username.csv', 'a') as fd:
        fd.writelines(ls)
        print("remaining", leng-i)


