from sklearn.linear_model import LogisticRegression
X = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1]
m = LogisticRegression()
m.fit(X,y)
h = float(input("enter how many hours you studied:"))
r = m.predict([[h]])[0]
if r==1:
    print(f"based on {h} you are likely to PASS")
else:
    print(f"based on {h} you are likely to FAIL")