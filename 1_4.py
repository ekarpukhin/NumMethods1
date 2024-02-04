acc = 4
ns = [10, 100, 1000, 10000, 100000]
sums = []
errors = []
digits_arr = []

for N in ns:
    s = sum([48/(5*(n*n+6*n+8)) for n in range(N+1)])
    sums.append(s)
    error = abs(acc-s)
    errors.append(error)
    digits = 1
    num = 1
    while(num>error):
        num *= 0.1
        digits+=1
    digits_arr.append(digits)
    print(s)

# plt.hist(errors)
# plt.show()
plt.hist(digits_arr)
plt.show()