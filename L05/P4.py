import numpy as np
from scipy.optimize import minimize

def z(f, r, R):
  if f <= 0:
    return np.inf

  term1 = 1 / np.sqrt(f)
  term2 = 2 * np.log10((r / 3.7) + (2.51 / (R * np.sqrt(f))))
  return term1 + term2

def solve_colebrook(r, R):
  f0 = 0.0370379
  result = minimize(lambda f: z(f, r, R)**2, f0, bounds=[(1e-6, None)])
  return result.x[0]

if __name__ == '__main__':
  r = 0.0001476
  R = 132080.0
  fo = solve_colebrook(r, R)
  print(f'f = {fo} ; z(f) = {z(fo, r, R)}')