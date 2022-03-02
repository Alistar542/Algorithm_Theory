import numpy as np

def reachability():
    # Initialize the variables
    ap = np.identity(5)
    a = createGraph()
    r = np.zeros((5,5))
    prev_r = np.ones((5,5))
    iter = 0
    while isNotConverged(prev_r,r):
        prev_r = r
        # Matrix mulitplication Ap with A
        ap = np.matmul(ap,a)
        # Does Logical OR operation on R and Ap
        r = np.logical_or(r,ap)
        # Converts the result into 1 and 0 instead of True and False 
        r = r.astype(np.int32)
        # Extra check to prevent from printing the last time
        if isNotConverged(prev_r,r):
            iter += 1
            print("Iteration No : ",iter)
            print(r)
    print("Connected Component")
    # Does logical AND on R and R Transpose for finding the connected components
    cc = np.logical_and(r, r.transpose())
    cc = cc.astype(np.int32)
    print(cc)

# Method that returns the adjacency matrix for a given graph
def createGraph():
    a = np.array([[0,1,0,0,1],[0,0,1,0,0],[0,0,0,1,0],[0,1,0,0,0],[1,0,0,0,0]])
    return a

# Method to check if the matrix has converged
# Returns True if the method has not converged and False otherwise
def isNotConverged(prev_r,r):
    return np.any(np.not_equal(prev_r,r))


reachability()
