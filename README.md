CCM
=========
# Pandas Large Data Set Processing

This is a python script that processes data for CCM.

Runs in --- ~120 to ~160 seconds ---
with MacbookPro 2.9 GHz Intel Core i5

# Setup:

Clone:
```
git clone https://github.com/aaronchu415/CCM.git
```

Use Virtual Environment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 script2.py
```

OR (if you have pandas and numpy installed correctly):
```
python3 script2.py
```

# Time Complexity:

TIME COMPLEXITY ANALYSIS:

SCRIPT RUNS IN O(nlogn) time complexity

* STEP 1. Presort the data frame. - O(nlogn).
        Explanation: df.sort_values uses quick sort per documentation
* STEP 2. Compute length, same_stock, start, end, columns - O(n)
        Explanation: We go through the rows 4 * n times
* STEP 3. Filter. - O(n)
        Explanation: We go through the rows n times to filter
* STEP 4. Sort final output. - O(nlogn).
        Explanation: df.sort_values uses quick sort per documentation
