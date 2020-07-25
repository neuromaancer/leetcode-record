from collections import Counter


def topKFrequent(nums, k):
    return [
        x for x, _ in sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
    ][:k]


nums = [1, 1, 1, 2, 2, 3]
k = 1

print(topKFrequent(nums, k))
