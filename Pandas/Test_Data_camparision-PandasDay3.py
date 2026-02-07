import pandas as pd
from sqlalchemy import create_engine
import oracledb


mysql_engine_scr = create_engine("mysql+pymysql://root:Admin%40123@localhost:3306/etl")
oracle_engine = create_engine("oracle+oracledb://system:Admin@localhost:1521/xe")

query_mysql_scr1 = "select * from Customers where CustomerID !='C001' "
query_mysql_scr = "select * from Customers "
query_oracle_tar = "select * from customer_info"

def test_compareData1():
    df_scr = pd.read_sql(query_mysql_scr, mysql_engine_scr)
    df_tar = pd.read_sql(query_oracle_tar, oracle_engine)
    assert df_scr.equals(df_tar), "data  matchied"

def test_compareData2():
        df_scr = pd.read_sql(query_mysql_scr1, mysql_engine_scr)
        df_tar = pd.read_sql(query_oracle_tar, oracle_engine)
        assert df_scr.equals(df_tar), "data not matchied"