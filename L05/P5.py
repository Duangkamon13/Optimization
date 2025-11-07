import numpy as np
from scipy.optimize import minimize

def Loss(Location, Bases, Distances):
  
    P = np.asarray(Location, dtype=float).reshape(1, 2)
    B = np.asarray(Bases, dtype=float)
    D = np.asarray(Distances, dtype=float).reshape(-1, 1)

    diff = B - P          
    sq_d = np.sum(diff * diff, axis=1, keepdims=True)  
    eps = sq_d - (D * D)  
    return float(np.sum(eps * eps))

def argmin_loss(Bases, Distances):
    B = np.asarray(Bases, dtype=float)
    D = np.asarray(Distances, dtype=float).reshape(-1, 1)

    x0 = np.mean(B, axis=0)  

    def obj(v):
        return Loss(v.reshape(1, 2), B, D)

    res = minimize(obj, x0=x0, method="BFGS")
    if not res.success:
        
        res2 = minimize(obj, x0=x0, method="Nelder-Mead", options={"maxiter": 2000})
        if res2.success and obj(res2.x) <= obj(res.x):
            return res2.x.astype(float)
        return (res2.x if obj(res2.x) <= obj(res.x) else res.x).astype(float)
    return res.x.astype(float)


if __name__ == '__main__':
    BRef = np.array([[100, 0], [100, 100], [0, 100],
    [0, 0], [-20, 50]])
    gt = np.array((30, 70)).reshape((1,2))
    # The distance
    D = np.sqrt(np.sum( (BRef - gt)**2, axis = 1 )).reshape(-1,1)
    P = np.array([30, 70])
    print(Loss(P, BRef, D))
    P = np.array([31, 71])
    print(Loss(P, BRef, D))
    P = np.array([29, 70])
    print(Loss(P, BRef, D))
    print(f"Location = {argmin_loss(BRef, D)}")
    # Test 2
    gt = np.array((15, 40)).reshape(1,2)
    D = np.sqrt(np.sum( (BRef - gt)**2, axis = 1 )).reshape(-1,1)
    print (f"Location = {argmin_loss(BRef, D)}))