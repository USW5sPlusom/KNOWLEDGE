from flask import Flask, render_template
from db.models import Base, engine, Entry, SessionLocal

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    session = SessionLocal()
    entries = session.query(Entry).order_by(Entry.category).all()
    session.close()
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("База данных и таблицы созданы.")
    app.run()