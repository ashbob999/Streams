from __future__ import annotations

from typing import List, Generic, TypeVar, Callable, Tuple

import parallel_stream

T = TypeVar("T")  # initial type
S = TypeVar("S")  # mapped to type


class Stream(Generic[T]):
    def __init__(self, *data: T) -> None:
        self.data: Tuple[T] = data
        # self.iterable: Iterable = iter(data)

    def parallel(self) -> parallel_stream.ParallelStream[T]:
        # TODO: make it return a parallel stream
        pass

    # all match: if all elements match a predicate
    def all_match(self, value: S, predicate: Callable[[T], S] = None) -> bool:
        if predicate is None:
            def predicate(x): return x

        for item in self.data:
            if predicate(item) != value:
                return False
        return True

    # any match: if any element matches a predicate
    def any_match(self, value: S, predicate: Callable[[T], S] = None) -> bool:
        if predicate is None:
            def predicate(x): return x

        for item in self.data:
            if predicate(item) == value:
                return True
        return False

    # TODO: collect? - collector type needs checking
    def collect(self, collector: Callable[[T, int], int] = None):
        pass

    # count: number of elements
    @property
    def count(self) -> int:
        return len(self.data)

    # TODO: filter: returns a stream, with certain elements
    def filter(self, predicate: Callable[[T], bool]) -> Stream[T]:
        pass

    # find first: gets the first element in stream, or none
    @property
    def find_first(self) -> T:
        return self.data[0]

    # foreach: performs an operation on each element
    def for_each(self, consumer: Callable[[T], None] = None) -> None:
        if consumer is not None:
            for item in self.data:
                consumer(item)

    # TODO: map: returns a stream for each converted element
    def map(self, function: Callable[[T], S] = None) -> Stream[S]:
        pass

    # TODO: min: returns minimum element
    def min(self, comparator: Callable[[T], int] = None) -> T:
        pass

    # TODO: max: returns maximum element
    def max(self, comparator: Callable[[T], int] = None) -> T:
        pass

    # TODO: of: returns n number of elements
    def of(self, count: int = 0) -> Stream[T]:
        pass

    # TODO: reduce: returns a sum of elements
    def reduce(self, accumulator: Callable[[T, int], int] = None) -> int:
        pass

    # TODO: sorted?
    def sorted(self, comparator: Callable[[T, T], int] = None) -> Stream[T]:
        pass

    # to array
    def to_array(self) -> List[T]:
        return list(self.data)

    @staticmethod
    def list_as_stream(data: List[T]) -> Stream[T]:
        return Stream(*data)

    @staticmethod
    def tuple_as_stream(data: Tuple[T]) -> Stream[T]:
        return Stream(*data)
