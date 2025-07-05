from O1 import ELJIX, JICT
import os

List = {'hi': 2, "test" : 3, "1": "hi"}
Custom = JICT.Convert(List)

J = ELJIX()
J.add(key = "hi", value = 2)
J.add(key = "TheArray", value = Custom)

print(J)

D = J.copy()
J.clear()
print()
print(f"J : {J}")
print(f"D : {D}")
print()
