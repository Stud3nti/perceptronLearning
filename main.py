import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("testdata.xlsx")
df['x0'] = 1
w1 = w2 =w0 = 0
epoch = 32
changes = False
for i in range(epoch):
    for index , row in df.iterrows():
        sum = row['x0']*w0 + row['x1']*w1 + row['x2']*w2
        if (row['y'] == 1 and sum <= 0) or (row['y'] == -1 and sum >= 0):
            w0 = w0 + row['y']*row['x0']
            w1 = w1 + row['y']*row['x1']
            w2 = w2 + row['y']*row['x2']
            changes = True
    if changes == False:
        break
print(w0,w1,w2)
plt.scatter(df['x1'],df['x2'], c=df['y'])
plt.plot([0,10], [(-w0/w2), (-w0-w1*10)/w2], 'r')
plt.show()


