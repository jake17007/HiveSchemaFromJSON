from table import Table


class Schema:

    def __init__(self, json_dict):
        self.schema_dict = json_dict['schema']
        self.tables = self.__tables_from_json_dict()

    def __tables_from_json_dict(self):
        tables = []
        for _, table_dict in self.schema_dict.items():
            tables.append(Table(table_dict,
                                delimiter='\\t',
                                stored_as='TEXTFILE',
                                location='/user/scamicha'))
        return tables

    def to_hql_create_script(self):
        table_create_statements = []
        for table in self.tables:
            table_create_statements.append(table.to_hql_create_statement())
        return '\n\n'.join(table_create_statements)
