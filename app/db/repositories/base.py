from sqlalchemy.pool import Pool


class BaseRepository():
    def __init__(self, connection: Pool) -> None:
        self._connection = connection
    
    @property
    def connection(self) -> Pool:
        return self._connection
