
"""
Spring 2020 DSP 539: Assignment 4 Python

Author by: Anusha Singamaneni

This script should be run using the command line, outputs the linguistic complexity of each sequence in a file of sequences. 
The sequence file should be passed by the end user as a command line argument.

Usage: python lgstc_comlx_sequence.py <filename.txt>
"""

import pandas as pnds
import sys 
import matplotlib.pyplot as pyplt

def obsrvdkmerCount(Seq,k):
    """
    Summary : Counts the number of observed kmers for a sequence, for a specific k value
    
    Description: This function takes k and a sequence Seq as input arguments and determines the number of observed k-mers 
    for a particular k-value
    
    Aurgments/variables: 
    Seq: the input sequence for which the k-mers need to be determined
    k: the input value, ranges from 1 to length of sequence 
    
    Return:the number of kmers observed
    """
    lk_pos = []
    for i in range(0,len(Seq)-k+1):
        lk_pos.append(Seq[i:i+k])

    lk_obs = list(set(lk_pos))
    return len(lk_obs)

def psblekmerCount(Seq,k):
    """
    Summary : Counts the number of possible kmers for a sequence, for a specific k value
    
    Description: This function takes k and a sequence Seq as input arguments and determines the number of possible/expected k-mers 
    for a particular k-value
    
    Aurgments/variables: 
    Seq: the input sequence for which the number of k-mers need to be determined
    k: the input value, ranges from 1 to length of the sequence 
    
    Return:the number of kmers possible
    """
    
    lk_pos = [] #ls_pos is list variable
    if k == 1:
        return 4;
    else:
        for i in range(0,len(Seq)-k+1):
            lk_pos.append(Seq[i:i+k])
            
        return len(lk_pos)
    
def create_kmer_df(Seq):
    """
    Summary : Creates a data frame with k values, observed number of kmers and possible number of kmers as columns. 
    
    Description: This function takes a sequence Seq as input argument and returns a pandas data frame 
    which has columns k value, observed kmer count and possible kmer count.
        
    Aurgments/variables: 
    Seq: the input sequence for which the kmer data frame needs to be created
    
    Return:
    kmer_df: kmer data drame
    """
    #import pandas as pnds
    k = []
    k_pos_list = []
    k_obs_list = []
    k = list(range(1,len(Seq)+1))
    
    for i in k:
        k_pos = psblekmerCount(Seq,i)
        k_pos_list.append(k_pos)
    
    for i in k:
        k_obs = obsrvdkmerCount(Seq,i)
        k_obs_list.append(k_obs)
    
    kmer_df = pnds.DataFrame(     # create the data frame
    {
         'k':k,
         'Observed kmers':k_obs_list,
         'Possible kmers':k_pos_list
    }
    )
    return kmer_df

def plot_kmer_prop(Seq):
    """
    Summary : Creates a graph for proportion of each observed kmer
    
    Description: This function takes a sequence Seq as input argument and produces a plot for the proportion of each observed kmers 
    with respect to the number of possible kmers
        
    Aurgments/variables: 
    Seq: the input sequence for which the kmer proportion graph needs to be created
    
    Return:
    None
    """
    
    
    kmer_df = create_kmer_df(Seq)
    kmer_prop = kmer_df['Observed kmers']/kmer_df['Possible kmers'] # calculate the kmer proportion
    pyplt.plot(kmer_df['k'],kmer_prop)
    pyplt.title('Proportion of Observed kmers')
    pyplt.xlabel('k value')
    pyplt.ylabel('Observed/Possible kmers')
    pyplt.show()
    
def linguistic_complexity(Seq):
    """
    Summary : Calculates the lingusitic complexity of a given sequence
    
    Description: This function takes a sequence Seq as input argument and produces the linguistic complexity, 
    the proportion of k-mers that are observed compared to the total number that are theoretically possible
        
    Aurgments/variables: 
    Seq: the input sequence for which the linguistic complexity needs to be determined
    
    Return:
    lc: linguistic complexity
    """
    
    kmer_df = create_kmer_df(Seq)
    tot_obs_kmer = sum(kmer_df['Observed kmers'])
    tot_pos_kmer = sum(kmer_df['Possible kmers'])
    lc = tot_obs_kmer/tot_pos_kmer
    return lc

if __name__=='__main__':
    
    myfile = sys.argv[1]
    with open(myfile,'r') as current_file:
        text = current_file.read()
    seq = text.split() # split sequences
    for i in range(0,len(seq)):
        #print(seq[i])
        lc_seq = linguistic_complexity(seq[i])
        print(lc_seq) # prints the linguistic complexity
        plot_kmer_prop(seq[i]) # Plots kmer proportion
