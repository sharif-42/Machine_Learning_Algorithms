from math import sqrt
from statistics import mean


class Normalization:
    def __init__(self, data):
        self.data = data
        self.max = max(data)
        self.min = min(data)
        self.mean = sum(data) / len(data)
        self.variance = round(mean([(x - self.mean) ** 2 for x in data]),3)
        self.std = round(sqrt(self.variance),3)

    def simple_feature_scaling(self):
        # new = old/max
        data = [i / self.max for i in self.data]
        return data

    def min_max(self):
        # new =(old-min)/(max-min)
        arg = self.max - self.min
        data = [round((i - self.min) / arg, 3) for i in self.data]
        return data

    def z_score(self):
        data = [round((i-self.mean)/self.std,3) for i in self.data]
        return data


if __name__ == '__main__':
    data = [1, 2, 10, 20, 100]
    normalize = Normalization(data)

    print("######## Show Statistics ###########")
    print("Original Data:", data)
    print("Min:",normalize.min)
    print("Max:",normalize.max)
    print("Mean:",normalize.mean)
    print("Variance:", normalize.variance)
    print("Standard Daviation:", normalize.std)
    print("####################################")


    print("Simple Feature Scaling Normalizations:", normalize.simple_feature_scaling())
    print("Min Max Normalizations:", normalize.min_max())
    print("Standard Z_Score Normalizations:", normalize.z_score())
    print("Normalization Done")
