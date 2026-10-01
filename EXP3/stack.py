from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        return self.items[-1]


stack = Stack[int]()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.items)
print("Popped:", stack.pop())
print("Top:", stack.peek())