import copy
from DB.Database import Remove_From_DB, Display_DB, Call_All, Sort_DB
from DB import DB
from Query.Adv_Process import Get_Query
import sys 

sting=""

def val_qry(a):#validation begins from here
    global sting
    b,pf,pw=chk_basic(a)
    
    
    m=a.split()
    n=len(m)
    c=appnd(m,0,pf)
    
    if b!=0 :
        d=chk_sel(c)
        if d!=0 :
            e=chk_from(m,pf)
            if e!=0:
                f=appnd(m,pw,n)
                
                g,conf=numand(f)
                if conf > 0 :
                    if g > 0 :
                        h=chck_where(f,g)
                        return h
                    else :
                        h=chk_args2(f)
                        return h
                        
                else :
                    return 0
                
        else :
            return 0
    else :
        return 0
    return e

def numand(a):
    global sting
    n=len(a)
    x=0
    b=0
    z=0
    pos=[]
    
    while x < n :
        if a[x].lower()=='and' :
            b=b+1
            pos.append(x)
        x=x+1
    
    if b > 0 :
        
        while z < b :
            
            if a[pos[z]] != 'AND' :
                
                sting=sting+'and not caps'
                return 0,0
            
            z=z+1
        return b,1
    else :
        
        return b,1
            
def chck_where(a,b):  
            global sting          
            x=0
            z=0
           # print a
            while z < b+1 :
                
                c=appnd(a,x-1,x+3)
                h=chk_args2(c)
                if h == 0 :
                    sting=sting+'error in arguments of where'
                    return 0
                x=x+4
                z=z+1
            return 1
        
        
def chk_args2(a):
    global sting
    n=len(a)
    x=0
    ret=0
    
    if (a[x] == 'Company_Name' or a[x] == 'Ticker_Symbol' or a[x] == 'Operating_Margin_Percentage' or a[x] == 'Year' or a[x] == 'Tax' or a[x] == 'Revenue' or a[x] == 'S&M_Expenses' or a[x] == 'Service_Expenses' or a[x] == 'R&D_Expenses' or a[x] == 'Quarter' or a[x] == 'Eps' or a[x] == 'Total_Expenses' or a[x] == 'Operating_Margin' or a[x] == 'Ratio' or a[x] == 'Growth_Rate') and (a[x+1]=='>' or a[x+1]=='>=' or a[x+1]=='<' or a[x+1]=='<=' or a[x+1]=='=' or a[x+1]=='!=') and a[x+2].isalnum() :
        ret=1
    else :
        sting=sting+'wrong argument2'
        return 0
            
    return ret
   
def appnd(a,b,c):#custom append function list name, start index ,stop index
    global sting
    x=b+1
    d=[]
    while x < c :
        d.append(a[x])
        x=x+1
    return d

def chk_basic(a):#check slect * from * where *
    global sting
    c=a.split()
    d=len(c)
    #print c
    e,pf,pw=chk_pos1(c,d)
    #print e
    if e==1 :
       
            return 1,pf,pw
        
    else :
        sting=sting+'syntax u entered is error'
        return 0,0,0
            
def chk_pos1(c,d):#make sure select > from > where is order followed   
    global sting
    str1='SELECT'
    str2='FROM'
    str3='WHERE'
    x=0
    pf=0
    pw=0
    while x < d :
        if c[x].lower()==str2.lower() :
            pf=x
        if c[x].lower()==str3.lower() :
            pw=x
        x=x+1
    if pf == 0 :
        sting=sting+"no from present"
        return 0,0,0
    if pw == 0 :
        sting=sting+"no where present"
        return 0,0,0
    if pw < pf :
        sting=sting+'wrong format for is after where'
        return 0,0,0
    if pf == 0 or pf < 2 :
        sting=sting+'no argument for select or select is not present'
        return 0,0,0
    if (pf+2) != pw :
        print pf
        print pw
        sting=sting+'no argument for from'
        return 0,0,0
    if c[0] != str1 :
        sting=sting+'select not in capitals'
        return 0,0,0
    
    
    if c[pf] != str2 :
            sting=sting+'for not in capitals'
            return 0,0,0
    
    if c[pw] != str3 :
            sting=sting+'where not in capitals'
            return 0,0,0
    return 1,pf,pw#exit
          
def chk_sel(a):#check contents of select
    global sting
    n=len(a)
    x=n
    if a[0].upper()=='TOP' :
        return chk_top(a,x)
    elif a[0].upper()=='MAX' :
        return chk_max(a,x)
    elif a[0].upper()=='MIN' :
        return chk_min(a,x)
    else :
        return chk_args(a)
 
def chk_args(a):#checks arguments given
    global sting
    n=len(a)
    x=0
    ret=0
    
    
    if a[0] != '*' :
        while x < n :
            if (a[x] == 'Company_Name' or a[x] == 'Operating_Margin_Percentage' or a[x] == 'Eps'or a[x] == 'Ticker_Symbol' or a[x] == 'Year' or a[x] == 'Tax' or a[x] == 'Revenue' or a[x] == 'S&M_Expenses' or a[x] == 'Service_Expenses' or a[x] == 'R&D_Expenses' or a[x] == 'Quarter' or a[x] == 'Total_Expenses' or a[x] == 'Operating_Margin' or a[x] == 'Ratio' or a[x] == 'Growth_Rate' and a[x+1]==','):
                ret=1
            else :
                sting=sting+'wrong argument'
                return 0
            x=x+2
    else :
        ret=1
    return ret 
           

