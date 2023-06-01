from scipy import stats

hits = [23, 56, 87, 99, 43, 63, 78, 56, 56, 56, 56, 78, 78, 78]

x = stats.mode(hits, keepdims = False)

print(x)
