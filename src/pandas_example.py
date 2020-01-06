import pandas as pd
import PandasHelper as pdh
from PandasHelper import FileType
import re
import pandasql as pdsql


path = 'C:\\Users\\NickTsai\\Desktop\\PandaPractice\\pokemon_data.json'
path2 = 'C:\\Users\\NickTsai\\Desktop\\PandaPractice\\pokemon_data.xlsx'

df = pdh.read_file_as_datafram(file_path= path, file_type=FileType.Json)
dfs = pdh.read_file_as_datafram(file_path= path2, file_type=FileType.Excel)

# datafram filtering
    # contains
df2 = df.loc[(df['Type 1'] == 'Grass') & (df['Name'].str.contains('Mega'))]

    # not contains
df3 = df.loc[(df['Type 1'] == 'Grass') & (~df['Name'].str.contains('Mega'))]

# datafram index reset
df2.reset_index(drop=True, inplace=True)

# sorting
    # one condtion
df4 = df.sort_values(['Name'], ascending=False)
    # Multi condition sorting
df5 = df.sort_values(['Name','Type 1'], ascending=True)

# Regular expression
df6 = df.loc[(df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True))]
df7 = df.loc[(df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True))]

# Replacement 
    # those pokemon who's type2 is dragon, its legendary become 'True'
#df8 = df.loc[df2['Type 2'] == 'Dragon', 'Legendary'] = 'True'
    # fillna method can replace the value in df with Nan
    # in following case, will fill 0
df9 = dfs.fillna(0)
    # or customize from different field
df10 = dfs.fillna({
        'Name':0,
        'Type 1':'no tp1',
        'Type 2':'no tp2'
    })

    # fill the  blank from the last row value
df11 = df.fillna(method="ffill")
    # same as above, but copy value horizontally, from roght to left
df12 = df.fillna(method="ffill", axis='columns')
    # same as df11, but will only compy one time
df13 = df.fillna(method="ffill", limit=1)

    # drop the record which contain na value at any column
df14 = dfs.dropna()
    # drop the record if all column have no value in a row
df15 = dfs.dropna(how="all")
    # same as df15, but specify on the certain column
df16 = dfs.dropna(thresh=1)


# SQL Query
q1 = "select * from df left join dfs on df.[#] = dfs.[#] "
df17= pdsql.sqldf(q1, globals())


# Group by
    # group by the data first
        # one condition
df18_1 = df.groupby('Type 1')
        # two condition
df18 = df.groupby(['Type 1','Type 2'])
    # get mean regardind to the group by data
df19 = df18.mean()
    # get max regardind to the group by data
df20 = df18.max()


# Concat
df21 = pd.concat([df, dfs])
df22 = pd.concat([df, dfs], ignore_index=True)

    # add new columns to distingulish among input data
    # benifit is to locate the data. e.g.: df23.loc['T2'], will only show T2 data
df23 = pd.concat([df, dfs], keys=['T1', 'T2'])
    # append it as column if there is anything additional (remove the duplicated one)
df24 = pd.concat([df, dfs], axis=1)


# Merge
df25 = pd.merge(df, dfs,on='Name')
df26 = pd.merge(df, dfs,left_on='Name',right_on='Name')
df27 = pd.merge(df, dfs,left_on='Name',right_on='Name',how='outer')


# Pivot table
#print(df)
df28 = df.pivot_table(index='Type 1', columns='Type 2')
print(df28)

