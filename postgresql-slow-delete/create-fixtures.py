#!/usr/bin/env python3

import random


def main():
    facilities = []
    for idx in range(25000):
        name = random.choice([
            'Super Facility',
            'Super secret',
            'Zone 51',
            'Hidden place',
            'Desert',
            'The cave'
        ]) + ' ' + str(int(random.random() * 100000000))
        print(f'''INSERT INTO facilities(id, name) VALUES({idx}, '{name}');''')
        facilities.append(idx)

    for idx in range(1, 25000):
        first_name = random.choice(['Bob', 'Jordan', 'Michel', 'Jean-Louis', 'Julien', 'Omar'])
        last_name = random.choice(['Gates', 'Douglas', 'Hen', 'U', 'Ockas'])
        print(f'''INSERT INTO users(id, first_name, last_name) VALUES({idx}, '{first_name}', '{last_name}');''')

    for _ in range(25000):
        facility = random.choice(facilities)
        content = random.choice(['Temperature increase', 'Temperature decrease', 'Humidity level', 'Fire alert'])
        print(f'''INSERT INTO logs(facility_id, content, date) VALUES('{facility}', '{content}', NOW());''')


if __name__ == '__main__':
    main()
