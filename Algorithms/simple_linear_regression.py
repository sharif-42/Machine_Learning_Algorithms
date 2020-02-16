from statistics import mean


class SimpleLinearRegression:
    """
    y = mx + c
    c = y-mx
    m and c are the coefficient of the fit line
    """

    def __init__(self, x, y, total_data):
        print("Linear Regression Calling")
        self.total_data = total_data
        self.x = x
        self.y = y
        self.m = 0  # slope of the line
        self.c = 0  # intercept of y axis

    def calculate_coefficient(self):
        up = 0
        down = 0
        mean_x = mean(self.x)
        mean_y = mean(self.y)
        print(mean_x, mean_y)

        for i in range(self.total_data):
            up += (x[i] - mean_x) * (y[i] - mean_y)
            down += ((x[i] - mean_x) ** 2)

        self.m = up / down
        self.c = mean_y - self.m * mean_x
        print(self.m, self.c)

    def result(self, new_x):
        self.calculate_coefficient()
        res = self.m * new_x + self.c
        print(res)


if __name__ == '__main__':
    total_data = 9
    x = [2.0, 2.4, 1.5, 3.5, 3.5, 3.5, 3.5, 3.7, 3.7]  # Independent Variable
    y = [196, 221, 136, 255, 244, 230, 232, 255, 267]  # Dependent Variable
    SLR = SimpleLinearRegression(x=x, y=y, total_data=total_data)
    new_value = 3.7
    SLR.result(new_value)