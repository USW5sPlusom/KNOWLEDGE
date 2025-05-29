from db.models import Base, engine
from app import app  # импортируем app из app.py

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("База данных и таблицы созданы.")
    app.run(debug=True)