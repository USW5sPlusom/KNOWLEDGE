from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from datetime import datetime
from contextlib import contextmanager

engine = create_engine("sqlite:///db/knowledge.db", echo=True)
Base = declarative_base()

# Создаем фабрику сессий
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Добавляем удобный контекстный менеджер
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(100))
    tag = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Entry(title={self.title!r}, category={self.category!r})>"