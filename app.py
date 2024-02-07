##################################################################
# Brian Lesko 
# 12/2/2023
# Robotics Studies, RRT Search
# Rapidly exploring Random Tree

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import customize_gui # streamlit GUI modifications
import robot
import rrt as RRT
gui = customize_gui.gui()
my_robot = robot.two2_robot()

def halton(index, base):
    fraction = 1
    result = 0
    while index > 0:
        fraction /= base
        result += fraction * (index % base)
        index = index // base  # floor division
    return result

def generate_halton_points(n, m):
    # List of the first few prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887]
    points = []
    for i in range(1, n + 1):
        point = []
        for j in range(m):
            point.append(halton(i, primes[j]))
        points.append(point)
    return points

def main():
    # Set up the app UI
    gui.clean_format(wide=True)
    Sidebar = gui.about(text = "This code implements the [Halton Sequence](https://en.wikipedia.org/wiki/Halton_sequence)")
    Title, image_spot = st.empty(), st.columns([1,5,1])[1].empty()
    fig, ax = my_robot.get_colored_plt("#F6F6F3",'#335095','#D6D6D6')
    my_robot.set_c_space_ax(ax)
    title = "<span style='font-size:30px;'>Halton Sequence:</span>"
    subtitle = "<span style='font-size:20px;'>Uniform Random Points</span>"
    with Title: st.markdown(f" {title} &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{subtitle} &nbsp; &nbsp; &nbsp; ", unsafe_allow_html=True)

    # Generate Halton points
    n = 3333
    points = generate_halton_points(n, 2)
    points = (np.transpose(points)-.5)*12

    # Create a colormap
    cmap = plt.get_cmap('Blues')
    start = 0.2
    stop = 1.0
    colors = cmap(np.linspace(start, stop, cmap.N))
    cmap = mcolors.LinearSegmentedColormap.from_list('Upper Half', colors)
    # Calculate colors for each point
    colors = [cmap(i**5) for i in np.linspace(0, 1, n)]

    # plot all the points
    # ax.scatter(points[0], points[1], c=colors)

    # Plot points in batches of size p
    p = 111
    for i in range(0, n, p):
        batch_points = points[:, i:i+p]
        batch_colors = colors[i:i+p]
        ax.scatter(batch_points[0], batch_points[1], c=batch_colors)

        # Display the current state of the plot
        with image_spot: 
            st.pyplot(fig)

    # Display the final result
    with image_spot: st.pyplot(fig)

main()