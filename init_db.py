from models import init_db, seed_data

if __name__ == '__main__':
    print("Создаю таблицы...")
    init_db()
    print("Заполняю тестовыми данными...")
    seed_data()
    print("Готово! База данных создана.")