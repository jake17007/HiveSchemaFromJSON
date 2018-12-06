import re

from column import Column


class Table:

    def __init__(self, table_dict, delimiter='\\t', stored_as='TEXTFILE',
                 location='/user/scamicha'):
        self.table_dict = table_dict
        self.dw_type = table_dict['dw_type']
        self.description = None
        if 'description' in table_dict:
            self.description = re.escape(table_dict['description'])
        self.columns = self.__columns_from_table_dict()
        self.hints = table_dict['hints']
        self.incremental = table_dict['incremental']
        self.table_name = table_dict['tableName']
        self.delimiter = delimiter
        self.stored_as = stored_as
        self.location = location + '/' + self.table_name

    def __columns_from_table_dict(self):
        columns = []
        for column in self.table_dict['columns']:
            columns.append(Column(column))
        return columns

    def to_hql_create_statement(self):
        hql = []
        hql.append('CREATE EXTERNAL TABLE IF NOT EXISTS {} ('.format(
            self.table_name))
        hql.append(',\n'.join([col.to_hql_expr() for col in self.columns]))
        hql.append(')')
        if self.description:
            hql.append('COMMENT \'{}\''.format(self.description))
        hql.append('ROW FORMAT DELIMITED')
        hql.append('FIELDS TERMINATED BY \'{}\''.format(
            self.delimiter))
        hql.append('STORED AS {}'.format(self.stored_as))
        # TODO: maybe put this semicolon on a different line
        hql.append('LOCATION \'{}\';'.format(self.location))
        return '\n'.join(hql)
