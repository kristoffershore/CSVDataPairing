import csv

item_list = []
image_list = []

with open('sbimagepairingtest.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   item_list.append({'Item Name': row['Item Name']})
   image_list.append({'Image Name': row['Image Name']})

itemwithimage_list = []

for index, x in enumerate(item_list):
    if x['Item Name'] == '':
        break
    for y in image_list:
        if x['Item Name']+"." in y['Image Name']:
            itemwithimage_list.append({
                'Item Name/Number': x['Item Name'],
                'Item Display Image': y['Image Name']
            })

    if index % 100 == 0:
        print(index, "items done")

print(index, "items done")
print("----------------\nLooping finished.")
print("Total of", index, "items done.\nWriting .csv...")        

keys = ['Item Name/Number', 'Item Display Image']

with open('pairedfields.csv', 'w', newline="") as output_file: 
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows([x for x in itemwithimage_list])
    
print("Complete.\n")