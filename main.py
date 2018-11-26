import json

from schema import Schema

INPUT_SCHEMA_FILE = '../schema/schema.json'
OUTPUT_HQL_SCRIPT = 'schema.hql'


def main():
    # Read schema JSON in as dictionary
    with open(INPUT_SCHEMA_FILE) as f:
        schema_dict = json.load(f)
        # Construct the schema
        schema = Schema(schema_dict)

    # Write the HQL create script to the specified output file
    with open(OUTPUT_HQL_SCRIPT, 'w+') as f:
        f.write(schema.to_hql_create_script())

    '''
    # Display distint column types listed in JSON document
    types = set()
    for table in schema.tables:
        for col in table.columns:
            if col.type not in types:
                print(table.table_name + '.' + col.name + ': ' + col.type)
            types.add(col.type)
    print(types)
    '''


if __name__ == '__main__':
    main()
