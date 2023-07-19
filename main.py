from core.database import conn, cur, conn_sqlalchemy
from scrapper.match_info import match_info

csv_path = r'C:\Users\bruni\python\github.com\brnocorreia\VLR.gg-Data-Scrapper\test_vlrgg.csv'

table_create_sql = '''
CREATE TABLE IF NOT EXISTS partida (
    id SERIAL NOT NULL,
    evento VARCHAR(255) NOT NULL,
    data_partida VARCHAR(40) NOT NULL,
    hora_partida VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
)
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cur.execute(table_create_sql)
    cur.execute('TRUNCATE TABLE partida')
    conn.commit()
    cur.close()

    df = match_info(
        'https://www.vlr.gg/237268/gen-g-vs-talon-esports-champions-tour-2023-pacific-last-chance-qualifier-ubqf')
    df.to_sql('partida', con=conn_sqlalchemy, if_exists='append', index=False)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
