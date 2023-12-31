from core.database import conn, cur, conn_sqlalchemy
from scrapper.match_info import match_info

table_partida_create_sql = '''
CREATE TABLE IF NOT EXISTS partidas (
    id SERIAL NOT NULL,
    evento VARCHAR(255) NOT NULL,
    data_partida VARCHAR(40) NOT NULL,
    hora_partida VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
)
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cur.execute(table_partida_create_sql)
    cur.execute('TRUNCATE TABLE partidas')
    conn.commit()
    cur.close()

    df = match_info(
        'https://www.vlr.gg/237268/gen-g-vs-talon-esports-champions-tour-2023-pacific-last-chance-qualifier-ubqf')
    df.to_sql('partida', con=conn_sqlalchemy, if_exists='append', index=False)



