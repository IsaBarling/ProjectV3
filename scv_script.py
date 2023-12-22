import pandas as pd
from sqlalchemy import create_engine

# Путь к твоему CSV файлу
csv_file = 'D://diplom/heartrate_seconds_merged.csv'

# Путь к твоей базе данных SQLite (изменить на актуальный путь)
sqlite_db = 'db.sqlite3'

# Создание соединения с базой данных
engine = create_engine(f'sqlite:///{sqlite_db}')

# Чтение данных из CSV
data = pd.read_csv(csv_file)

# Загрузка данных в базу данных
data.to_sql('heartrate', con=engine, if_exists='append', index=False)

print("Data imported successfully.")
