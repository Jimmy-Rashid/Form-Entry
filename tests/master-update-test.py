import pandas as amogus

output = amogus.read_excel("output.xlsx")
master = amogus.read_excel("master.xlsx")

master_update = amogus.concat([master, output], ignore_index=True)
master_update.to_excel("master.xlsx", index=False)