def chk_top(a,n):#check conetnts of top
    global sting
    x=n
    if a[0]== 'TOP' :
        if a[1] == '(' and (a[2]=='CNAME' or a[2]=='TOTAL_EXPENSES' or a[2]=='OPERATING_MARGIN' or a[2]=='OPERATING_MARGIN_PERCENTAGE' or a[2]=='RATIO' or a[2]=='GROWTH_RATE' or a[2]=='Revenue' ) and a[3]==',' :
            b=a[4]
            if b.isdigit() :
                if a[5]==')' :
                    return 1
                else :
                    sting=sting+'mistake in closing )'
                    return 0
            else :
                sting=sting+'wrong type'
                return 0
        else :
            sting=sting+'error in initial part'
            return 0   
    else :
        sting=sting+'top not in caps'
        return 0
        
def chk_max(a,n):#check contents of max
    global sting
    x=n
    if a[0]== 'MAX' :
        if a[1] == '(' and (a[2]=='CNAME' or a[2]=='TOTAL_EXPENSES' or a[2]=='OPERATING_MARGIN' or a[2]=='OPERATING_MARGIN_PERCENTAGE' or a[2]=='RATIO' or a[2]=='GROWTH_RATE' or a[2]=='R&D_Ratio' ) and a[3]==',' :
            b=a[4]
            if b.isdigit() :
                if a[5]==')' :
                    return 1
                else :
                    sting=sting+'mistake in closing )'
                    return 0
            else :
                sting=sting+'wrong type'
                return 0
        else :
            sting=sting+'error in initial part'
            return 0   
    else :
        sting=sting+'MAX not in caps'
        return 0
    
def chk_min(a,n):#check contents of min
    global sting
    x=n
    if a[0]== 'MIN' :
        if a[1] == '(' and (a[2]=='CNAME' or a[2]=='TOTAL_EXPENSES' or a[2]=='OPERATING_MARGIN' or a[2]=='OPERATING_MARGIN_PERCENTAGE' or a[2]=='RATIO' or a[2]=='GROWTH_RATE') and a[3]==',' :
            b=a[4]
            if b.isdigit() :
                if a[5]==')' :
                    return 1
                else :
                    sting=sting+'mistake in closing )'
                    return 0
            else :
                sting=sting+'wrong type'
                return 0
        else :
            sting=sting+'error in initial part'
            return 0   
    else :
        sting=sting+'MIN not in caps'
        return 0
 
def chk_from(a,pf) :#check from value
    global sting
    #print a[pf+1]
    if a[pf+1] != 'DB' :
        sting=sting+'wrong database'
        return 0
    else :
        return 1
 
def Validate_Query(Que):
    b=val_qry(Que)#begin validation
    if b==1:
        return ''
    else :
        return sting
def Pro_Query(Que, DB):
    NDB=copy.deepcopy(DB)
    NDB=Call_All(NDB)
    temp = Que.split(' ')
    
    if temp.count('WHERE') != 0:
        x=0
        n=len(temp)
        while x<n :
                if temp[x]=='WHERE' :
                        break
                x=x+1
        
        common=[]
        for i in range(x):
            common.append(temp[i])
        common.append(temp[i+1])
    
        diffq=[]
        count=0
        z=0
        i=i+2
        countand=temp.count('AND')+1
        
        for p in range(countand):
            diffq.append([])
 
        n=len(temp)
        while (z+i)<n :
                if temp[z+i]!='AND' :
                    diffq[count].append(temp[z+i])
                else:
                    count=count+1
                z=z+1
    
        temp=[]
        for i in range(len(diffq)):
            comcopy=copy.deepcopy(common)
            comcopy.extend(diffq[i])
            temp.append(comcopy)
            strtemp=' '.join(temp[0])
            #print strtemp
            FailedList=Get_Query(strtemp,NDB)
            Remove_From_DB(NDB,FailedList)
            temp=[]
            strtemp=''
            
        if (NDB.__len__()==0):
            return "Empty Result!!!!!"
            exit(0)
        
        col_name=[]
        i=1
        for i in range(common.__len__()):
            if common[i] !='FROM':
                col_name.append(common[i])
            else:
                break
        col_name.pop(0)
        
        if col_name[0] == '*':
            Display_DB(NDB)
        
        else :
            k=col_name.count(',')
            for i in range(k):
                col_name.remove(',')
            if col_name[0]!="TOP" and col_name[0]!="MAX":
                return Display_DB(NDB,col_name)
            else:
                if col_name[0]=="TOP":
                    NDB=top(NDB,col_name[2],int(col_name[4]))
                    for i in range(5):
                        col_name.pop(0)
                    col_name.pop(0)
                    return Display_DB(NDB,col_name)
                
                if col_name[0]=="MAX":
                    NDB=top(NDB,col_name[2],int(col_name[3]))
                    for i in range(5):
                        col_name.pop(0)
                    col_name.pop(0)
                    return Display_DB(NDB,col_name)
    else:    
        pass

def top(db,cname,num):
    new_db=[]
    db=Sort_DB(db,cname)
    for i in range(num):
        new_db.append(db[i])
    return new_db     
    
def Rec_Query(Que,DB):
    mess=Validate_Query(Que)
    if mess != '':
        return ('Query Entered is Incorrect!!!!!'+mess)
    return(Pro_Query(Que,DB))
    

if __name__ == '__main__':
#    Display_DB(DB)
#   Rec_Query('select * from db where Year > 1990 and Year < 1345 and Company__Name = sai',DB)
#    Rec_Query(raw_input('Enter A Query::'),DB)
    print (Validate_Query(raw_input("Enter Query:")))   