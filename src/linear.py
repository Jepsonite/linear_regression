import csv
from functools import reduce
import matplotlib.pyplot as plt
import numpy


def sum(listOfPoints):
    summa = reduce((lambda x, y: x + y), listOfPoints)
    # print('summa on ' + str(summa))
    return summa

def gradient(someList):
    return float(len(someList) * sum(get_xy(someList)) - sum(get_x(someList)) * sum(get_y(someList))) / float(len(someList) * sum(get_xx(someList)) - sum(get_x(someList)) ** 2)

def intercept(someList):
    return float(sum(get_xx(someList)) * sum(get_y(someList)) - sum(get_x(someList)) * sum(get_xy(someList))) / float(len(someList) * sum(get_xx(someList)) - sum(get_x(someList)) ** 2)

def get_x(points):
    # returns a list of x-coordinates
    x_coordinates = list(map(lambda x: x[0], points))
    # print(x_coordinates)
    return x_coordinates

def get_y(points):
    # returns a list of y-coordinates
    y_coordinates = list(map(lambda x: x[1], points))
    # print(y_coordinates)
    return y_coordinates

def get_xy(points):
    # returns a list of products x_i * y_i
    xy_products = list(map(lambda x: x[0] * x[1], points))
    # print(xy_products)
    return xy_products

def get_xx(points):
    # return a list of products x_i * x_i
    xx_products = list(map(lambda x: x[0]**2, points))
    # print(xx_products)
    return xx_products

def get_y_vals(points, intercept_point, slope):
    # returns the y-coordinates of the linear regression line
    y_vals = list(map(lambda x: intercept_point + slope * x[0], points))
    # print(y_vals)
    return y_vals

def main():
    with open('test.csv', 'r') as file:
        # reader = csv.reader(file)
        # my_list = list(reader)
        my_list = [list(map(int, line)) for line in csv.reader(file, delimiter=',')]
    # print(my_list)
    # print(gradient(my_list))
    # print(intercept(my_list))
    intercept_point = intercept(my_list)
    slope = gradient(my_list)
    y_vals = get_y_vals(my_list, intercept_point, slope)
    x_list = get_x(my_list)
    y_list = get_y(my_list)
    plt.scatter(x_list, y_list, color = 'red')
    plt.plot(x_list, y_vals, color = 'cyan')
    plt.show()

main()