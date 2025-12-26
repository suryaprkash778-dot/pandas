import pandas as pd
import numpy as np
df = pd.DataFrame(
    {
        'a':['foo','foo','foo','bar','bar','bar'],
        'b':['one','one','two','two','one','one'],
        'c':['x','y','x','y','x','y'],
        'd':[1,3,2,5,4,1]
    },
)

# pivot table
print(df.pivot_table(values='d',index=['a','b'],columns='c'))





>>>"C:\Users\Surya Prakash\PythonProject\numpy arrays\.venv\Scripts\python.exe" "C:\Users\Surya Prakash\PythonProject\numpy arrays\main.py" 
c          x    y
a   b            
bar one  4.0  1.0
    two  NaN  5.0
foo one  1.0  3.0
    two  2.0  NaN

Process finished with exit code 0
