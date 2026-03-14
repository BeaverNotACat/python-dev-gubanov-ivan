from asyncio import set_event_loop_policy

from src.api.adapters.engines import AppSession, LogsSession
from src.api.di.container import container
from src.cli.factories.app import (
    BlogMockFactory,
    CommentMockFactory,
    PostMockFactory,
    UserMockFactory,
)
from src.cli.factories.logs import LogMockFactory

BLOG_COUNT_MULTIPLIER = 3
POST_COUNT_MULTIPLIER = 9
COMMENT_COUNT_MULTIPLIER = 9


async def mock_app(count: int) -> None:
    session = await container.get(AppSession)
    UserMockFactory.__async_session__ = session
    BlogMockFactory.__async_session__ = session
    PostMockFactory.__async_session__ = session
    CommentMockFactory.__async_session__ = session

    await UserMockFactory.create_batch_async(count)
    for _ in range(count * BLOG_COUNT_MULTIPLIER):
        await BlogMockFactory.create_async(
            owner_id=BlogMockFactory.__random__.randint(1, count)
        )
    for _ in range(count * POST_COUNT_MULTIPLIER):
        await PostMockFactory.create_async(
            author_id=PostMockFactory.__random__.randint(1, count),
            blog_id=PostMockFactory.__random__.randint(
                1, count * BLOG_COUNT_MULTIPLIER
            ),
        )
    for _ in range(count * COMMENT_COUNT_MULTIPLIER):
        await CommentMockFactory.create_async(
            author_id=CommentMockFactory.__random__.randint(1, count),
            post_id=CommentMockFactory.__random__.randint(
                1, count * POST_COUNT_MULTIPLIER
            ),
        )
    await session.close()


async def mock_logs(count: int) -> None:
    session = await container.get(LogsSession)
    LogMockFactory.__async_session__ = session

    await LogMockFactory.create_batch_async(count)
    # await session.commit()
    await session.close()
