import pandas as pd

#pd.Series()
series1=pd.Series([1,2,3,4])
print("Using pd.Series()")
print(series1,"\n")

series1=pd.Series([1,2,3,4],index=["w","x","y","z"])
print("Using pd.Series() with index")
print(series1,"\n")

#pd.DataFrame()
data={"calories":[420,380,390],"duration":[50,40,45]}
df=pd.DataFrame(data)
print("Using pd.DataFrame()")
print(df,"\n")

#df.loc()
print("Using df.loc()")
print(df.loc[0],"\n")
print(df.loc[[0,1]],"\n")

#pd.read_csv()
df=pd.read_csv('data.csv')
print("Using pd.read_csv()")
print(df.to_string(),"\n")

#pd.read_json()

#df.dropna()
newdf=df.dropna()
print("Using df.dropna()")
print(newdf,"\n")

#df.drop_duplicates()
print("Using df.drop_duplicates()")
newdf=df.drop_duplicates()
print(newdf,"\n")

#df.corr()
print("Using df.corr()")
print(df.corr(),"\n")

#df.info()
print("Using df.info()")
print(df.info(),"\n")

#df.head()
print("Using df.head()")
print(df.head(),"\n")

#df.tail()
print("Using df.tail()")
print(df.tail(),"\n")
