from pathlib import Path
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
})

path = Path('data.parquet')
df.to_parquet(path=path, index=False, compression='snappy')

print(pd.read_parquet(path))

print(pd.read_parquet(path, columns=['name', 'age']))