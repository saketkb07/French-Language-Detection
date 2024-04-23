#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from langdetect import detect

def detect_language(text):
    try:
        return detect(text)
    except:
        return "400 Bad Request"

def detect_french(csv_file, outputfile):
    df = pd.read_csv(csv_file, encoding='utf-8')
    french_rows = []

    fifth_column = df.iloc[:, 4]

    for index, cell in fifth_column.items():
        language = detect_language(str(cell))
        if language == 'fr':
            french_rows.append(df.iloc[index])

    if french_rows:
        result_df = pd.DataFrame(french_rows)
        result_df.to_csv(outputfile, index=False)  # Corrected variable name here
        print("French text detected. Results written to", outputfile)
    else:
        print("Good news - No French text detected")

input_csv = 'Saket.csv'
outputfile = 'french_text_results.odt'
detect_french(input_csv, outputfile)


# In[ ]:




