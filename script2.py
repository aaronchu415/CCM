# load modules
import pandas as pd
import time

# log start time
start_time = time.time()

# load input data set (Python pickle file)
df = pd.read_pickle(r'px.xz')  # replace <path> with proper file path

# USER CODE

# TIME COMPLEXITY ANALYSIS:
# SCRIPT RUNS IN O(nlogn) time complexity

# STEP 1. Presort the data frame. - O(nlogn).
#         Explanation: df.sort_values uses quick sort per documentation
# STEP 2. Compute length, same_stock, start, end, columns - O(n)
#         Explanation: We go through the rows 4 * n times
# STEP 3. Filter. - O(n)
#         Explanation: We go through the rows n times to filter
# STEP 4. Sort final output. - O(nlogn).
#         Explanation: df.sort_values uses quick sort per documentation


# assumptions are that given data frame is pre sorted by bbgid and dt.
# if not we can sort it
PRE_SORTED = True

if not PRE_SORTED:
    df = df.sort_values(
        ['bbgid', 'dt'], ascending=[False, True])

# get time difference between current row and prev row
df['length'] = (
    df['dt'] - df['dt'].shift(1)) - pd.Timedelta(days=1)

# get bloomberg_id difference between current row and prev row
df['same_stock'] = (
    df['bbgid'] == df['bbgid'].shift(1))

# get start date for current row (start date is the prev row + 1 day)
df['start'] = (df['dt'].shift(1)) + pd.Timedelta(days=1)

# get end date for current row (end date is current row - 1 day)
df['end'] = (df['dt']) - pd.Timedelta(days=1)

TIME_GAP_EXIST = (df['length'].dt.total_seconds() > 1)
SAME_STOCK_AS_PREV_ROW = (df['same_stock'] == True)
# filter for only rows that have time gap and is same stock as prev row
# if different stock then we dont care about time gap
diff = df[TIME_GAP_EXIST & SAME_STOCK_AS_PREV_ROW]

# change timedelta object to integer
diff['length'] = pd.to_numeric(diff['length'].dt.days, downcast='integer')

# get only the columns we care about
stats = diff[['start', 'end', 'length', 'bbgid']]

# sort based on problem instructions
stats = stats.sort_values(
    ['length', 'bbgid', 'start'], ascending=[False, True, True])

# reset index
stats = stats.reset_index()
# drop old index
stats = stats.drop(['index'], axis=1)

print(stats.head(50))

# export result to Excel
# replace <path> with proper file path
stats.iloc[0:1000].to_excel(r'px_stats.xlsx')

# show execution time
print("--- %s seconds ---" % (time.time() - start_time))
