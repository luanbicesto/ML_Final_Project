import csv

#Sort list using keys
def sort_keys(values):
    n = zip(values, range(1, len(values)+1))
    s = sorted(n, key=lambda x: x[0])
    return [i[1] for i in s]

BASEPATH = '../'
ORIGINAL_CSV = BASEPATH+'training_solutions_rev1.csv'
# csv file containing the solutions by the classifier
GENERATED_CSV = BASEPATH+'training_solutions_rev1.csv'

# Key to Galaxy ID
image_name_key = 'GalaxyID'
equals_key = 'Equals'

# Number of responses for each Class
classes_nresponses = (3, 2, 2, 2, 4, 2, 3, 7, 3, 3, 6)

# All Classes Keys
classes_allnames= [['Class%d.%d'%(i+1,c+1)for c in range(classes_nresponses[i])] for i in range(11)]

#Classes names for new generated csv files
classes_names = tuple(['Class%d'%x for x in range(1,12)])

#Open original csv readers
original_csv = open(ORIGINAL_CSV, 'rb')
reader = csv.DictReader(original_csv)

#generate database
data_dict = {}

for row in reader:
    row_id = row[image_name_key]
    line = []
    for i in range(11):
        values = [float(row[x]) for x in classes_allnames[i]]
        line.append(sort_keys(values))
    data_dict[row_id] = line

original_csv.close()

#Open result csv and generates a csv containing the comparation between the order of values in classes.
generated_csv = open(GENERATED_CSV, 'rb')
reader = csv.DictReader(generated_csv)

compare_csv = open(BASEPATH+'result.csv' , 'wb')
writer = csv.DictWriter(compare_csv, fieldnames = [image_name_key, equals_key])

#Write header in csv file
writer.writeheader()

#Do the comparation and saves in result.csv in BASEPATH
for row in reader:
    row_id = row[image_name_key]
    line = []
    for i in range(11):
        values = [float(row[x]) for x in classes_allnames[i]]
        line.append(sort_keys(values))
    
    if (data_dict[row_id] == line):
        writer.writerow({image_name_key:row_id, equals_key: 1})
    else:
        writer.writerow({image_name_key:row_id, equals_key: 0})

compare_csv.close()
generated_csv.close()
