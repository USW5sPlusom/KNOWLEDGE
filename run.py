from flask import Flask, render_template, request, redirect, url_for
from db.models import Base, engine, Entry, get_db

app = Flask(__name__, template_folder="templates")

@app.route('/add_entry', methods=['POST'])
def add_entry():
    title = request.form.get('title')
    content = request.form.get('content')
    category = request.form.get('category')
    tag = request.form.get('tag')

    if not title or not content or not category:
        return redirect(url_for('index'))

    # Используем контекстный менеджер для сессии
    with get_db() as session:
        new_entry = Entry(
            title=title,
            content=content,
            category=category,
            tag=tag
        )
        session.add(new_entry)
        session.commit()

    return redirect(url_for('index'))

@app.route("/")
def index():
    # Используем контекстный менеджер для сессии
    with get_db() as session:
        entries = session.query(Entry).order_by(Entry.category).all()
        return render_template("index.html", entries=entries)

if __name__ == "__main__":
    # Создаем таблицы
    Base.metadata.create_all(bind=engine)
    print("База данных и таблицы созданы.")
    app.run(debug=True)