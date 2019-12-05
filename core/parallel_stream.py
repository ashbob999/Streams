import itertools
from typing import Generic, TypeVar, Iterable

T = TypeVar("T")


class ParallelStream(Generic[T]):
    def __init__(self, *iterables: Iterable[T]) -> None:
        self.iterable = itertools.chain(*iterables)

    def parallel(self):
        pass
