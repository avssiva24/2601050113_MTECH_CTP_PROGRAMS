from dataclasses import dataclass, field
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Queue(Generic[T]):
    items: deque[T] = field(default_factory=deque)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        return self.items.popleft()


queue = Queue[int]()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:", list(queue.items))
print("Dequeued:", queue.dequeue())
print("Queue after deletion:", list(queue.items))