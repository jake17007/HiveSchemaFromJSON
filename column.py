import re

SQL_TO_HQL_DATATYPE_MAPPINGS = {
    'text': 'string',
    'guid': 'bigint',
    'enum': 'string',  # TODO: may be able to make this varchar(?)
    'datetime': 'timestamp'
}


class Column:

    def __init__(self, column_dict):
        self.type = column_dict['type']
        self.description = None
        if 'description' in column_dict:
            self.description = re.escape(column_dict['description'])
        self.name = column_dict['name']
        if self.type == 'varchar':
            self.type = 'varchar({})'.format(column_dict['length'])
        if self.type in SQL_TO_HQL_DATATYPE_MAPPINGS:
            self.type = SQL_TO_HQL_DATATYPE_MAPPINGS[self.type]

    def to_hql_expr(self):
        hql = []
        hql.append(self.name)
        hql.append(self.type)
        if self.description:
            hql.append('COMMENT \'{}\''.format(self.description))
        return ' '.join(hql)
