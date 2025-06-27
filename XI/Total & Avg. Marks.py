import pandas as pd
import matplotlib.pyplot as pl
S1=pd.Series(["bilal","raghav","het","naitik","dhruvil","mihir"])
S2=pd.Series([80,70,60,50,40,30])
S3=pd.Series([30,40,50,60,70,80])
S4=pd.Series([35,33,42,52,62,12])
S5=pd.Series([22,32,42,52,62,12])
S6=pd.Series([10,20,30,40,50,60])
S7=S2+S3+S4+S5+S6
dic1={'Name':S1,'ACC':S2,'BS':S3,'ECO':S4,'ENG':S6,"total":S7}
df1=pd.DataFrame(dic1)
df1.to_csv("F:\\MV.csv")
df2=pd.read_csv("F:\\MV.csv")
print(df2)
pl.plot(S1,S2)
pl.plot(S1,S3)
pl.plot(S1,S4)
pl.plot(S1,S5)
pl.plot(S1,S6)
pl.title("MARKS CHART")
pl.xlabel("NAME")
pl.ylabel("MARKS")
pl.legend(["red","blue","yellow","pink","black"])
