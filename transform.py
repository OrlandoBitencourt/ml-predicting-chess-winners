import hashlib
import csv

def generate_unique_hash(value: str) -> str:
    m = hashlib.md5(value.encode('utf-8'))
    return str(int(m.hexdigest(), 16))[0:12]

input_file = open('chess_games.csv')
reader = csv.reader(input_file)

output_file =  open('output.csv', 'w')
writer = csv.writer(output_file)

reader_data = [row for row in reader]

reader_data[0].append('black_user_unique_id')
reader_data[0].append('white_user_unique_id')

for row in reader_data:
    if row[0] == 'game_id':
        continue
    row.append(int(generate_unique_hash(value=row[7])))
    row.append(int(generate_unique_hash(value=row[9]))) 

writer.writerows(reader_data)

input_file.close()
output_file.close()
