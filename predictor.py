### Custom definitions and classes if any ###
import warnings
  

warnings.filterwarnings("ignore")


teamD = {
     "Rajasthan Royals" : 1,
    "Gujarat Titans" : 2 ,
    "Royal Challengers Bangalore" : 3,
    "Lucknow Super Giants" : 4,
    "Sunrisers Hyderabad" : 5,
    "Punjab Kings" : 6,
    "Delhi Capitals" : 7,
    "Mumbai Indians" : 8,
    "Chennai Super Kings" : 9,
    "Kolkata Knight Riders" : 10
}

stadiumD = {
    "Narendra Modi Stadium" : 1,
    "MA Chidambaram Stadium" : 2,
    "Arun Jaitley Stadium" : 3,
    "M.Chinnaswamy Stadium" : 4,
    "Wankhede Stadium" : 5,
    "Dr DY Patil Sports Academy" : 6,
    "Punjab Cricket Association IS Bindra Stadium" : 7,
    "Sawai Mansingh Stadium" : 8,
    "Rajiv Gandhi International Stadium" : 9,
    "Eden Gardens" : 10,
    "Maharashtra Cricket Association Stadium" : 11,
    "Brabourne Stadium" : 12,
    "Himachal Pradesh Cricket Association Stadium" : 13,
    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium" : 14
}


def predictRuns(testInput):
   
   import pandas as pd
   import joblib
   
   
   PR=pd.read_csv(testInput)

   wk = len((PR.loc[0,'batsmen']).split(','))-2
   t1 = teamD[PR.loc[ 0 , 'batting_team']]
   t2 = teamD[PR.loc[ 0 , 'bowling_team']]
   std = stadiumD[PR.loc[0,'venue']]
   reg1 = joblib.load('models/P' + str( t1 - 1) + "1")
   reg2 = joblib.load('models/P' + str(t2 - 1) + "2")
   reg3 = joblib.load('models/P' + str(t1 - 1) + "S")
   reg4 = joblib.load('models/PSF')

   p1 = reg1.predict([[ t2 , wk ]])
   p2 = reg2.predict([[ t1 , wk ]])
   p3 = reg3.predict([[ std, wk ]])
   p4 = reg4.predict([[ std, wk ]])


   prediction = int((p1 + p2 + p3 + p4)/4)
   return prediction



import joblib
wk = 1
t1 = 7 
t2 = 10
std = 7
reg1 = joblib.load('models/P' + str( t1 - 1) + "1")
reg2 = joblib.load('models/P' + str(t2 - 1) + "2")
reg3 = joblib.load('models/P' + str(t1 - 1) + "S")
reg4 = joblib.load('models/PSF')

p1 = reg1.predict([[ t2 , wk ]])
p2 = reg2.predict([[ t1 , wk ]])
p3 = reg3.predict([[ std, wk ]])
p4 = reg4.predict([[ std, wk ]])

#print(p1 , p2 ,p3 ,p4)
prediction = ((p1 + p2 + p3 + p4)//4)
print("PROJECTED SCORE after 6 Overs is-->",prediction)