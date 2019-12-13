from concurrent.futures.thread import ThreadPoolExecutor
from typing import Generic, TypeVar, Tuple, Callable

T = TypeVar("T")


class ParallelStream(Generic[T]):
    def __init__(self, *data: T, thread_count: int = 2) -> None:
        self.data: Tuple[T] = data

        if not 0 < thread_count < 100:
            thread_count = 2

        self.thread_count = thread_count
        self.amount_per_thread = len(self.data) // self.thread_count

    # foreach: performs an operation on each element
    def for_each(self, consumer: Callable[[T], None] = None) -> None:
        def handle_data(min_index, max_index):
            if consumer is not None:
                for i_ in range(min_index, max_index, 1):
                    consumer(self.data[i_])

        with ThreadPoolExecutor(max_workers=self.thread_count) as executor:
            if self.amount_per_thread == 0:
                executor.submit(handle_data, 0, len(self.data))
            else:
                for i in range(self.thread_count - 1):
                    executor.submit(handle_data, i * self.amount_per_thread, (i + 1) * self.amount_per_thread)
                executor.submit(handle_data, (i + 1) * self.amount_per_thread, len(self.data))
