from collections.abc import AsyncGenerator
import uuid

from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime



# local database
DATABASE_URL = "sqlite+aiosqlite:///./test.db"


# all models inherites from it like user & post
# Base = DbContext in dotnet

class Base(DeclarativeBase):
    pass





class Post(Base):
    __tablename__ = "posts"

    # id will be 550e8400-e29b-41d4-a716-446655440000 instead of series 1 -> 2 -> 3 -> 4
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Post belongs to User
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)

    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="posts")


# connection to db 
engine = create_async_engine(DATABASE_URL)  # = new DbContext(...) in dotnet

# every Request have a new session -> Session Factory
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Dependency Injection
# every endpoint need session
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


