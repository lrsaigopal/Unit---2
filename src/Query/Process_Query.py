'''
Created on 16-Feb-2013

@author: Sai Gopal,Dhiren,Rahul
'''
import copy
from DB.Database import Remove_From_DB, Display_DB, Call_All, Sort_DB
from DB import DB
from Query.Adv_Process import Get_Query


def Check_It(a):

    import re    
    re1='(select)'    # Word 1
    re2='( )'    # White Space 1
    re3='(.*)'    # select arguments
    re4='( )'    # White Space 2
    re5='(from)'    # Word 2
    re6='( )'    # White Space 3
    re7='(DB)'    # Word 3
    re8='( )'    # White Space 4
    re9='(where)'    # Word 4
    re10='( )'    # White Space 5
    re11='(.*)'    # where arguments
    
    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11,re.IGNORECASE|re.DOTALL)
    m = rg.search(a)
    #check for select 8 from 8 where
    if m:
        word1=m.group(1)
        ws1=m.group(2)
        c1=m.group(3)
        ws2=m.group(4)
        word2=m.group(5)
        ws3=m.group(6)
        word3=m.group(7)
        ws4=m.group(8)
        word4=m.group(9)
        ws5=m.group(10)
        c2=m.group(11)
        
        s=c1.split()
        #print c1
        if s[0]!='top' and s[0]!='max' and s[0]!='min' :
            #print 'came to check'
            re23='(Company_Name|Ticker_Symbol|Year|Tax|Revenue|S&M_Expenses|Service_Expenses|R&D_Expenses|Quarter|Eps|Total_Expenses|Operating_Margin|Operating_Margin_Percentage|R&D_Ratio|Growth_Rate)'#select R&D_Ratio , Eps from DB where Quarter > 10|(Company_Name , )*|(Ticker_Symbol , )*|(Year , )*|(Eps , )*|(Operating_Margin_Percentage, )*|(Revenue , )*|(S&M_Expenses , )*|(Service_Expenses , )*|(R&D_Expenses , )*|(Quarter , )*|(Total_Expenses , )*|(Operating_Margin , )*|(R&D_Ratio , )*|(Growth_Rate , )*)'    # Word 1
            
            
    
            rg = re.compile(re23,re.IGNORECASE|re.DOTALL)
            mq = rg.search(c1)
            if mq:
                pass
            else :
                return 0
        else :
            re12='(top|Max|Min)'    # for top or max or min
            re13='( )'    # White Space 1
            re14='(\\()'    # Any Single Character 1
            re15='( )'    # White Space 2
            re16='(Company_Name|Ticker_Symbol|Year|Eps|Tax|Revenue|S&M_Expenses|Service_Expenses|R&D_Expenses|Quarter|Total_Expenses|Operating_Margin|Operating_Margin_Percentage|R&D_Ratio|Growth_Rate)'    # Word 2
            re17='( )'    # White Space 3
            re18='(,)'    # Any Single Character 2
            re19='( )'    # White Space 4
            re20='((?:[0-9]*))'    # Variable Name 1
            re21='( )'    # White Space 5
            re22='(\\))'    # Any Single Character 3
            
            rq = re.compile(re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22,re.IGNORECASE|re.DOTALL)
            m = rq.search(c1)
            if m:
            #    print 'wd'
                pass
            else :
                return 0
        t=c2.split()
        p=len(t)
        i=0
        true=1
        while i <p :
            if t[i]=='And' :
                true=0
                break
            i=i+1          
        if true == 0 :
            
    
            
    
            #re35='( )'
            re30='(.*)'    # before and
            re31='( )'    # White Space 1
            re32='(And)'    # Word 1
            re33='( )'    # White Space 2
            re34='(.*)'    # after and
            
    
            rg = re.compile(re30+re31+re32+re33+re34,re.IGNORECASE|re.DOTALL)
            s = rg.search(c2)
            
            if s:
                    q=s.group(1)
                    ws1=s.group(2)
                    word1=s.group(3)
                    ws2=s.group(4)
                    d=s.group(5)
                    #print "("+q+")"+"("+ws1+")"+"("+word1+")"+"("+ws2+")"+"("+d+")"+"\n"
                    re25='(Company_Name|Ticker_Symbol|Year|Tax|Eps|Revenue|S&M_Expenses|Service_Expenses|R&D_Expenses|Quarter|Total_Expenses|Operating_Margin|Operating_Margin_Percentage|R&D_Ratio|Growth_Rate)'    # Word 1
                    re26='( )'    # White Space 1
                    re27='(>|<|>=|<=|=|!=)'    # Any Single Character 1
                    re28='( )'    # White Space 2
                    re29='([a-zA-Z0-9]+)'    # Integer Number 1
        
                    rg = re.compile(re25+re26+re27+re28+re29,re.IGNORECASE|re.DOTALL)
                    f = rg.search(q)
                    v = rg.search(d)
                    if f and v :
                        #print 'regex is correct'
                        return 1
                    else :
                        return 0
            else :
                    return 0
    
    
        else :
    
            re25='(Company_Name|Ticker_Symbol|Year|Eps|Tax|Revenue|S&M_Expenses|Service_Expenses|R&D_Expenses|Quarter|Total_Expenses|Operating_Margin|Operating_Margin_Percentage|R&D_Ratio|Growth_Rate)'    # Word 1
            re26='( )'    # White Space 1
            re27='(>|<|>=|<=|=|!=)'    # Any Single Character 1
            re28='( )'    # White Space 2
            re29='([a-zA-Z0-9]+)'    # Integer Number 1
    
            rg = re.compile(re25+re26+re27+re28+re29,re.IGNORECASE|re.DOTALL)
            x = rg.search(c2)
            if x:
                    word1=x.group(1)
                    ws1=x.group(2)
                    c1=x.group(3)
                    ws2=x.group(4)
                    int1=x.group(5)
                    
                    return 1
            
    
            else :
                return 0
    
    
    
    
         
    else : 
        return 0

