class JaccardSimilarity:
    # A Class for searching Jaccard Similarity

    @staticmethod
    def get_transpose_matrix(lst):
        # This Function take a matrix as input and return the transpose matrix of the input matrix
        transpose_matrix = [[row[i] for row in lst] for i in range(1, len(lst[0]))]
        return transpose_matrix

    @staticmethod
    def similarity_calc(lst1, lst2):
        """
        This is the actual function to calculate jaccard similarity.
        take two column as input and calculate jaccard similarity between the two column
        """
        intersection = 0
        union = 0
        for a, b in zip(lst1, lst2):
            if a == b == 1:           # calculate intersection between two column
                intersection += 1
            if a == 1 or b == 1:      # calculate union between two column
                union += 1
        return intersection / union   # return jaccard similarity between two column


if __name__ == "__main__":
    matrix = [['SHINGLES', 'D1', 'D2', 'D3'],   # this is our matrix
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
    print("Input Matrix:\n")
    for row in matrix:       # show the input matrix
        print(row)
    transpose_matrix = JaccardSimilarity.get_transpose_matrix(matrix[1:])  # transpose the matrix
    needed_list = [(0, 1), (0, 2), (1, 2)]    # combination of column for which we calculate the jaccard similarity

    print("\nOutput:")
    for i in needed_list:    # Calculation for jaccard similarity
        print("jaccard similirity {D%d , D%d} = %0.2f" %
              (i[0]+1, i[1]+1, JaccardSimilarity.similarity_calc(transpose_matrix[i[0]], transpose_matrix[i[1]])))