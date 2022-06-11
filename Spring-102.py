from time import time
cvf=0
Portal=2
import os
import binascii
self="'"


zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []
namez = input("for compress ul or extract cl? ")
#@Author Jurijus pacalovas
class compression:

    def cryptograpy_compression(self):
                
                self.name = "Author: Jurijus pacalovas"
                
                if namez=="ul":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    if nameas[nac-5:nac]==".docx":
                    	Portal=1
                    if nameas[nac-4:nac]==".pdf":
                    	Portal=3
                    if nameas[nac-4:nac]==".doc":
                    	Portal=1
                    if nameas[nac-4:nac]==".png":
                    	Portal=7
                    if nameas[nac-4:nac]==".jpg":
                    	Portal=9
                    if nameas[nac-4:nac]==".mp4":
                    	Portal=8

                    nameas=name+".Spring-102"
                
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw1=0
                    sw2=0
                    sw3=0
                    sw5=0
                    sw4=0
                    n=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                 
                       

                  
                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1
                                if assxw==e3%12 or assxw==e3%10:
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""  
                                       
                                      
                                            if e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="1" and e3== e3%10:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0" and e3== e3%11:
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                    
                                                    
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="1" and e3== e3%3:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0" and e3== e3%2:
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                    
                                    
                                    
                                            elif e4=="0" and e3== e3%9:
                                                    sda3=sda3+"1"
                                                    e4="1"
                                                    e4=""
                                                
                                            elif e4=="1" and e3== e3%8:
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""
                                                
                                                    
                                            elif e4=="1" and e3 ==e3%1:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                    
                                            elif e4=="0" and e3 ==e3%1:
                                                    sda3=sda3+"1"
                                                    e4="1"
                                                    e4=""
                                                    
                                                    
                                                    
                                            elif e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                            if assxw==e3%2 or assxw==e3%10:
                                            	if e4=="0":
            	                                    sda3=sda3+"0"
            	                                    e4="0"
            	                                    e4=""  
                                               
                                              
            	                                if e4=="1":
            	                                    
            		                           
                                             

                                
                                                   if e4=="0" and e3== e3%7:
                                                    	sda3=sda3+"1"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%16:
                                                        sda3=sda3+"0"
                                                        e4="1"
                                                        e4=""
                                                    
                                                   elif e4=="0" and e3== e3%15:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%14:
                                                        sda3=sda3+"1"
                                                        e4="1"
                                                        e4=""
                                                        
                                               
                                                   elif e4=="1" and e3== e3%13:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""

                                
                                if e4=="1" and e3== e3%9+assxw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                
                                elif e4=="0" and e3== e3%8+assxw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                elif e4=="0" and e3== e3%7+sw2:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0" and e3== e3%8+assxw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                elif e4=="0" and e3== e3%7+sw2:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw2:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""   
                                
                                elif e4=="0" and e3== e3%7+sw1:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw1:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="0" and e3== e3%7+sw:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                
                                elif e4=="0" and e3== e3%5+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
   
                                elif e4=="1" and e3== e3%4+sw4:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw4:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""                                  
                                elif e4=="1" and e3== e3%4+sw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0" and e3== e3%2+sw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                    
                                        
                                elif e4=="1":
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0":
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""                                
 
	                                                  
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    cvf=sw1
                                    cvf=sw2
                                    cvf=sw3
                                    sw=sw+3
                                    sw1=sw1+4
                                    sw2=sw2+1
                                    sw3=sw3+3
                                    
                                    sw4=sw4+n
                                    
                                    n=n+7
                                    
                                    sw5=sw4+n
                                    
                                    
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+2
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                   
                                    n = int(sda3, 2)
                                
                                    qqwslenf=len(sda3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    
                                    
                                    
                                    
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==200:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

    def cryptograpy_unpack(self):                      
                 if namez=="cl":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    Portal=2
                    namea="file.W"
                    namem=""
                    namema="?"
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    nameas=name[:nac-11]
                    nac=len(nameas)
            
                    
                    
                    nac=len(nameas)
                    sw1=0
                    sw2=0
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw3=0
                    sw4=0
                    sw5=0
                    n=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        
                        	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1 
                                
                                if assxw==e3%12 or assxw==e3%10:
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""  
                                       
                                      
                                            if e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="0" and e3== e3%10:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0" and e3== e3%11:
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                    
                                                    
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="1" and e3== e3%3:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0" and e3== e3%2:
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                    
                                    
                                    
                                            elif e4=="0" and e3== e3%9:
                                                    sda3=sda3+"1"
                                                    e4="1"
                                                    e4=""
                                                
                                            elif e4=="1" and e3== e3%8:
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""
                                                
                                                    
                                            elif e4=="1" and e3 ==e3%1:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                    
                                            elif e4=="0" and e3 ==e3%1:
                                                    sda3=sda3+"1"
                                                    e4="1"
                                                    e4=""
                                                    
                                                    
                                                    
                                            elif e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                            if assxw==e3%2 or assxw==e3%10:
                                            	if e4=="0":
            	                                    sda3=sda3+"0"
            	                                    e4="0"
            	                                    e4=""  
                                               
                                              
            	                                if e4=="1":
            	                                    
            		                           
                                             

                                
                                                   if e4=="0" and e3== e3%7:
                                                    	sda3=sda3+"1"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%16:
                                                        sda3=sda3+"0"
                                                        e4="1"
                                                        e4=""
                                                    
                                                   elif e4=="0" and e3== e3%15:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%14:
                                                        sda3=sda3+"1"
                                                        e4="1"
                                                        e4=""
                                                        
                                               
                                                   elif e4=="1" and e3== e3%13:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""

                                
                                if e4=="1" and e3== e3%9+assxw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                
                                elif e4=="0" and e3== e3%8+assxw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                elif e4=="0" and e3== e3%7+sw2:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0" and e3== e3%8+assxw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                elif e4=="0" and e3== e3%7+sw2:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw2:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""   
                                
                                elif e4=="0" and e3== e3%7+sw1:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw1:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="0" and e3== e3%7+sw:
                                	sda3=sda3+"1"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                
                                elif e4=="0" and e3== e3%5+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
   
                                elif e4=="1" and e3== e3%4+sw4:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw4:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""                                  
                                elif e4=="1" and e3== e3%4+sw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0" and e3== e3%2+sw:
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
                                    
                                        
                                elif e4=="1":
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0":
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""                                
 
	                                                  
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    cvf=sw1
                                    cvf=sw2
                                    cvf=sw3
                                    sw=sw+3
                                    sw1=sw1+4
                                    sw2=sw2+1
                                    sw3=sw3+3
                                    
                                    sw4=sw4+n
                                    
                                    n=n+7
                                    
                                    sw5=sw4+n
                                    
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+2
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                   
                                    n = int(sda3, 2)
                                
                                    qqwslenf=len(sda3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                               
                                    sssssw=len(jl) 
                                    sssssw=len(jl)
                                   

                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                    
                            
                                    assxw=assxw+1
                                    if assxw==200:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

                                


 
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)
