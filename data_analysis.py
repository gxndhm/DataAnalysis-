from dask.distributed import Client
import time
import pandas as pd
from sklearn.linear_model import LinearRegression

# --- PART 1: THE DASK PARALLEL TEST ---
# This is for Section 3.1 of the report to see how fast 1 vs 10 vs 20 workers are
def check_speed(num_workers):
    # Fire up the parallel engine
    client = Client(n_workers=num_workers)
    
    start = time.time()
    
    # Using a simple mean calculation to test the speed on the big file
    # (Using the df_clean from the first script)
    avg_home = df_clean['Population Staying at Home'].mean().compute()
    
    end = time.time()
    client.close()
    return end - start

# I'll run these and put the seconds into my report table
print(f"Time for 1 worker: {check_speed(1):.2f}s")
print(f"Time for 10 workers: {check_speed(10):.2f}s")
print(f"Time for 20 workers: {check_speed(20):.2f}s")

# --- PART 2: THE REGRESSION (Section 3.2) ---
# Switching to the smaller file for the machine learning part
df_small = pd.read_csv('Trips_Full Data.csv')

# Predicting trip frequency based on distance
X = df_small[['Trips 1-25 Miles']]
y = df_small['Number of Trips 5-10']

model = LinearRegression().fit(X, y)
print(f"Model R-squared is: {model.score(X, y):.4f}")
