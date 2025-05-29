from flask import Flask, render_template
from db.models import Base, engine

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("База данных и таблицы созданы.")
    app.run()