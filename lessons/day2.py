import pandas as pd

dfs = pd.read_html( "https://en.wikipedia.org/wiki/Table_of_food_nutrients" )

df_dairy = dfs[0]
print(df_dairy)

df_next = dfs[1]
print(df_next)
