import pandas as amogus

# dataframe = amogus.read_excel("storage.xlsx")

gender = "male"
name = "Jimmy"
age = "19"

gender2 = "helicopter"
name2 = "John"
age2 = "46"

df1 = amogus.DataFrame(
    data={"name": [name], "age": [age], "gender": [gender]},
)
df2 = amogus.DataFrame(
    data={"name": [name2], "age": [age2], "gender": [gender2]},
)

if name2 != name:
    df1 = amogus.concat([df1, df2])


print(df1)
