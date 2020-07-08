# import sqlalchemy
# from sqlalchemy.dialects.postgresql import psycopg2

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://django:B2wBigD@taPG@localhost:5432/djangodb')

# # select
# df_read = pd.read_sql_table("metas_app_meta1p_teste_inicial", engine)
# df_read_cols = pd.read_sql_table("metas_app_meta1p_teste_inicial", engine, columns=['id', 'marca','dia', 'valor_calculado'])
#
# query = '''select *
#            from metas_app_meta1p_teste_inicial
#            where id = 1'''
# df_read_sql = (query, engine)
#
# print(df_read.dtypes)
# print('******************')
# print(df_read.head())
# print(df_read_cols.head())
# # print(df_read_sql.head())
# print('******************\n')

# insert
# 1P
df_1p = pd.read_csv("/home/marcelio/Tmp/django/modelo_1p.csv")
print(df_1p.head())
df_1p.to_sql(
    name = 'metas_app_meta1p_teste',
    con=engine,
    index=False,
    if_exists='append'
)

# 3P
df_3p = pd.read_csv("/home/marcelio/Tmp/django/modelo_3p.csv")
print(df_3p.head())
df_3p.to_sql(
    name = 'metas_app_meta3p_teste',
    con=engine,
    index=False,
    if_exists='append'
)