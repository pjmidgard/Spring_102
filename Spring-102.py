from time import time
import os
import binascii
import math
import os.path

lenf=0
name=""
add_bits=""
Make_togher=""

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
     
        def cryptograpy_compression4(self):
               
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":       
                    if namez=="c":
                        
                        
                        Deep=1
 

                        Deep3=-1
                        Block_101=1
                        
                        
                        compress_or_not_compress1=0

                        Predict_Combiton=10
                        Predict_Combiton_Max=100
                        
                        Predict_Number=10
                        Predict_Number2=10
                        Last_bits=""
                        Last_bits_Save=""
                        File_stop=1
                        Compress_times=0
                        J=0
                        Compress_times_Str=""
                        Ti=0
                        
                        

                        i=1

                    if namez=="e":
                        Deep=20
 

                        Deep3=-1
                        Block_101=2
                        J=0
                        
                        
                        compress_or_not_compress1=0
                        
                        Predict_Number=10
                        Predict_Number2=10
                        Last_bits=""
                        Last_bits_Save=""
                        File_stop=1
                        Compress_times=0
                        i=2
               
                    Number_add_plus_one=""
                    Prime_Not=""
                    Times_6=""
                    Corrupted=0
                     
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                           
                   
                    namem=""
                    namema="?"
                    Number_N12=""
                    X_1=""
                    X_2=""
       
                    nameas=name
                    nac=len(nameas)
                   
                    compress_or_not_compress=1
                    Circle_times3=0

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                 
                            nameas=name[:nac-4]
                            nac=len(nameas)
                           
                            C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                 
                    if i==1:
                        Compress_times=0
                       
                       
                        nameas=name+".bin"
                        N_N=0
                        N_n=0
                   
                       
                    nac=len(nameas)
                   
                    Block_10R=0
                    Block_10T_U=0
                    Block_10TU10=0
                    Block_10TU11=0
                   
                 
                    s=""

                    Equal_info_between_of_the_cirlce_of_the_file=""
                    Equal_info_between_of_the_cirlce_of_the_file_2=""

                    Prime_Not=""
                    Times_6=""

                    Translate_info_Decimal=""

                    D=0

                    x=0
                    x1=0
                    x2=0
                    n=0
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
                        lenf7=len(data)
                        if lenf7==0:
                            raise SystemExit
                       
                        END_working=0
                        Circle_times2=0
                                 
                        Equal_info_between_of_the_cirlce_of_the_file_23=""

                        sda18=""
                        Equal_info_between_of_the_cirlce_of_the_file_29=""
                       
                        SpinS=0
                        while END_working<10:
                     
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                               
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                               
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1
                                           
                                   

                                    if Circle_times3==1:
                                        Equal_info_between_of_the_cirlce_of_the_file_2=sda
                           
                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_2, 2)
                               
                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                           
                                    width_bits3=binascii.unhexlify(width_bits % n)                                   
                                    width_bits2=len(width_bits3)
                                   
                                    data=width_bits3
                                 
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                               
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1

                                    Equal_info_between_of_the_cirlce_of_the_file_2=sda

                                    lenf3=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                lenf2=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**40)-1:
                                        raise SystemExit

                                #########################################################################################################################################################
                               
                               
                                if i==1:

                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file_2)

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                               
                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file)
                                   
                                   
                                    #Extract
                           
                                    s=""

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                   
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                 
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                 
                                    g=0

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)                     
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                               
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                   
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                               
                                    add_bits=""

                                    Times_6=""

                                    #Compression

                                    sda10=""
                                    Translate_info_Decimal=""
                                   
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
               
                                    if  Circle_times2==0 and SpinS==0:
                                        Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file
                                        SpinS=1

                                   


                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                           
                                   
                                    INIT=""
                                    Number_N=""
                                    INIT=Equal_info_between_of_the_cirlce_of_the_file
                                   
                                        
                                    #print(INIT)
                                    block=0
                                    Block_10T=0
                                    Number_N4=""

                                   
                                    Predict_Number=Predict_Number2
                                    Predict_Number3=Predict_Number2
                                    Predict_Number4=str(Predict_Number3)
                                    Number_Predict_Save=0
                                
                                   

                                    while block<lenf6:
                                            Number_N1=INIT[block:block+1]
                                            Number_N2=INIT[block+1:block+2]
                                            Number_N3=INIT[block+2:block+3]
                                            Number_N14=INIT[block+3:block+4]
                                            Number_N15=INIT[block+4:block+5]
                                            Number_N16=INIT[block+5:block+6]

                                            Number_N17=INIT[block:block+8]
 
                                            
                                         
                                            Block_101_binary=bin(Block_101)[2:]

                                            if Block_101==1:
                                                    Last_bits=Number_N1+Number_N2+Number_N3
                                                    Block_103=Block_101+0
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                    Number_N=Number_N1+"0"+Number_N2+"0"+Number_N3+"0"
                                                   
                                                    Block_102_binary="0"+"0"+"0"+"0"+"0"+"0"
                                                    Block_122_binary="0"+"0"+"0"+"0"+"1"+"0"
                                                    Block_123_binary="0"+"0"+"1"+"0"+"0"+"0"

                                                    Block_103=Block_101+0
                                                    Block_105_binary=str(Block_103)

                                                   


                                                    Block_101_1_binary="0"+"0"+"1"+"0"+"1"+"0"
                                                    Block_101_2_binary="1"+"0"+"0"+"0"+"0"+"0"
                                                    Block_101_3_binary="1"+"0"+"0"+"0"+"1"+"0"


                                                    Block_103=Block_101+0
                                                    Block_105_binary=str(Block_103)

                                                   


                                                    Block_101_1_1_binary="1"+"0"+"1"+"0"+"0"+"0"
                                                    Block_101_2_1_binary="1"+"0"+"1"+"0"+"1"+"0"

                                                    Block_101_4_1_binary=""
                                                   
                                                   
                                                   
                                            else:
                                                    Block_103=Block_101+0
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                    Number_N=Number_N1+Number_N2+Number_N3+Number_N14+Number_N15+Number_N16
                                                   
                                                    #print(Number_N2)
                                                   
                                                    Block_102_binary=""


                                                    Block_103=Block_101+1
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                   

                                                   
                                                    Block_122_binary=""


                                                    Block_103=Block_101+2
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                   
                                                   
                                                    Block_123_binary=""




                                                    Block_103=Block_101+3
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                   
                                                   
                                                    Block_101_1_binary=""


                                                    Block_103=Block_101+4
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary


                                                    Block_1031=Block_101+3
                                                    Block_105_binary1=str(Block_1031)

                                                    Block_106_binary1=Block_105_binary1
                                           
                                                   

                                                   
                                                    Block_101_2_binary=""


                                                    Block_103=Block_101+5
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                   
                                                   
                                                    Block_101_3_binary=""


                                                    Block_103=Block_101+6
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                   
                                                   
                                                    Block_101_1_1_binary=""


                                                    Block_103=Block_101+7
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                   
                                                   
                                                   
                                                    Block_101_2_1_binary=""


                                                    #Predict

                                                   
                                                                   
                                                    #print(Block_10T4) 
                                                
                                                
                                                    Block_103=Predict_Number
                                                    Block_105_binary=str(Block_103)

                                                    Block_106_binary=Block_105_binary
                                           
                                                   

                                                   
                                                    Block_101_4_1_binary=Block_106_binary

                                                    X2=Block_106_binary
                                                    long1=len(X2)

                                                    X_N=int(X2)
                                                    #print(X_N)


                                                    


                                                    Predict_Number11=Predict_Number+1
                                                    if  Predict_Number11==Predict_Combiton_Max:
                                                            Predict_Number11=Predict_Combiton
                                                           


                                                    Block_1031=Predict_Number11
                                                    Block_1051_binary=str(Block_1031)

                                                    Block_10611_binary=Block_1051_binary
                                           
                                                   

                                                   
                                                    Block_101_4_11_binary=Block_10611_binary

                                                    X12=Block_10611_binary
                                                    long11=len(X12)
                                                    #print(X2)

                                                 
                                                    long=len(Block_101_4_1_binary)
                                                    Number_N17=INIT[block:block+long]
                                                    Number_N12=Number_N17
                                                    X10=Number_N12
                                                    #print(Number_N12)
                                                    #print(Block_101_4_1_binary)
                                                   

                                                                                                       
                                                   
                                                    #print(Block_102_binary)
                                            if Block_101==1:

                                                    Number_N18=len(Number_N17)
                                                    if Number_N18==8:

                                                            Number_N17=int(Number_N17,2)

                                                            Number_N17=Number_N17+10


                                                            Number_N19=str(Number_N17)

                                                            Number_N19_Long=len(Number_N19)

                                                            if Number_N19_Long==1:#255 265
                                                                    Number_N19="000"+Number_N19

                                                            elif Number_N19_Long==2:#255 265
                                                                    Number_N19="00"+Number_N19

                                                            elif Number_N19_Long==3:#255 265
                                                                    Number_N19="0"+Number_N19
                                                                    
                                                            #print(Number_N19)
                                                            Number_N4=Number_N4+Number_N19
                                                            block=block+8

                                                    else:
                                                            #print(Block_101_4_1_binary

                                                         
                                                            Last_bits_Save=Last_bits
                                                            #print(Block_10T4+"1")
                                                            block=block+3          
                                                   
                                                                 
                                            if Block_101!=1:
                                                     
                                                    Compress_times_Str=str(Compress_times)
                                                    Compress_times_Long=len(Compress_times_Str)
                                                   
                                                    X_12=str(X_N)
                                                    if  Ti==1:
                                                            #print(Block_101_4_1_binary)
                                                            

                                                            #print(X_12[1:2])

                                                            Number_N4=Number_N4+X_12[0:2]
                                                            Ti=0
                                                            #print("1"+Compress_times_Str)
                                                            #print(X2)
                                                            block=block+long
                                                            Number_Predict_Save=1 
                                                       
                                                    elif X_N>=Predict_Number and X_N<=Predict_Number+9 and X_12!="0" and Ti==0:
                                                            #print(Block_101_4_1_binary)
                                                            

                                                            #print(X_12[1:2])

                                                            Number_N4=Number_N4+X_12[1:2]
                                                            Ti=1
                                                            #print("1"+Compress_times_Str)
                                                            #print(X2)
                                                            block=block+long
                                                            Number_Predict_Save=1
                                                           
                                                           
                                                   
                                                   
                                                 
                                                    else:
                                                            #print(Block_101_4_1_binary

                                                         
                                                            Number_N4=Number_N4+Number_N1
                                                            J=J+1
                                                            #print(Block_10T4+"1")
                                                            block=block+1
                                           
                                                    Predict_Number=Predict_Number+1#
                                                    if Predict_Number==Predict_Combiton_Max:
                                                            Predict_Number=Predict_Combiton
                                    if Block_101==1:
                                        Block_101=2
                                    
                                    
                        
                                    if Number_Predict_Save==1 or J>0:
                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                            
                                           

                                           
                                            lenf6=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                                       

                                            
                                                   
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                           
                                            Number_N4=Equal_info_between_of_the_cirlce_of_the_file_17
                                            
                                                

                                                
                                       
                                 
                                            Compress_times=Compress_times+1
                                            J=0
                                            #print(Compress_times)
                                            
                                           

                                       
                                           
                                    #print(Block_101)
                                    Predict_Number2=Predict_Number2+1
                                    if Predict_Number2==Predict_Combiton_Max:
                                            Predict_Number2=Predict_Combiton
                                   
                                   
                                  
                                   
                                   
                                 
                                 
                                    if compress_or_not_compress==1:
                                       
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                            #print(Number_N4)
                                 
                                   
   
                                    if compress_or_not_compress==1:
                                         
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                            sda18=Equal_info_between_of_the_cirlce_of_the_file
                                            #print(len(Equal_info_between_of_the_cirlce_of_the_file_17))
                             
                                   
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)

                                    if lenfS<20:
                                            File_stop=0

                                   

                                    if compress_or_not_compress==2 and Circle_times2==0:
                                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[1:]
                                   
                                 
                                    Circle_times2=Circle_times2+1
                         
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17

                                    if compress_or_not_compress==2:
                                                  
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file


                                    if Compress_times==Deep:
                                            compress_or_not_compress1=3 
                  


                                         
                                           
                                           
                                 
                                   
                                    if  lenfS<=Deep3 or compress_or_not_compress==2:
                                        Circle_times3=Circle_times2
                                       
                                        if compress_or_not_compress==2:
                                            Circle_times3=Circle_times2-1


                                   
                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:

                                            
                                            Number_N4=Number_N4+"0"+Last_bits_Save
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                            Last_bits_long=len(Last_bits_Save)
                                            Last_bits_long=Last_bits_long+1
                                            Last_bits_long_str=str(Last_bits_long)
                                            Number_N4=Last_bits_long_str+Number_N4
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4

                                            Number_N5=int(Number_N4)

                                            Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_N5)[2:]
                                           
                                   

                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)                                         
                                            Equal_info_between_of_the_cirlce_of_the_file_17="1"+Equal_info_between_of_the_cirlce_of_the_file_17
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:

                                                                                             
                                                times_compress=bin(Compress_times)[2:]
                                                lenf1=len(times_compress)
                                                add_bitst=""
                                               
                                                count_bitst=8-lenf1%8
                                               
                                                z=0
                                                if count_bitst!=0:
                                                        if count_bitst!=8:
                                                            while z<count_bitst:
                                                                add_bitst="0"+add_bitst
                                                                z=z+1

                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:
                                               
                                                add_bits=""
                                                count_bits=8-lenf%8
                                                z=0
                                                if count_bits!=0:
                                                        if count_bits!=8:
                                                            while z<count_bits:
                                                                add_bits="0"+add_bits
                                                                z=z+1
                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:
                                           
                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                           
                                    if  lenfS<=Deep3 or compress_or_not_compress1==3:
                                               
                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)
                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                           
                                            with open(nameas, "wb") as f2:
                                                f2.write(width_bits3)
                                       
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
                                if i==2:

                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                             
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                   
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    sda10=""
                                    Translate_info_Decimal=""
                                 
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                               
                                    Number_of_the_file=0
                                    Prime_Not=0
                               
                                    if C==1:
                                        if  Circle_times2==0:

                                           
                                                if Equal_info_between_of_the_cirlce_of_the_file[0:9]=="000000001":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[9:]

                                                elif Equal_info_between_of_the_cirlce_of_the_file[0:8]=="00000001":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]

                                                elif Equal_info_between_of_the_cirlce_of_the_file[0:7]=="0000001":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[7:]

                                                elif Equal_info_between_of_the_cirlce_of_the_file[0:6]=="000001":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[6:]

                                                elif Equal_info_between_of_the_cirlce_of_the_file[0:5]=="00001":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[5:]

                                                elif Equal_info_between_of_the_cirlce_of_the_file[0:4]=="0001":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[4:]

                                                elif Equal_info_between_of_the_cirlce_of_the_file[0:3]=="001":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[3:]

                                                elif Equal_info_between_of_the_cirlce_of_the_file[0:2]=="01":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[2:]

                                                elif Equal_info_between_of_the_cirlce_of_the_file[0:1]=="1":
                                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[1:]
                                                        
                                                T=2

                                                Equal_info_between_of_the_cirlce_of_the_file3=int(Equal_info_between_of_the_cirlce_of_the_file,2)
                                                Equal_info_between_of_the_cirlce_of_the_file3=str(Equal_info_between_of_the_cirlce_of_the_file3)
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file3)
                                                if Equal_info_between_of_the_cirlce_of_the_file3[0:1]=="1":
                                                        Equal_info_between_of_the_cirlce_of_the_file3=Equal_info_between_of_the_cirlce_of_the_file3[1:lenf6-1]
                                                        
                                                elif Equal_info_between_of_the_cirlce_of_the_file3[0:1]=="2":
                                                        Last_bits=Equal_info_between_of_the_cirlce_of_the_file3[lenf6-1:]
                                                        Equal_info_between_of_the_cirlce_of_the_file3=Equal_info_between_of_the_cirlce_of_the_file3[1:lenf6-2]
                                                        
                                                
                                                elif Equal_info_between_of_the_cirlce_of_the_file3[0:1]=="3":
                                                        Last_bits=Equal_info_between_of_the_cirlce_of_the_file3[lenf6-2:]
                                                        Equal_info_between_of_the_cirlce_of_the_file3=Equal_info_between_of_the_cirlce_of_the_file3[1:lenf6-3]
                                               
                                       
                                       
                                           
   
                                        if C==1 and T!=0:
                                                    Equal_info_between_of_the_cirlce_of_the_file3=Equal_info_between_of_the_cirlce_of_the_file3
                                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file3)
                                                    X2=""
                                                    X12=""
                                                    X10=""
                                                    


                                                    

                                                    INIT=""
                                                    Number_N=""
                                                    INIT=Equal_info_between_of_the_cirlce_of_the_file3
                                                    
                                                   
                                                        
                                                    #print(INIT)
                                                    block=0
                                                    Block_10T=0
                                                    Number_N4=""

                                                   
                                                    Predict_Number=10
                                                    Predict_Number3=10
                                                    Predict_Number4=str(Predict_Number3)
                                                    Number_Predict_Save=0
                                                
                                                   

                                                    while block<lenf6:
                                                            Number_N1=INIT[block:block+1]
                                                            
                                                         
                                                            Block_101_binary=bin(Block_101)[2:]

                                                            
                                                            if Block_101==1:
                                                                     Number_N= Number_N1    
                                                                   
                                                                   
                                                            if Block_101!=1:
                                                                    Block_103=Block_101+0
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary
                                                           
                                                                    Number_N=Number_N1
                                                                   
                                                                    #print(Number_N2)
                                                                   
                                                                    Block_102_binary=""


                                                                    Block_103=Block_101+1
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary
                                                           
                                                                   

                                                                   
                                                                    Block_122_binary=""


                                                                    Block_103=Block_101+2
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary
                                                           
                                                                   
                                                                   
                                                                    Block_123_binary=""




                                                                    Block_103=Block_101+3
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary
                                                           
                                                                   
                                                                   
                                                                    Block_101_1_binary=""


                                                                    Block_103=Block_101+4
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary


                                                                    Block_1031=Block_101+3
                                                                    Block_105_binary1=str(Block_1031)

                                                                    Block_106_binary1=Block_105_binary1
                                                           
                                                                   

                                                                   
                                                                    Block_101_2_binary=""


                                                                    Block_103=Block_101+5
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary
                                                           
                                                                   
                                                                   
                                                                    Block_101_3_binary=""


                                                                    Block_103=Block_101+6
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary
                                                           
                                                                   
                                                                   
                                                                    Block_101_1_1_binary=""


                                                                    Block_103=Block_101+7
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary
                                                           
                                                                   
                                                                   
                                                                   
                                                                    Block_101_2_1_binary=""


                                                                    #Predict

                                                                   
                                                                                   
                                                                    #print(Block_10T4) 
                                                                
                                                                
                                                                    Block_103=Predict_Number
                                                                    Block_105_binary=str(Block_103)

                                                                    Block_106_binary=Block_105_binary
                                                           
                                                                   

                                                                   
                                                                    Block_101_4_1_binary=Block_106_binary

                                                                    X2=Block_106_binary
                                                                    long1=len(X2)


                                                                    Predict_Number11=Predict_Number+1
                                                                    if  Predict_Number11==100:
                                                                            Predict_Number11=10
                                                                           


                                                                    Block_1031=Predict_Number11
                                                                    Block_1051_binary=str(Block_1031)

                                                                    Block_10611_binary=Block_1051_binary
                                                           
                                                                   

                                                                   
                                                                    Block_101_4_11_binary=Block_10611_binary

                                                                    X12=Block_10611_binary
                                                                    long11=len(X12)
                                                                    #print(X2)

                                                                 
                                                                    long=len(Block_101_4_1_binary)
                                                                    Number_N17=INIT[block:block+long]
                                                                    Number_N12=Number_N17
                                                                    X10=Number_N12
                                                                    #print(Number_N12)
                                                                    #print(Block_101_4_1_binary)
                                                                   

                                                                                                                       
                                                                   
                                                                    #print(Block_102_binary)
                                                            if Block_101==1:
                                                                    
                                                                    if Number_N=="9":

                                                                            Number_N4=Number_N4+"111"
                                                                        
                                                                            block=block+1
                                                                                   
                                                                   
                                                                    elif Number_N=="8":

                                                                            Number_N4=Number_N4+"110"
                                                                        
                                                                            block=block+1
                                                               
                                                                            #print(Block_106_binary)
                                                                    elif Number_N=="7":

                                                                            Number_N4=Number_N4+"101"
                                                                        
                                                                            block=block+1


                                                                    elif Number_N=="6":

                                                                            Number_N4=Number_N4+"100"
                                                                        
                                                                            block=block+1

                                                                    elif Number_N=="5":

                                                                            Number_N4=Number_N4+"011"
                                                                        
                                                                            block=block+1
                                                                           
                                                                    elif Number_N=="4":

                                                                            Number_N4=Number_N4+"010"
                                                                        
                                                                            block=block+1


                                                                    elif Number_N=="3":

                                                                            Number_N4=Number_N4+"001"
                                                                        
                                                                            block=block+1

                                                                    elif Number_N=="2":

                                                                            Number_N4=Number_N4+"000"
                                                                        
                                                                            block=block+1
                                                                    else:
                                                                        print("file corrupted")
                                                                        raise SystemExit
                                                                                
                                                                   
                                                                              
                                                            if Block_101!=1:
                                                                     
                                                               
                                                                    if Number_N1=="1":
                                                                            #print(Block_101_4_1_binary)

                                                                         
                                                                            Number_N4=Number_N4+X2
                                                                            #print(X2)
                                                                            block=block+1
                                                                            Number_Predict_Save=1
                                                                            J=J+1
                                                                           
                                                                           
                                                                    elif Number_N1=="0":
                                                                            #print(Block_101_4_1_binary)

                                                                         
                                                                            Number_N4=Number_N4+X12
                                                                            #print(X12)
                                                                            block=block+1
                                                                            Number_Predict_Save=1
                                                                            J=J+1
                                                                           
                                                                   
                                                                 
                                                                    else:
                                                                            #print(Block_101_4_1_binary

                                                                         
                                                                            Number_N4=Number_N4+Number_N1
                                                                            J=J+1
                                                                            #print(Block_10T4+"1")
                                                                            block=block+1
                                                           
                                                                    Predict_Number=Predict_Number+1#
                                                                    if Predict_Number==100:
                                                                            Predict_Number=10
                                    if J>0:
                                        Block_101=1
                                        J=0
                                        
                                    

                                            
                                            
                        
                                                
                                    Times_6=Number_add_plus_one
                                    Number_add_plus_one=""
                                     
                                    #####################################################################################################################################################
                                 
                                    Prime_Not=""
                                   
                                   
                                    Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4
                                    #print(Equal_info_between_of_the_cirlce_of_the_file_17)
                                   
                                    Equal_info_between_of_the_cirlce_of_the_file3=Equal_info_between_of_the_cirlce_of_the_file_17
                                 

                                    if i==2:
                                        Make_togher=""
                                        Make_togher=Times_6
                                        Number_add_plus_one=""
                                        add_bits=""
                                        if C==1 and T!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                        #print(Circle_times2)
                                       
                                       
                                        if  Circle_times2==T:
                                             
                                            if C==1 and T==0:
                                                Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file
                                                lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                add_bits=""
                                                count_bits=8-lenf%8
                                                z=0
                                                if count_bits!=0:
                                                        if count_bits!=8:
                                                            while z<count_bits:
                                                                add_bits="0"+add_bits
                                                                z=z+1
                                                Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                       
                                            if C==1 and T!=0:
                                                Equal_info_between_of_the_cirlce_of_the_file_17=Number_N4+Last_bits

                                                Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_17[1:]
                                                lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                
                                                   
                                               
                                                lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                add_bits=""
                                                count_bits=8-lenf%8
                                                z=0
                                                if count_bits!=0:
                                                        if count_bits!=8:
                                                            while z<count_bits:
                                                                add_bits="0"+add_bits
                                                                z=z+1
                                                if len(add_bits)==8:
                                                        add_bits=""
                                                                
                                                Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                            #print(Equal_info_between_of_the_cirlce_of_the_file_17)

                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                       
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)

                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                           
                                            with open(nameas, "wb") as f2:
                                           
                                             
                                                f2.write(width_bits3)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)

                                        
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
