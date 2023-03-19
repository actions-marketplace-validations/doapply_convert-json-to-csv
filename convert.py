import json
import sys
import agate

def main(json_file, csv_file):
    with open(json_file) as f:
        data = json.load(f)
    
    column_names = ['key', 'value']
    column_types = [agate.Text(), agate.Text()]

    table = agate.Table.from_dict(data, column_names=column_names, column_types=column_types)

    table.to_csv(csv_file)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
