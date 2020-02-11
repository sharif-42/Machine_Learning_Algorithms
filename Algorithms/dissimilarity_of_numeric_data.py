class DissimilarityCalculator:
    def __init__(self, data1, data2):
        """
        :type data1: List of int
        :type data2: List of int
        :param data1: 1st row of data set
        :param data2: 2nd row of data set
        data set must have same length.
        """

        self.data1 = data1
        self.data2 = data2
        self.ln = len(data1)  # length of the data sets

    def manhattan_distance(self):
        """
        :return: manhattan distance between the data sets
        """
        diff = 0
        for i in range(self.ln):
            diff += abs(self.data1[i]-self.data2[i])
        return diff

    def euclidean_distance(self):
        """
        :return: euclidean distance between the data sets
        """
        diff = 0
        for i in range(self.ln):
            diff += ((self.data1[i] - self.data2[i]) ** 2)
        distance = round(diff ** 0.5, 2)
        return distance

    def minkowski_distance(self, h):
        """
        :param h: minkowski coefficient , must h>=1
        :return: Minkowski distance between the data sets
        """
        diff = 0
        for i in range(self.ln):
            diff += (abs(self.data1[i] - self.data2[i]) ** h)

        distance = round(diff ** (1/h), 2)
        return distance


if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    data2 = [5, 4, 3, 10, 15]
    ds = DissimilarityCalculator(data1=data1, data2=data2)

    euclidean_distance = ds.euclidean_distance()
    print("Euclidean Distance =", euclidean_distance)

    manhattan_distance = ds.manhattan_distance()
    print("Manhattan Distance =", manhattan_distance)

    minkowski_distance = ds.minkowski_distance(h=1)
    print("Minkowski Distance =", minkowski_distance)