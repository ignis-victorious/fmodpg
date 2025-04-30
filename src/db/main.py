#
#  _________________
#  Import LIBRARIES
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import text
#  Import FILES
from src.config import settings
#  _________________



async_engine: AsyncEngine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True
)

async def init_db():
    async with AsyncSession(async_engine) as session:
        statement =




#
#  _________________
#  Import LIBRARIES
#  Import FILES
#  _________________


