def jaccard_similarity(lst1, lst2):
    intersection = 0
    union = 0
    for a, b in zip(lst1, lst2):
        if a == b == 1:
            intersection += 1
        if a == 1 or b == 1:
            union += 1
    print(intersection, union)
    return intersection / union


if __name__ == "__main__":
    lst = [
        [1, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 0]
    ]
    for i in range(3):
        print("jaccard similirity between column {} and {} is :{}".
              format(i + 1, i + 2, jaccard_similarity(lst[i], lst[i + 1])))
