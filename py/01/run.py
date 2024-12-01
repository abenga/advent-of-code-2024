from collections import Counter

from pathlib import Path


def get_lists():
    list_file = Path(__file__).parent / "input/lists"
    list_a = []
    list_b = []
    with open(list_file) as f:
        for line in f:
            a, b = [int(el) for el in line.strip().split()]
            list_a.append(a)
            list_b.append(b)
    list_a.sort()
    list_b.sort()
    return list_a, list_b


def puzzle1():
    list_a, list_b = get_lists()

    print(sum([abs(list_a[i] - list_b[i]) for i in range(len(list_a))]))


def puzzle2():
    list_a, list_b = get_lists()
    counts = Counter(list_b)
    similarity_score = sum([el * counts.get(el, 0) for el in list_a])

    print(similarity_score)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
