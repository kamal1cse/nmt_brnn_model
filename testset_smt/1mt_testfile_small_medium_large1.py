file1 = open("test.pun","r")
file2 = open("test.eng","r")
file3 = open("testpredsmt.eng","r")


#open file in write mode
file4 = open("11testInpSmall.pun","w")
file5 = open("15testInpMedium.pun","w")
file6 = open("19testInpLarge.pun","w")

file7 = open("12testRefSmall.eng","w")
file8 = open("16testRefMedium.eng","w")
file9 = open("20testRefLarge.eng","w")

file10 = open("13testpredSmall.eng","w")
file11 = open("17testpredMedium.eng","w")
file12 = open("21testpredLarge.eng","w")
             
punInput=file1.readlines()
engRef=file2.readlines()
engPred=file3.readlines()
             
for i in range(0,len(punInput)):
    line=punInput[i]
    words = line.split()
    count=len(words)
    print("count is ",i)
    if count<6:
        file4.write(punInput[i])
        file7.write(engRef[i])
        file10.write(engPred[i])
    elif count<15:
        file5.write(punInput[i])
        file8.write(engRef[i])
        file11.write(engPred[i])
    else:
        file6.write(punInput[i])
        file9.write(engRef[i])
        file12.write(engPred[i])

print("done")
print("count is ",i)

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
file10.close()
file11.close()
file12.close()



