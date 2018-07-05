import pickle
import numpy as np

def read_t(t=0.25, root="./"):
    if t > 0:
        data = pickle.load(open(root+'Ising2DFM_reSample_L40_T=%.2f.pkl'%t,'rb'))
    else:
        data = pickle.load(open(root+'Ising2DFM_reSample_L40_T=All.pkl','rb'))
    return np.unpackbits(data).astype(int).reshape(-1,1600)

stack = []
for t in np.arange(0.25,4.01,0.25):
    stack.append(read_t(t))

X = np.vstack(stack)
pickle.dump(np.packbits(X), open('Ising2DFM_reSample_L40_T=All.pkl','wb'))
