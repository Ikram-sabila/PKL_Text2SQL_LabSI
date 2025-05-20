from sqlalchemy import create_engine, inspect

engine = create_engine("mysql+pymysql://root:abc@localhost:3306/preposyandu")

inspector = inspect(engine)
tables = inspector.get_table_names()

tabel_info = {}

for table_name in tables:
    columns = inspector.get_columns(table_name)
    tabel_info[table_name] = {}
    for col in columns:
        tipe = str(col["type"]).split(" ")[0].replace('"utf8mb4_unicode_ci"', "").replace("COLLATE", "").strip()
        tabel_info[table_name][col["name"]]=tipe

## Jika ingin melihat full isi database di terminal
# import json
# print(json.dumps(tabel_info, indent=2))
