import pandas as pd 
from prices import wf_data, titles_text

#create dataframe for wf data
items = pd.DataFrame(wf_data, columns=['Item','Regular','Sale'])
print(items)

