# %%
import sys
import os
import matplotlib.pyplot as plt
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

import textwrap
import pandas as pd
from pandasai import SmartDatalake
from pandasai import SmartDataframe
import json 

#python -m pip install matplotlib

def store_as_csv(table_out, file_name):
    
    TESTDATA = StringIO(table_out)
    df = pd.read_csv(TESTDATA , sep=";")
    df.to_csv(file_name, sep='\t', encoding='utf-8')

    return df

def save_file(table_out , output_path , impact , subject, format_file):
  
  if format_file == '.csv':
    file_name = output_path + '/' + 'summarize_' +  str(impact) + '__' +  str(subject) + '.csv'
    _ = store_as_csv(table_out, file_name)

  return True

# %%
