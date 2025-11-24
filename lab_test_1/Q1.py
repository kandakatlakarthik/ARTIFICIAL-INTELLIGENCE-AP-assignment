import timeit
import random
from typing import List, Callable

def reverse_manual(lst: List[int]) -> List[int]:
    """Reverse with a manual loop."""
    result = []
    for item in reversed(lst):  # reversed iterator avoids index math
        result.append(item)
    return result

def reverse_slice(lst: List[int]) -> List[int]:
    """Reverse via slicing."""
    return lst[::-1]

def reverse_builtin(lst: List[int]) -> List[int]:
    """Reverse using list.reverse (in-place copy)."""
    temp = lst.copy()
    temp.reverse()
    return temp

IMPLEMENTATIONS = {
    "manual": reverse_manual,
    "slice": reverse_slice,
    "builtin": reverse_builtin,
}

def run_correctness_tests():
    cases = [
        [],
        [1],
        [1, 2, 3],
        list(range(10)),
        list(range(10, -1, -1)),
    ]
    for name, func in IMPLEMENTATIONS.items():
        for case in cases:
            expected = list(reversed(case))
            result = func(case)
            assert result == expected, f"{name} failed on {case}"

def benchmark(func: Callable[[List[int]], List[int]], data: List[int], repeat: int = 5, number: int = 1000) -> float:
    timer = timeit.Timer(lambda: func(data))
    return min(timer.repeat(repeat=repeat, number=number)) / number

def main():
    run_correctness_tests()
    data = [random.randint(0, 1_000_000) for _ in range(10000)]

    for name, func in IMPLEMENTATIONS.items():
        reversed_list = func(data)
        print(f"{name} reversed first 10 elements: {reversed_list[:10]}")

    print("\nBenchmark (seconds per call, lower is better):")
    for name, func in IMPLEMENTATIONS.items():
        duration = benchmark(func, data)
        print(f"{name:7s}: {duration:.9f}")

if __name__ == "__main__":
    main()