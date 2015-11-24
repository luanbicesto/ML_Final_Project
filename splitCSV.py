import csv

BASEPATH = './'
ORIGINAL_CSV = BASEPATH+'training_solutions_rev1.csv'
# Key to Galaxy ID
image_name_key = 'GalaxyID'

# Number of responses for each Class
classes_nresponses = (3, 2, 2, 2, 4, 2, 3, 7, 3, 3, 6)

# All Classes Keys
classes_allnames= [['Class%d.%d'%(i+1,c+1)for c in range(classes_nresponses[i])] for i in range(11)]

#Classes names for new generated csv files
classes_names = tuple(['Class%d'%x for x in range(1,12)])

#Create csv writers
file_objects = [open(BASEPATH + classes_names[i]+'.csv' ,'wb') for i in range(0, 11)]
csv_writer_dicts = [csv.DictWriter(file_objects[i], fieldnames=[image_name_key, classes_names[i]]) for i in range(0, 11)]

#Write headers in csv files
for w in csv_writer_dicts:
    w.writeheader()

#Open original csv readers
original_csv = open(ORIGINAL_CSV, 'rb')
reader = csv.DictReader(original_csv)

#Save csv files
for row in reader:
    row_id = row[image_name_key]
    for i in range(11):
        values = [float(row[x]) for x in classes_allnames[i]]
        response = values.index(max(values))+1
        csv_writer_dicts[i].writerow({image_name_key:row_id, classes_names[i]: response})

#Close all files
for f in file_objects:
    f.close()
original_csv.close()

