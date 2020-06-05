file1 = open("test.pun","r",encoding="utf8")
file2 = open("testref.eng","r",encoding="utf8")
file3 = open("test_demo-model2_step_135847.pt.eng","r",encoding="utf8")


#open file in write mode
file4 = open("11testInpSmall.pun.txt","w",encoding="utf8")
file5 = open("15testInpMedium.pun.txt","w",encoding="utf8")
file6 = open("19testInpLarge.pun.txt","w",encoding="utf8")

file7 = open("12testRefSmall.eng.txt","w",encoding="utf8")
file8 = open("16testRefMedium.eng.txt","w",encoding="utf8")
file9 = open("20testRefLarge.eng.txt","w",encoding="utf8")

file10 = open("13testpredSmall.eng.txt","w",encoding="utf8")
file11 = open("17testpredMedium.eng.txt","w",encoding="utf8")
file12 = open("21testpredLarge.eng.txt","w",encoding="utf8")
             
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