def Validate_Query(Que):
    #return 1
    return Check_It(Que)


def Pro_Query(Que, DB):
    NDB=copy.deepcopy(DB)
    NDB=Call_All(NDB)
    temp = Que.split(' ')
    
    if temp.count('where') != 0:
        x=0
        n=len(temp)
        while x<n :
                if temp[x]=='where' :
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
        countand=temp.count('And')+1
        
        for p in range(countand):
            diffq.append([])
 
        n=len(temp)
        while (z+i)<n :
                if temp[z+i]!='And' :
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
            print "Empty"
            exit(0)
        
        col_name=[]
        i=1
        for i in range(common.__len__()):
            if common[i] !='from':
                col_name.append(common[i])
            else:
                break
        col_name.pop(0)
        
        k=col_name.count(',')
        for i in range(k):
            col_name.remove(',')
        if col_name[0]!="top" and col_name[0]!="max":
            Display_DB(NDB,col_name)
        else:
            if col_name[0]=="top":
                NDB=top(NDB,col_name[2],int(col_name[3]))
                for i in range(5):
                    col_name.pop(0)
                Display_DB(NDB,col_name)
            
            if col_name[0]=="max":
                NDB=top(NDB,col_name[2],int(col_name[3]))
                for i in range(5):
                    col_name.pop(0)
                Display_DB(NDB,col_name)
    else:    
        pass

def top(db,cname,num):
    new_db=[]
    db=Sort_DB(db,cname)
    for i in range(num):
        new_db.append(db[i])
    return new_db     
    
def Rec_Query(Que,DB):
    if Validate_Query(Que) == 0:
        print 'Query Entered is Incorrect!!!!!Exiting'
        exit(1)
    Pro_Query(Que,DB)
    

if __name__ == '__main__':
#    Display_DB(DB)
#   Rec_Query('select * from db where Year > 1990 and Year < 1345 and Company__Name = sai',DB)
#    Rec_Query(raw_input('Enter A Query::'),DB)
    print (Validate_Query(raw_input("Enter Query:")))   