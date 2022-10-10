'''
Ms. Pan's comments:

- Use plt.title, xlabel, ylabel(); the title was small and uncentered.
- Changed annotate coordinates, for more spacing, was cramped before.
- Technically I wanted sample_number and n to be defined at the top.
- See comments throughout code. Remember to space arguments for methods.
- Not every comment I added is strictly necessary, but some are more than others.
  E.g. "Count 'yes' and 'no'" since loops are harder to parse.
'''


'''
Daniel Hua 9/29/22 Pyplot Histogram

'''
from pandas import read_csv
import matplotlib.pyplot as plt
from random import seed, sample    # Condensed into one line.
import statistics


seed(1)

def statkey(sample_number, n): # Added space here
    """
    It is always good to write comments for a function.
    It seems this 'docstring' format is the standard, but you just need
    to tell people what the function does, especially for one as specific and
    complex as this one.
    
    Replicates Statkey sampling distribution for sample proportion.
    Takes sample_number samples of size n and plots the data on a histogram.
    """

    lst = []
    
    # Import data from .csv and convert to list
    filename = "pets.csv"
    data = read_csv(filename, header = None)
    data = data[0].values.tolist()
    
    # Random sampling    
    for i in range(sample_number):
        yes_count = 0
        no_count = 0
        samp = sample(data, k=n)
        
        # Count 'yes's and 'no's in the sample
        for j in samp:
            if j == 'yes':
                yes_count += 1
            else:
                no_count += 1
        
        # Calculate and record sample proportion
        proportion = (yes_count / (yes_count + no_count))
        lst.append(proportion)
        
    # Calculate mean and std error for the sampling distribution
    mean = statistics.mean(lst)
    pstdev = statistics.pstdev(lst)

    print("The mean is", mean)
    print("The standard error is", pstdev)
    
    # Plot all samples on a histogram
    plt.hist(lst, edgecolor='black')

    plt.title("Pets Histogram")
    plt.xlabel("Percentage of Yes Answers")
    plt.ylabel("Frequency")

    # Apparently, keywords don't require spaces around the =; just mentioning.
    plt.annotate("n =  {}".format(n), xy=(.05,.9), xycoords='axes fraction')
    plt.annotate("samples =  {}".format(sample_number), xy = (.05,.85), xycoords = 'axes fraction')
    plt.annotate("mean =  {}".format(round((mean),2)), xy = (.7,.9), xycoords = 'axes fraction')
    plt.annotate("pstdev =  {}".format(round((pstdev),2)), xy = (.7,.85), xycoords = 'axes fraction')    

    plt.show()

# Default: Generates sampling distribution for 1000 samples of size 30.
statkey(1000, 30)




