# 1.10

def get_mxs(delta):
    arr = list(itertools.product((1+delta, 1-delta), repeat=9))
    mxs = map(lambda a: [[*a[0:3]], [*a[3:6]], [*a[6:9]]], arr)
    return mxs

A = np.array([[9, 17, 1],[27, 35, -18], [6, 14, 4]])

# delta = 0.5
mxs = get_mxs(0.5) 
min_det = 1000000
max_det = -1000000
for mx in mxs:
    newmx = np.multiply(A,mx)
    max_det = max(max_det, np.linalg.det(newmx))
    min_det = min(min_det, np.linalg.det(newmx)) 
print(min_det, max_det)

# delta = 0.1

mxs = get_mxs(0.1)
min_det = 1000000
max_det = -1000000

for mx in mxs:
    newmx = np.multiply(A,mx)
    max_det = max(max_det, np.linalg.det(newmx))
    min_det = min(min_det, np.linalg.det(newmx)) 
print(min_det, max_det)