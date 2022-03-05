import hashlib
import csv

def generate_unique_hash(value: str) -> str:
    """    
    Create an integer unique hash from a string value and returns as string
    """
    m = hashlib.md5(value.encode('utf-8'))
    return str(int(m.hexdigest(), 16))[0:12]

input_file = open('chess_games.csv')
reader = csv.reader(input_file)

output_file =  open('output.csv', 'w')
writer = csv.writer(output_file)

# Get data
reader_data = [row for row in reader]

# Creating 2 new column names
reader_data[0].append('black_user_unique_id')
reader_data[0].append('white_user_unique_id')

for row in reader_data:
    # Ignoring first line
    if row[0] == 'game_id':
        continue
    
    # Convert string row to int
    if row[4] == "Black":
        row[4] = 0
    elif row[4] == 'White':
        row[4] = 1
    else: 
        row[4] = 2
    
    # Creating an INT unique id, based on white/black_id
    row.append(int(generate_unique_hash(value=row[7])))
    row.append(int(generate_unique_hash(value=row[9]))) 

# Write output
writer.writerows(reader_data)

input_file.close()
output_file.close()
