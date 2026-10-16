string = '''
In solver.py implement the m=8 branch as a function solve_m8(runner, families):
- Hypotheses: perm (D={0}), simon (D={0,s}, 255 candidates), simon2 (D=H, all 10795 two-dimensional subspaces of F_2^8, enumerated at import time). Priors uniform over the families present in `families`, uniform over candidates within each family.
- Likelihood for a measured string y' under hidden set D, with misfire rate mu and readout flip rate q:
  P(y'|D) = (1/256) * [ mu*G(y') + (1-mu)*sum_{u in D} (1-2q)^{|u|} * (-1)^{u.y'} ]
  where G(y') = sum over all 256 u of (1-2q)^{|u|} * (-1)^{u.y'} and |u| is the Hamming weight. Precompute the 256x256 sign matrix and weights with numpy and vectorise over candidates.
- Collect Simon samples in small batches (e.g. 4-6 shots per run call), update log-likelihoods, compute marginal likelihood per family (average over candidates, in log-space with scipy.special.logsumexp), and the posterior over (family, secret).
- Stop when the top posterior mass exceeds 0.995 (family and secret jointly; for perm just the family), or when the budget is exhausted. Return the family and the MAP secret (simon: s; simon2: sorted list of the three nonzero elements of H).
- Parameterise mu and q as arguments (defaults 0.04 and 0.02) so that they can be estimated later.
Write tests/test_m8.py: for 100 random oracles per family at nominal noise, report accuracy and mean queries used per family. Do not assert thresholds yet, just print a table.
'''
v_count = 0
c_count = 0
d_count = 0
s_count = 0

for i in string:
    if i.lower() in {'a', 'e', 'i', 'o', 'u'}:
        v_count += 1
    elif i.lower().isalpha():
        c_count += 1
    elif i.isnumeric():
        d_count += 1
    else:
        s_count += 1
print(f"Vowels count = {v_count}")
print(f"Consonants count = {c_count}")
print(f"Digits count = {d_count}")
print(f"Special count = {s_count}")