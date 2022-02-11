#Matrix ethod of structural analysis
#It computes the discpacement and the forces and the monents of various elements

#import modules
import math
import numpy as np
import pandas as pd


def main():
    # import the txt nodes.txt file delimited using a tab.
    # syntax of file is: Node name, X position, Y position, Z position. All positions in metres in global space.
    file = np.loadtxt('nodes.txt', delimiter='\t', comments='#', skiprows=1)
    print(file)
    print(file[:, 1])
    print(np.transpose(file[:, 1]))

    # the first row removes the node numbers by multiplying them with zero
    data = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(data)
    new = np.dot(file, data)
    print(new)

    # define the variables

    # output results
    output_results = str(file)
    # write results to file by overwritting previous results
    output_file = open('output.txt', 'w')
    output_file.write(output_results)
    output_file.close()


if __name__ == '__main__':
    main()