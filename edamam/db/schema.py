from sqlalchemy import (
    Column, Date, Enum as PgEnum, ForeignKey, ForeignKeyConstraint, Integer,
    String, Table, MetaData
)

from enum import Enum, unique

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),

    # Именование индексов
    'ix': 'ix__%(table_name)s__%(all_column_names)s',

    # Именование уникальных индексов
    'uq': 'uq__%(table_name)s__%(all_column_names)s',

    # Именование CHECK-constraint-ов
    'ck': 'ck__%(table_name)s__%(constraint_name)s',

    # Именование внешних ключей
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',

    # Именование первичных ключей
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

@unique
class Gender(Enum):
    female = 'female'
    male = 'male'

user_table= Table(
    'citizens',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False),
    Column('diet', String, nullable=False),
    Column('gender', PgEnum(Gender, name='gender'), nullable=False),
)