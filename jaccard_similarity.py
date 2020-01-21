class JaccardSimilarity:

    @staticmethod
    def get_transpose_matrix(lst):
        transpose_matrix = [[row[i] for row in lst] for i in range(1, len(lst[0]))]
        return transpose_matrix

    @staticmethod
    def similarity_calc(lst1, lst2):
        intersection = 0
        union = 0
        for a, b in zip(lst1, lst2):
            if a == b == 1:
                intersection += 1
            if a == 1 or b == 1:
                union += 1
        return intersection / union


if __name__ == "__main__":
    lst = [['SHINGLES', 'D1', 'D2', 'D3'],
           ['This', 1, 1, 0],
           ['his_', 1, 1, 0],
           ['is_i', 1, 1, 0],
           ['s_is', 1, 1, 0],
           ['_is_', 1, 1, 1],
           ['is_a', 1, 1, 1],
           ['s_a_', 1, 1, 1],

           ['_a_s', 1, 0, 0],
           ['a_sa', 1, 0, 0],
           ['_sam', 1, 0, 0],
           ['samp', 1, 0, 0],
           ['ampl', 1, 0, 0],
           ['mple', 1, 0, 0],
           ['ple_', 1, 0, 0],
           ['le_t', 1, 0, 0],
           ['e_te', 1, 0, 0],

           ['_tex', 1, 1, 1],
           ['text', 1, 1, 1],

           ['ran', 0, 1, 1],
           ['rand', 0, 1, 1],
           ['ando', 0, 1, 1],
           ['ndom', 0, 1, 1],
           ['dom_', 0, 1, 1],
           ['om_t', 0, 1, 1],
           ['m_te', 0, 1, 1],
           ['it_i', 0, 0, 1],
           ['t_is', 0, 0, 1],
           ]
    transpose_matrix = JaccardSimilarity.get_transpose_matrix(lst[1:])
    needed_list = [(0, 1), (0, 2), (1, 2)]
    for i in needed_list:
        print("jaccard similirity {D%d , D%d} = %0.2f" %
              (i[0]+1, i[1]+1, JaccardSimilarity.similarity_calc(transpose_matrix[i[0]], transpose_matrix[i[1]])))

