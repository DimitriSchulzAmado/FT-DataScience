import numpy as np
import pandas as pd

df = pd.DataFrame({"AAA": [6, 7, 8],
                   "BBB": [10, 11, 12],
                   "CCC": [-100, 50, 30]})

df_test01 = df
df_test02 = df
# if df.AAA >= 6: altere a coluna BBB para -1
df_test01.loc[df.AAA >= 6, "BBB"] = -1
df_test02.loc[df.AAA >= 7, ["BBB", "CCC"]] = 555

df_numpy = pd.DataFrame({"AAA": [4, 5, 6, 7],
                         "BBB": [10, 20, 30, 40],
                         "CCC": [100, 50, -10, -50]})

# cria uma coluna chamada logic e vai inserir high ou low de acordo com a operação
df_numpy["logic"] = np.where(df_numpy["AAA"] > 5, "high", "low")
print(df_numpy),
