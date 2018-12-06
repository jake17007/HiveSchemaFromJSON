import json
import sys

from schema import Schema


def main(input_schema_file, output_hql_script):

    # Read schema JSON in as dictionary
    with open(input_schema_file) as f:
        schema_dict = json.load(f)
        # Construct the schema
        schema = Schema(schema_dict)

    # Write the HQL create script to the specified output file
    with open(output_hql_script, 'w+') as f:
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
    if len(sys.argv) != 3:
        print('You must provide input and output file arguments.')
    else:
        main_file, input_schema_file, output_hql_script = sys.argv
        main(input_schema_file, output_hql_script)
