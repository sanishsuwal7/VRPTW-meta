"""
file: figure.py
description: This program creates plots or graphs found by vehicles or ants
language: python3
author: Sanish Suwal(ss4657@rit.edu), Jay Nair(an1147@rit.edu), Bhavdeep Khileri(bk2281@rit.edu)
"""

import os

from matplotlib import pyplot as plt


def plot_customers_and_routes(customers, routes, filename):
    """
    Creates images from the best paths travelled by vehicles
    :param customers: customers or nodes
    :param routes: best path
    :param filename:name of image file to be saved
    :return: None
    """

    # Splitting the list into sublists before each occurrence of 0
    routes = [[0] + routes[i + 1:j] for i, j in
                     zip([-1] + [idx for idx, val in enumerate(routes) if val == 0],
                         [idx for idx, val in enumerate(routes) if val == 0])]



    routes = [route for route in routes if len(route) >= 3]
    colors = [
        'red', 'blue', 'green', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'lime', 'pink',
        'teal', 'lavender', 'brown', 'beige', 'maroon', 'turquoise', 'olive', 'hotpink', 'navy', 'grey',
        'black', 'white', 'crimson', 'turquoise', 'indigo', 'silver', 'gold', 'violet', 'tan', 'rosybrown']
    # Extract customer coordinates
    x_coords = [customer.x_coordinate for customer in customers]
    y_coords = [customer.y_coordinate for customer in customers]

    # Plot customers
    plt.scatter(x_coords, y_coords, color='blue')

    # Plot depot
    depot_x = customers[0].x_coordinate  # First route, first customer
    depot_y = customers[0].y_coordinate
    plt.scatter(depot_x, depot_y, color='gold', label='Depot')

    # Plot routes
    for i, route in enumerate(routes):
        route_x = [depot_x] + [customers[customer].x_coordinate for customer in route] + [depot_x]
        route_y = [depot_y] + [customers[customer].y_coordinate for customer in route] + [depot_y]
        plt.plot(route_x, route_y, marker='o', color=colors[i])

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Customer Locations and Routes')
    plt.legend()
    plt.grid(True)
    # Extract directory name from filename
    directory_name = filename.split('.')[0]
    assets_directory = os.path.join('assets', directory_name)
    # Create directory if it doesn't exist
    os.makedirs(assets_directory, exist_ok=True)
    # Save plot image
    plt.savefig(os.path.join(assets_directory + "/" + filename))
    plt.cla()
    plt.close()