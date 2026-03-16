from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from src.api.adapters.connections import AppSession
from src.api.adapters.orm.app import UserORM
from src.api.application.common.repositories import UsersRepositoryI


class UsersRepository(UsersRepositoryI):
    def __init__(self, session: AppSession) -> None:
        self.session = session

    async def fetch_user_id(self, login: str) -> int:
        query = select(UserORM.id).where(UserORM.login == login)
        res = await self.session.execute(query)
        try:
            return res.scalar_one()
        # TODO: Hilarious special case but this is obvously bad
        except NoResultFound:
            return 0
