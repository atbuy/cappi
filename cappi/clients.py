"""Defines both the sync and async client."""

import asyncio


__all__ = (
    "Client",
    "AsyncClient",
)


class BaseClient:
    def __new__(cls, *args, **kwargs):
        """Don't allow user inheritance."""

        if not issubclass(cls, (Client, AsyncClient)):
            raise TypeError("Inheritance from 'BaseClient' is not allowed.")

        return super().__new__(cls)

    def __init__(self, base_url: str):
        self.base_url = base_url

    def __repr__(self):
        name = self.__class__.__name__
        base_url = self.base_url

        return f"<{name}({base_url=})>"

    def __str__(self):
        return self.__repr__()


class Client(BaseClient):
    """Synchronous client for requests."""


class AsyncClient(BaseClient):
    """Asynchronous client for requests."""
