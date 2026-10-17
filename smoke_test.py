from experiment import compare
a=compare(3650,34678,5469,35211,draws=2000)
b=compare(3650,34678,5469,35211,draws=2000)
assert a==b and .049<a['difference']<.051
assert a['difference_normal_95_interval'][0]>0
assert a['right_tail_adjusted_p']>0
try:compare(5,4,1,2)
except ValueError:pass
else:raise AssertionError('Invalid counts accepted')
print('Effect direction, seeded simulation, positive Monte Carlo correction, and invalid-count checks passed.')
