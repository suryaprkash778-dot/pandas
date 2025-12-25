import pandas as pd
left = pd.DataFrame({
    'a': ['a0', 'a1', 'a2', 'a3'],
    'b': ['b0', 'b1', 'b2', 'b3']
})

right = pd.DataFrame({
    'c': ['c4', 'c5', 'c6', 'c7'],
    'd': ['d4', 'd5', 'd6', 'd7']
})

newdf = left.join(right, how='outer')
print(newdf)
