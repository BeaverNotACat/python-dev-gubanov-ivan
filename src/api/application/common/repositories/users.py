from abc import abstractmethod
from typing import Protocol


class UsersRepositoryI(Protocol):
    @abstractmethod
    async def fetch_user_id(self, login: str) -> int:
        raise NotImplementedError
