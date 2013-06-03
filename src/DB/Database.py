
import string
import random

def Rand_Gen(size, chars):#create random generated names or numbers
    return ''.join(random.choice(chars) for x in range(size))

def Create_Rand_DB(l='',a=0):#create a database with all random values in it
        if l.__eq__(''):
            print"Enter file name with the path if in a different file:\n" 
            l=raw_input()
        f=open(l,'w')
        if a == 0:
            print"Enter the number of companies to be put into dict:\n"
            a=int(raw_input())
        e=["Company_Name : ","Ticker_Symbol : ","Eps : ","Revenue : ","S&M_Expenses : ","Service_Expenses : ","R&D_Expenses : ","Tax : ","Quarter : ","Year : "] 
        quarters=["Q1","Q2","Q3","Q4"]
        for k in range(a):
            cname=Rand_Gen(10,string.ascii_lowercase)
            tkr=cname[:3]
            tax="35"
            yr="19"+Rand_Gen(2,string.digits)
            for qtr in quarters:
                f.write(e[0]+cname+"\n")
                f.write(e[1]+tkr+"\n")
                f.write(e[2]+Rand_Gen(3,string.digits)+"\n")
                f.write(e[3]+Rand_Gen(10,string.digits)+"\n")
                f.write(e[4]+Rand_Gen(9,string.digits)+"\n")
                f.write(e[5]+Rand_Gen(8,string.digits)+"\n")
                f.write(e[6]+Rand_Gen(9,string.digits)+"\n")
                f.write(e[7]+tax+"\n")
                f.write(e[8]+qtr+"\n")
                f.write(e[9]+yr+"\n")
                f.write("---------------------------------"+"\n")
        f.write('\n')#a blank line conceptually marks the end of file
        f.close()
        return Read_Database(l)
        
def Read_Database(l):#read a database (if it exists)
        db=[]
        f=open(l, 'r')
        a={}
        while 1:
            line=f.readline()
            if line=='\n':#reached end of data base
                break 
            if Make_DB(a,line):
                db.append(a)
                a={}
        f.close()
        return db

def Make_DB(a,line):#make the temp created database permanent
    w=line.split()
    if len(w)==1:#means reached ------- line or end of a company
        return True#end of a company
    a[w[0]]=w[2]
    return False

def Display_DB(db,a=[]):#displays the database in a nice orderly manner
    c=[]
    if a.__len__()!=0:
        for i in range(db.__len__()):
            for j in range(a.__len__()):
                b=str(a[j])+":"+str(db[i][a[j]])+"\n"
                c.append(b)
            d="---------------------------------"+"\n"+"THE COMPANY NUMBER:-\t"+str(i+1)+"\n"
            c.append(d)
    else:
        e=["Company_Name","Ticker_Symbol","Eps","Revenue","S&M_Expenses","Service_Expenses","R&D_Expenses","Tax","Quarter","Year"]
        for i in range(db.__len__()):
            for j in range(e.__len__()):
                b=str(e[j])+":"+str(db[i][e[j]])+"\n"
            d="---------------------------------"+"\n"+"THE COMPANY NUMBER:-\t"+str(i+1)+"\n"
            c.append(d)
    return c


def Remove_From_DB(db,a):#remove the enteries from database
    for j in a:
        e=["Company_Name"]
        for i in range(db.__len__()):
            if db[i][e[0]] == j:
                db.pop(i)
                break
    return db

def Sort_DB(db,b):#sort db wrt a particular key
    db = sorted(db, key=lambda k: k[b])
    return db

def Total_Expenses(db):#calculate total expenses
    a="Total_Expenses"
    e=["S&M_Expenses","Service_Expenses","R&D_Expenses"]
    for i in range(db.__len__()):
        b=long(db[i][e[0]])
        c=long(db[i][e[1]])
        d=long(db[i][e[2]])
        db[i][a]=str(b+c+d)
    return db

def Operating_Margin(db):#calculate operating margin
    a="Operating_Margin"
    e=["Total_Expenses","Revenue"]
    for i in range(db.__len__()):
        b=int(db[i][e[0]])
        c=int(db[i][e[1]])
        db[i][a]=str(c-b)
    return db

def Operating_Margin_Percentage(db):#calculate operating margin percentage
    a="Operating_Margin_Percentage"
    e=["Revenue","Operating_Margin"]
    for i in range(db.__len__()):
        b=int(db[i][e[0]])
        c=int(db[i][e[1]])
        c=int((float(c)/b)*100)
        db[i][a]=str(c)
    return db

def Ratio(db):#calculate r&d ratio
    a="R&D_Ratio"
    e=["Revenue","R&D_Expenses"]
    for i in range(db.__len__()):
        b=int(db[i][e[0]])
        c=int(db[i][e[1]])
        db[i][a]=str(float(b)/c)
    return db

def Growth_Rate(db):#calculate growth rate
    a="Growth_Rate"
    e=["Operating_Margin","Revenue"]
    j=0
    for i in range(db.__len__()):
        b=int(db[i][e[0]])
        c=int(db[i][e[1]])
        db[i][a]=str(float(b)/c)
    return db

def Call_All(db):#this function will call all the functions to calculate om , r&d ratio etc to complete the db enteries
    db=Total_Expenses(db)#sum of all expenses
    db=Operating_Margin(db)#difference of Total_Expenses and revenue
    db=Operating_Margin_Percentage(db)#Op % to Total_expenses
    db=Growth_Rate(db)#Growth_Rate
    db=Ratio(db)
    return db

if __name__ == '__main__':
    c=[]
    a=[]
    db=Create_Rand_DB()
    c=db
    Display_DB(db,a)
    print "Enter the key on which the sort is to run:-\t"
    b=raw_input()
    db=Sort_DB(db,b)
    db=Remove_From_DB(db,a)
    Call_All(db)
