import pandas as pd

myData = {
    "Cars" : ["BMW" , "Porsche" , "McLaren" , "Pagani" , "Lamborghini" , "Mercedes" , "Toyota" , "Kia"],
    "Top Speed" : [250 , 260 , 375 , 375 , 350 , 300 , 300 , 225]
}

myDataFrame = pd.DataFrame(myData)

print(myDataFrame)
print()
print()
print(myDataFrame.head(2))
print()
print()
print(myDataFrame.tail(2))