def conversorBase(num,base1:str,base2:str):    
    base1=str(base1)
    base2=str(base2)
    if (not(base1.isnumeric() or base2.isnumeric())):
        return "BASE INEXISTENTE"
    num=str(num)
    base1=int(base1)
    base2=int(base2)
    dic_ln={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'g':16,'h':17,'i':18,'j':19,'k':20,'l':21,'m':22,'n':23,'o':24,'p':25,'q':26,'r':27,'s':28,'t':29,'u':30,'v':31,'w':32,'x':33,'y':34,'z':35,
            0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x',34:'y',35:'z'}    
    x=[]
    x.extend(num)
    x.reverse()
    for z in range(0,len(x)):
        x[z]=dic_ln[x[z]]
        if(x[z]>base1):
            return("VALOR NÃO EXISTENTE NA BASE")
        x[z]=x[z]*base1**z
    num=sum(x)
    x=''
    while num>0:
        x=x+dic_ln[num%base2]
        num=num//base2
    return x[::-1]
