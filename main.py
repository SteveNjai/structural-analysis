#Matrix ethod of structural analysis
#It computes the discpacement and the forces and the monents of various elements

#import modules
import numpy as np
import sys
import datetime

def main():
    # store reference of original standard output as variable
    original_stdout = sys.stdout

    #import files
    file_stiffness = 'stiffness.txt'
    file_joint_load = 'joint_load.txt'
    file_member_reaction = 'member_reaction.txt'
    file_force_matrix = 'force_matrix.txt'

    # import the stiffness matrix file delimited using a tab.
    stiffness_k = np.loadtxt(file_stiffness, delimiter='\t', comments='#', skiprows=1)
    joint_load = np.loadtxt(file_joint_load, delimiter='\t', comments='#',skiprows=1)
    member_reaction = np.loadtxt(file_member_reaction, delimiter='\t', comments='#', skiprows=1)
    force_matrix = np.loadtxt(file_force_matrix, delimiter='\t', comments='#', skiprows=1)

    # sum up the member reaction matrix
    member_reaction_sum = np.sum(member_reaction, axis = 1)

    #generate combined load matrix equal to joint load  minus member reaction
    combined_load_matrix = np.subtract(joint_load, member_reaction_sum)

    #revise the stiffness matrix depending on the force matrix
    revised_stiffness_k_1 = np.arange(stiffness_k.size).reshape(stiffness_k.shape)
    for i in revised_stiffness_k_1:
        revised_stiffness_k_1[i] = force_matrix

    revised_stiffness_k_2 = np.transpose(revised_stiffness_k_1)
    revised_stiffness_k = np.multiply(revised_stiffness_k_1,revised_stiffness_k_2)



    #solve [revised stiffness matrix]*[k]*[D] = [F] to get displacement matrix [D].
    new_stiffness_k = np.multiply(revised_stiffness_k, stiffness_k)


    # modify stifness matrix by deleting all zero rows and oclumns
  #  for i in new_stiffness_k:
  #      if np.all(np.multiply(i,i) == 0):
  #          print('\n i is\n', i)
   #         modified_stiffness_k = np.delete(new_stiffness_k, 0 , axis = 0)

   # SOLVE THE STIFFNESS EQUATIONS
    if np.linalg.det(new_stiffness_k) != 0:
        displacement_matrix_D = np.linalg.solve(new_stiffness_k, combined_load_matrix)

        # check if solution is correct
        if np.allclose(np.dot(new_stiffness_k, displacement_matrix_D),combined_load_matrix):
            displacement_matrix = displacement_matrix_D

            # calculate reactions
            reaction_matrix = np.subtract(
                np.dot(new_stiffness_k, displacement_matrix), combined_load_matrix)

            #Print values for the deflections and the reactions
            print('\n Displacement matrix \n', displacement_matrix)
            print('\n Reaction matrix \n', reaction_matrix)

        else:
            print("\n No solution found for displacement matrix \n")


    else:
        print("\n The stiffness matrix is a singular matrix. Could not solve. Modify the force matrix\n")

    # PRINT VALUES
    # PRint header
    print('---------------OUTPUT-----------------')
    now = datetime.datetime.now()
    print('\n Calculated on date and time: ')
    print(now.strftime("%Y-%m-%d | %H:%M:%S"))
    print('\nThe following is the input data\n')
    # Print values
    print('\nstiffness matrix K\n', stiffness_k)
    print('\njoint load Aj \n', joint_load)
    print('\nmember reaction \n', member_reaction)
    print('\n force matrix \n', force_matrix)

    print('\n---------------------RESULTS----------------')
    print(' \n summed member reaction Ar\n', member_reaction_sum)
    print('\n combined load matrix Ac = Aj - Ar \n', combined_load_matrix)
    print('\n stiffness force matrix \n', revised_stiffness_k)
    print('\n new stiffness matrix \n', new_stiffness_k)
    print('\n # |---------------------------------------------------------')
    print("""
    \n # | This program is designed by Stephen Njai N and reuires Python 3.
    \n # | This program utilizes the following modules: sys, numpy, datetime.
    \n # | This program is meant to run fro the command line or a python IDE such as pycharm.
    \n # | For any questions, reach out on njorogenjai11@gmail.com
    \n # |---------------------------------------------------------------------------------------|
    
    """)


    # write results to file by overwritting previous results
    with open('output.txt', 'w') as output:
        #set stdout to file object
        sys.stdout = output
        now = datetime.datetime.now()

        #PRint header
        print(""" # |-------------------------------------------------------------------------------
        \n # |          STIFFNESS MATRIX METHOD OF STRUCTURAL ANALYSIS : RESULTS OUTPUT
        \n # | Calculated on date and time: 
        \n $ | """, now.strftime("%Y-%m-%d | %H:%M:%S"),"""
        \n # | The following program calculates the deflection and the reactions of structural members using the
        matrix method of structural analysis. Please use the corresponding input text files to input your data 
        before running this program in your command prompt or Python IDE. The input text files are the: stiffness.txt,
        joint load.txt, member reaction.txt and force matrix.txt.
        \n $ |-------------------------------------------------------------------------------------------------
        """
        )
        print('\nThe following is the input data')

        # Print values
        print('\nstiffness matrix K\n', stiffness_k)
        print('\njoint load Aj \n', joint_load)
        print('\nmember reaction \n', member_reaction)
        print('\n force matrix \n', force_matrix)

        print('\n---------------------RESULTS----------------')
        print(' \n summed member reaction Ar\n', member_reaction_sum)
        print('\n combined load matrix Ac = Aj - Ar \n', combined_load_matrix)
        print('\n stiffness force matrix \n', revised_stiffness_k)
        print('\n new stiffness matrix \n', new_stiffness_k)

        # Print values for the deflections and the reactions
        # SOLVE THE STIFFNESS EQUATIONS
        if np.linalg.det(new_stiffness_k) != 0:
            displacement_matrix_D = np.linalg.solve(new_stiffness_k,
                                                    combined_load_matrix)

            # check if solution is correct
            if np.allclose(np.dot(new_stiffness_k, displacement_matrix_D),
                           combined_load_matrix):
                displacement_matrix = displacement_matrix_D

                # calculate reactions
                reaction_matrix = np.subtract(
                    np.dot(new_stiffness_k, displacement_matrix),
                    combined_load_matrix)

                # Print values for the deflections and the reactions
                print('\n Displacement matrix \n', displacement_matrix)
                print('\n Reaction matrix \n', reaction_matrix)

            else:
                print("\n No solution found for displacement matrix \n")


        else:
            print(
                "\n ERROR! The stiffness matrix is a singular matrix. Could not solve. Modify the force matrix\n")

            #summarizing the file
        print('\n # |---------------------------------------------------------')
        print("""
           \n # | This program is designed by Stephen Njai N and reuires Python 3.
           \n # | This program utilizes the following modules: sys, numpy, datetime.
           \n # | This program is meant to run fro the command line or a python IDE such as pycharm.
           \n # | For any questions, reach out on njorogenjai11@gmail.com
           \n # |---------------------------------------------------------------------------------------|

           """)

        output.close()  #close the output file
        sys.stdout = original_stdout    #resume normal standard output

#call the main function
if __name__ == '__main__':
    main()