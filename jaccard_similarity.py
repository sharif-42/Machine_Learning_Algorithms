class JaccardSimilarity:

    @staticmethod
    def get_transpose_matrix(lst):
        transpose_matrix = [[row[i] for row in lst] for i in range(len(lst[0]))]
        return transpose_matrix

    @staticmethod
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
    column = 4
    columns = [i for i in range(column)]
    print(columns)

    lst = [[1, 0, 1, 1],
           [0, 1, 1, 1],
           [0, 1, 0, 0],
           [1, 0, 1, 1],
           [0, 0, 0, 1],
           [1, 1, 1, 0],
           [1, 1, 0, 0]
           ]
    print(lst[0])
    transpose_matrix = JaccardSimilarity.get_transpose_matrix(lst)

    # for i in range(3):
    #     print("jaccard similirity between column {} and {} is :{}".
    #           format(i + 1, i + 2, jaccard_similarity(lst[i], lst[i + 1])))

    # rows, columns = list(map(int, input().split()))  # input no. of row and column
    # lst = []
    # for i in range(rows):
    #     a = list(map(int, input().split()))
    #     lst.append(a)

    """ dummy inputs
    7 4
    1 0 1 1
    0 1 1 1
    0 1 0 0
    1 0 1 1
    0 0 0 1
    1 1 1 0
    1 1 0 0
    """
