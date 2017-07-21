from typing import Optional


class CacheBackend:
    async def get(self, key: str, format: str = 'html') -> Optional[bytes]:
        raise NotImplementedError

    def set(self, key: str, payload: bytes, ttl: int = None, format: str = 'html') -> None:
        raise NotImplementedError

    def modified_since(self, key: str, format: str = 'html') -> int:
        raise NotImplementedError
