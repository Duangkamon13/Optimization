import numpy as np

import numpy as np

class Face:
    def __init__(self, A, B, C, col=(128,128,128)):
        '''
        A, B, C are vertices of the face,
        in order of counter clockwise to the out normal vector.
        Each vertex is a np.array of shape (3,).
        '''
        self.A = A
        self.B = B
        self.C = C
        self.color = col
        # Determine the normal vector
        # Dummy. Write your code here!
        # --- make sure they are numpy arrays ---
        self.A = np.array(self.A, dtype=float)
        self.B = np.array(self.B, dtype=float)
        self.C = np.array(self.C, dtype=float)
        # n = ((B-A) x (C-A)) / ||(B-A) x (C-A)||
        n_unnorm = np.cross(self.B - self.A, self.C - self.A)
        n_len = np.linalg.norm(n_unnorm)
        if n_len == 0:
            self.normal = np.array([0.0, 0.0, 0.0])  # degenerate triangle
        else:
            self.normal = n_unnorm / n_len

    def ray(self, O, V):
        # Dummy. Write your code here!
        O = np.array(O, dtype=float)
        V = np.array(V, dtype=float)
        n = self.normal
        d = V - O
        eps = 1e-9

        # Step 2. Formulate the plane equation.
        # n.T @ p = k where k = n.T @ A where p is a point on the plane
        k = n @ self.A

        # Step 3. Compute the parametric t for the intersection
        denom = n @ d
        if abs(denom) < eps or not np.isfinite(denom):
            return np.inf
        t = (k - n @ O) / denom
        if t < 0:
            return np.inf

        # Step 4. Determine if the intersection lies
        # within the face boundaries
        # The intersection point Q
        Q = O + t * d

        # Test the boundaries
        # Q inside if { (B-A)x(Q-A) }·n >= 0, { (C-B)x(Q-B) }·n >= 0, { (A-C)x(Q-C) }·n >= 0
        insideAB = (np.cross(self.B - self.A, Q - self.A) @ n) >= -eps
        insideBC = (np.cross(self.C - self.B, Q - self.B) @ n) >= -eps
        insideCA = (np.cross(self.A - self.C, Q - self.C) @ n) >= -eps

        if insideAB and insideBC and insideCA:
            return float(t)
        else:
            return np.inf

if __name__ == '__main__':
    f1 = Face(np.array((0, 20, 80)),
              np.array((-20, -10, 80)),
              np.array((20, -10, 80)),
              (240, 200, 100))

    O = np.array((0,0,0))

    V1 = np.array((-40, 0, 50))
    t = f1.ray(O, V1)
    print('t = {:.3f}'.format(t))   

    V2 = np.array((0, 0, 50))
    t = f1.ray(O, V2)
    print('t = {:.3f}'.format(t))   

