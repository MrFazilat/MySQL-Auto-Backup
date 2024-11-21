import pymysql
import os
import datetime
import schedule
import time
import threading

db_user = 'username'
db_password = 'password'
db_name = 'database_name'
db_host = 'localhost'
backup_dir = '/path/to/backup/directory'

def backup_mysql():
    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            db=db_name
        )
        
        current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        backup_file = os.path.join(backup_dir, f"{db_name}_backup_{current_time}.sql")

        with open(backup_file, 'w') as backup:
            cursor = connection.cursor()

            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]
                backup.write(f"-- Dumping table: {table_name}\n")
                
                cursor.execute(f"SHOW CREATE TABLE {table_name}")
                create_table_query = cursor.fetchone()[1]
                backup.write(f"{create_table_query};\n\n")
                
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                for row in rows:
                    values = ', '.join([f"'{str(value)}'" if value is not None else 'NULL' for value in row])
                    backup.write(f"INSERT INTO {table_name} VALUES ({values});\n")
                backup.write("\n")

        connection.close()
        print(f"Backup Saved To {backup_file} ")
    except Exception as e:
        print(f"Error: {e}")

def schedule_backup(interval_minutes):
    schedule.every(interval_minutes).minutes.do(backup_mysql)
    
    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    threading.Thread(target=run_schedule, daemon=True).start()

def get_user_input():
    try:
        interval_minutes = int(input("Every Min: "))
        if interval_minutes <= 0:
            print("لطفاً یک عدد مثبت وارد کنید.")
        else:
            schedule_backup(interval_minutes)
            print(f" Backup Set To Every {interval_minutes} Min.")
    except ValueError:
        print("Warning")

if __name__ == "__main__":
    get_user_input()

    while True:
        time.sleep(1)
