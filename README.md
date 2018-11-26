# HiveSchemaFromJSON

HiveSchemaFromJSON is a tool that creates an HQL script to create a Hive schema, i.e. a number of tables, given a JSON file as input.

## Requirements

Python 3.x is required for installation and running HiveSchemaFromJSON. For Python 3 installation instructions, see https://www.python.org/.

## Running HiveSchemaFromJSON

To run HiveSchemaFromJSON to generate an HQL script, a JSON file must be provided as input. See the "Input" section below for more information. Given the JSON file exists, HiveSchemaFromJSON can be executed with Python 3. See the "Execution" section below for details.

### Input

The JSON file from which the HQL script will be created should specify the structure of the schema to be created. It should be in the following format:

...

### Execution

Given that a proper JSON file exists, execute HiveSchemaFromJSON with the following command. Argument placeholders, indicated with angled brackets (i.e. "`<`arg`>`"), in the command shown should be replaced with the argument specified.

```
$ python3 main.py <input_json_file_path> <output_hql_script_file_path>
```

- `input_json_file_path`: the full path to the JSON file to be used in generating the HQL script, e.g. "`/Users/me/path/to/schema.json`"
- `output_hql_script_file_path`: the full path to the HQL script that will be generated, e.g. "`/Users/me/path/to/schema.hql`". This file will be created if it does not exist at the time of execution. It will be overwritten if it does already exist.
