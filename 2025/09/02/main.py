import csv
import random


def main():
    data = db()
    weapons = data.get('weapon', [])

    print(weapons[random.randint(0, len(weapons)-1)].get('name'))


def db():
    data = {}
    with open('db.csv', newline='\n') as db_file:
        reader = csv.DictReader(db_file, delimiter=';')
        for row in reader:
            data_type = row['type']
            if data_type not in data:
                data[data_type] = []

            data[data_type].append(row)

    return data


if __name__ == "__main__":
    main()
