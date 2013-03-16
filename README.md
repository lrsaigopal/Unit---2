Unit---2
========



Extension Of Unit 1 With Socket Programming

To Run The Project Please Run Main.py File  To Setup The Database And Init The Server.


Next Run Client.py And Continue .

[All IP Set To LocalHost In The Version.Will Be Removed In The Final Version]


Supported Queries Formats :

1)SELECT Company_Name FROM DB WHERE Operating_Margin_Percentage > 20 AND Revenue > 6000000000 AND Quarter = Q1

2)SELECT TOP  ( Revenue , 3 )  Company_Name FROM DB WHERE Year = 1954 #fail

3)SELECT Company_Name , Eps FROM DB WHERE Year = 1995

4)SELECT MAX ( R&D_Ratio , 1 )  Company_Name FROM DB WHERE Year = 1954

5)SELECT Total_Expenses FROM DB WHERE Ticker_Symbol = tzs AND Quarter = Q1
 