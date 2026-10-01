import time
import sys


n = 1_000_000

start = time.time()

numbers = [x * 2 for x in range(n)]
list_sum = sum(numbers)

list_time = time.time() - start
list_memory = sys.getsizeof(numbers)


start = time.time()

numbers_gen = (x * 2 for x in range(n))
generator_sum = sum(numbers_gen)

generator_time = time.time() - start
generator_memory = sys.getsizeof(numbers_gen)


print("List sum:", list_sum)
print("Generator sum:", generator_sum)

print("List time:", list_time)
print("Generator time:", generator_time)

print("List memory:", list_memory)
print("Generator memory:", generator_memory)