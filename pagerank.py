import numpy as np
from scipy.sparse import csc_matrix, coo_matrix
import re



def pageRank(G, s = .85, maxerr = .001):
    """
    Computes the pagerank for each of the n states.
    Used in webpage ranking and text summarization using unweighted
    or weighted transitions respectively.
    Args
    ----------
    G: matrix representing state transitions
       Gij can be a boolean or non negative real number representing the
       transition weight from state i to j.
    Kwargs
    ----------
    s: probability of following a transition. 1-s probability of teleporting
       to another state. Defaults to 0.85
    maxerr: if the sum of pageranks between iterations is bellow this we will
            have converged. Defaults to 0.001
    """
    
    n=78
  

    with open(G) as f:
        taxi=[line.strip().split(',') for line in f.readlines() if line ]
            
        taxinum=taxi[1:]
        newrow=[item[0] for item in taxinum]
        newcolumn=[item[1] for item in taxinum]
        newdata=[item[2] for item in taxinum]
        
        
        row1=["0" if x =='' else x for x in newrow]
        column1=["0" if x =='' else x for x in newrow]
        data1=["0" if x =='' else x for x in newrow]

        rowa=np.array(row1)
        
        columna=np.array(column1)
        dataa=np.array(data1)

        row2=[int(x) for x  in rowa]
        column2=[int(x) for x  in columna]
        data2=[int(x) for x  in dataa]
            

    M=coo_matrix((data2,(row2,column2)), shape=(78,78)).tocsc()
    #M = matrix.tocsc()
    # transform G into markov matrix M
    #M = csc_matrix(G,dtype=np.float)
    rsums = np.array(M.sum(1))[:,0]
    ri, ci = M.nonzero()
    M.data = M.data / rsums[ri]

    # bool array of sink states
    sink = rsums==0

    # Compute pagerank r until we converge
    ro, r = np.zeros(n), np.ones(n)
    while np.sum(np.abs(r-ro)) > maxerr:
        ro = r.copy()
        # calculate each pagerank at a time
        for i in xrange(0,n):
            # inlinks of state i
            Ii = np.array(M[:,i].todense())[:,0]
            # account for sink states
            Si = sink / float(n)
            # account for teleportation to state i
            Ti = np.ones(n) / float(n)

            r[i] = ro.dot( Ii*s + Si*s + Ti*(1-s) )

    # return normalized pagerank
    return r/sum(r)




if __name__=='__main__':
    # Example extracted from 'Introduction to Information Retrieval'
    G = "chicago-taxi-rides.txt"

    print(pageRank(G,s=.86))