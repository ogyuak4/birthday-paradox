import random
number=365
listt=[]
def day_finder(a):
    if a<=31:
        return(str(a)+" january")
    elif a>=32 and a<60:
        return (str(a-31) + " february")
    elif a>=60 and a<91:
        return (str(a - 59) + " march")
    elif a>=91 and a<121:
        return (str(a - 90) + " april")
    elif a>=121 and a<152:
        return (str(a - 120) + " may")
    elif a>=152 and a<182:
        return (str(a - 151) + " june")
    elif a>=182 and a<213:
        return (str(a - 181) + " july")
    elif a>=213 and a<244:
        return (str(a - 212) + " august")
    elif a>=244 and a<274:
        return (str(a - 243) + " september")
    elif a>=274 and a<305:
        return (str(a - 273) + " october")
    elif a>=305 and a<335:
        return (str(a - 304) + " november")
    elif a>=335 and a<366:
        return (str(a - 334) + " december")







while number>0:
    aa = random.randint(1, 365)
    listt.append(aa)
    number=number-1

print("first person birthdate is", end=" ")
print(day_finder(listt[0]))
print("second person birthdate is",end=" ")
print(day_finder(listt[1]))
print(" ")


if listt[0]==listt[1]:
    print("birthdate of the person who born in the same day with another person:",end=" ")
    print(day_finder(listt[1]))
    print("people count : 2")

elif listt[0]==listt[2] or listt[1]==listt[2]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[2]))
    print("people count : 3")


elif listt[0]==listt[3] or listt[1]==listt[3] or listt[2]==listt[3]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[3]))
    print("people count : 4")

elif listt[0]==listt[4] or listt[1]==listt[4] or listt[2]==listt[4] or listt[3]==listt[4]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[4]))
    print("people count : 5")


elif listt[0]==listt[5] or listt[1]==listt[5] or listt[2]==listt[5] or listt[3]==listt[5] or listt[4]==listt[5]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[5]))
    print("people count : 6")

elif listt[0]==listt[6] or listt[1]==listt[6] or listt[2]==listt[6] or listt[3]==listt[6] or listt[4]==listt[6] or listt[5]==listt[6]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[6]))
    print("people count : 7")

elif listt[0]==listt[7] or listt[1]==listt[7] or listt[2]==listt[7] or listt[3]==listt[7] or listt[4]==listt[7] or listt[5]==listt[7] or listt[6]==listt[7]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[7]))
    print("people count : 8")

elif listt[0]==listt[8] or listt[1]==listt[8] or listt[2]==listt[8] or listt[3]==listt[8] or listt[4]==listt[8] or listt[5]==listt[8] or listt[6]==listt[8] or listt[7]==listt[8]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[8]))
    print("people count : 9")

elif listt[0]==listt[9] or listt[1]==listt[9] or listt[2]==listt[9] or listt[3]==listt[9] or listt[4]==listt[9] or listt[5]==listt[9] or listt[6]==listt[9] or listt[7]==listt[9] or listt[8]==listt[9]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[9]))
    print("people count : 10")

elif listt[0] == listt[10] or listt[1] == listt[10] or listt[2] == listt[10] or listt[3] == listt[10] or listt[4] == listt[10] or listt[5] == listt[10] or listt[6] == listt[10] or listt[7] == listt[10] or listt[8] == listt[10] or listt[9] == listt[10]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[10]))
    print("people count : 11")

elif listt[0] == listt[11] or listt[1] == listt[11] or listt[2] == listt[11] or listt[3] == listt[11] or listt[4] == listt[11] or listt[5] == listt[11] or listt[6] == listt[11] or listt[7] == listt[11] or listt[8] == listt[11] or listt[9] == listt[11] or listt[10] == listt[11]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[11]))
    print("people count : 12")

elif listt[0] == listt[12] or listt[1] == listt[12] or listt[2] == listt[12] or listt[3] == listt[12] or \
        listt[4] == listt[12] or listt[5] == listt[12] or listt[6] == listt[12] or listt[7] == listt[12] or listt[8] == listt[12] or listt[9] == listt[12] or listt[10] == listt[12] or listt[11] == listt[12]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[12]))
    print("people count : 13")

elif listt[0] == listt[13] or listt[1] == listt[13] or listt[2] == listt[13] or listt[3] == listt[13] or listt[4] == listt[13] or listt[5] == listt[13] or listt[6] == listt[13] or listt[7] == listt[13] or \
        listt[8] == listt[13] or listt[9] == listt[13] or listt[10] == listt[13] or listt[11] == listt[13] or listt[12] == listt[13]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[13]))
    print("people count : 14")

elif listt[0] == listt[14] or listt[1] == listt[14] or listt[2] == listt[14] or listt[3] == listt[14] or listt[4] == listt[14] or listt[5] == listt[14] or listt[6] == listt[14] or listt[7] == listt[14] or listt[8] == listt[14] or \
        listt[9] == listt[14] or listt[10] == listt[14] or listt[11] == listt[14] or listt[12] == listt[14] or listt[13] == listt[14]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[14]))
    print("people count : 15")

elif listt[0] == listt[15] or listt[1] == listt[15] or listt[2] == listt[15] or listt[3] == listt[15] or listt[4] == listt[15] or listt[5] == listt[15] or listt[6] == listt[15] or listt[7] == listt[15] or \
        listt[8] == listt[15] or listt[9] == listt[15] or listt[10] == listt[15] or listt[11] == listt[15] or listt[12] == listt[15] or listt[13] == listt[15] or listt[14] == listt[15]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[15]))
    print("people count : 16")

elif listt[0] == listt[16] or listt[1] == listt[16] or listt[2] == listt[16] or listt[3] == listt[16] or listt[4] == listt[16] or listt[5] == listt[16] or listt[6] == listt[16] or listt[7] == listt[16] or listt[8] == listt[16] or \
        listt[9] == listt[16] or listt[10] == listt[16] or listt[11] == listt[16] or listt[12] == listt[16] or listt[13] == listt[16] or listt[14] == listt[16] or listt[15] == listt[16]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[16]))
    print("people count : 17")

elif listt[0] == listt[17] or listt[1] == listt[17] or listt[2] == listt[17] or listt[3] == listt[17] or listt[4] == listt[17] or listt[5] == listt[17] or listt[6] == listt[17] or listt[7] == listt[17] or listt[8] == listt[17] or listt[9] == listt[17] or \
        listt[10] == listt[17] or listt[11] == listt[17] or listt[12] == listt[17] or listt[13] == listt[17] or listt[14] == listt[17] or listt[15] == listt[17] or listt[16] == listt[17]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[17]))
    print("people count : 18")

elif listt[0] == listt[18] or listt[1] == listt[18] or listt[2] == listt[18] or listt[3] == listt[18] or listt[4] == listt[18] or listt[5] == listt[18] or listt[6] == listt[18] or listt[7] == listt[18] or \
        listt[8] == listt[18] or listt[9] == listt[18] or listt[10] == listt[18] or listt[11] == listt[18] or listt[12] == listt[18] or listt[13] == listt[18] or listt[14] == listt[18] or listt[15] == listt[18] or listt[16] == listt[18] or listt[17] == listt[18]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[18]))
    print("people count : 19")

elif listt[0] == listt[19] or listt[1] == listt[19] or listt[2] == listt[19] or listt[3] == listt[19] or listt[4] == listt[19] or listt[5] == listt[19] or listt[6] == listt[19] or \
        listt[7] == listt[19] or listt[8] == listt[19] or listt[9] == listt[19] or listt[10] == listt[19] or listt[11] == listt[19] or listt[12] == listt[19] or listt[13] == listt[19] or listt[14] == listt[19] or listt[15] == listt[19] or listt[16] == listt[19] or listt[17] == listt[19] or listt[18] == listt[19]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[19]))
    print("people count : 20")

elif listt[0] == listt[20] or listt[1] == listt[20] or listt[2] == listt[20] or listt[3] == listt[20] or listt[4] == listt[20] or listt[5] == listt[20] or listt[6] == listt[20] or listt[7] == listt[20] or listt[8] == listt[20] or listt[9] == listt[20] or \
        listt[10] == listt[20] or listt[11] == listt[20] or listt[12] == listt[20] or listt[13] == listt[20] or listt[14] == listt[20] or listt[15] == listt[20] or listt[16] == listt[20] or listt[17] == listt[20] or listt[18] == listt[20] or listt[19] == listt[20]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[20]))
    print("people count : 21")

elif listt[0] == listt[21] or listt[1] == listt[21] or listt[2] == listt[21] or listt[3] == listt[21] or listt[4] == listt[21] or listt[5] == listt[21] or listt[6] == listt[21] or listt[7] == listt[21] or listt[8] == listt[21] \
        or listt[9] == listt[21] or listt[10] == listt[21] or listt[11] == listt[21] or listt[12] == listt[21] or listt[13] == listt[21] or listt[14] == listt[21] or listt[15] == listt[21] or listt[16] == listt[21] or listt[17] == listt[21] or listt[18] == listt[21] or listt[19] == listt[21] or listt[20] == listt[21]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[21]))
    print("people count : 22")

elif listt[0] == listt[22] or listt[1] == listt[22] or listt[2] == listt[22] or listt[3] == listt[22] or listt[4] == listt[22] or listt[5] == listt[22] or listt[6] == listt[22] or listt[7] == listt[22] or listt[8] == listt[22] or listt[9] == listt[22] or listt[10] == listt[22] or listt[11] == listt[22] or \
        listt[12] == listt[22] or listt[13] == listt[22] or listt[14] == listt[22] or listt[15] == listt[22] or listt[16] == listt[22] or listt[17] == listt[22] or listt[18] == listt[22] or listt[19] == listt[22] or listt[20] == listt[22] or listt[21] == listt[22]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[22]))
    print("people count : 23")

elif listt[0] == listt[23] or listt[1] == listt[23] or listt[2] == listt[23] or listt[3] == listt[23] or listt[4] == listt[23] or listt[5] == listt[23] or listt[6] == listt[23] or listt[7] == listt[23] or listt[8] == listt[23] or listt[9] == listt[23] or listt[10] == listt[23] or listt[11] == listt[23] or \
        listt[12] == listt[23] or listt[13] == listt[23] or listt[14] == listt[23] or listt[15] == listt[23] or listt[16] == listt[23] or listt[17] == listt[23] or listt[18] == listt[23] or listt[19] == listt[23] or listt[20] == listt[23] or listt[21] == listt[23] or listt[22] == listt[23]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[23]))
    print("people count : 24")

elif listt[0] == listt[24] or listt[1] == listt[24] or listt[2] == listt[24] or listt[3] == listt[24] or listt[4] == listt[24] or listt[5] == listt[24] or listt[6] == listt[24] or listt[7] == listt[24] or listt[8] == listt[24] or listt[9] == listt[24] or listt[10] == listt[24] or listt[11] == listt[24] or \
        listt[12] == listt[24] or listt[13] == listt[24] or listt[14] == listt[24] or listt[15] == listt[24] or listt[16] == listt[24] or listt[17] == listt[24] or listt[18] == listt[24] or listt[19] == listt[24] or listt[20] == listt[24] or listt[21] == listt[24] or listt[22] == listt[24] or listt[23] == listt[24]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[24]))
    print("people count : 25")

elif listt[0] == listt[25] or listt[1] == listt[25] or listt[2] == listt[25] or listt[3] == listt[25] or listt[4] == listt[25] or listt[5] == listt[25] or listt[6] == listt[25] or listt[7] == listt[25] or listt[8] == listt[25] or listt[9] == listt[25] or listt[10] == listt[25] or listt[11] == listt[25] or \
        listt[12] == listt[25] or listt[13] == listt[25] or listt[14] == listt[25] or listt[15] == listt[25] or listt[16] == listt[25] or listt[17] == listt[25] or listt[18] == listt[25] or listt[19] == listt[25] or listt[20] == listt[25] or \
        listt[21] == listt[25] or listt[22] == listt[25] or listt[23] == listt[25] or listt[24] == listt[25]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[25]))
    print("people count : 26")

elif listt[0] == listt[26] or listt[1] == listt[26] or listt[2] == listt[26] or listt[3] == listt[26] or listt[4] == listt[26] or listt[5] == listt[26] or listt[6] == listt[26] or listt[7] == listt[26] or listt[8] == listt[26] or listt[9] == listt[26] or listt[10] == listt[26] or listt[11] == listt[26] or \
        listt[12] == listt[26] or listt[13] == listt[26] or listt[14] == listt[26] or listt[15] == listt[26] or listt[16] == listt[26] or listt[17] == listt[26] or listt[18] == listt[26] or listt[19] == listt[26] or listt[20] == listt[26] or \
        listt[21] == listt[26] or listt[22] == listt[26] or listt[23] == listt[26] or listt[24] == listt[26] or listt[25] == listt[26]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[26]))
    print("people count : 27")

elif listt[0] == listt[27] or listt[1] == listt[27] or listt[2] == listt[27] or listt[3] == listt[27] or listt[4] == listt[27] or listt[5] == listt[27] or listt[6] == listt[27] or listt[7] == listt[27] or listt[8] == listt[27] or listt[9] == listt[27] or listt[10] == listt[27] or listt[11] == listt[27] or \
        listt[12] == listt[27] or listt[13] == listt[27] or listt[14] == listt[27] or listt[15] == listt[27] or listt[16] == listt[27] or listt[17] == listt[27] or listt[18] == listt[27] or listt[19] == listt[27] or listt[20] == listt[27] or \
        listt[21] == listt[27] or listt[22] == listt[27] or listt[23] == listt[27] or listt[24] == listt[27] or listt[25] == listt[27] or listt[26] == listt[27]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[27]))
    print("people count : 28")

elif listt[0] == listt[28] or listt[1] == listt[28] or listt[2] == listt[28] or listt[3] == listt[28] or listt[4] == listt[28] or listt[5] == listt[28] or listt[6] == listt[28] or listt[7] == listt[28] or listt[8] == listt[28] or listt[9] == listt[28] or listt[10] == listt[28] or listt[11] == listt[28] or \
        listt[12] == listt[28] or listt[13] == listt[28] or listt[14] == listt[28] or listt[15] == listt[28] or listt[16] == listt[28] or listt[17] == listt[28] or listt[18] == listt[28] or listt[19] == listt[28] or listt[20] == listt[28] or \
        listt[21] == listt[28] or listt[22] == listt[28] or listt[23] == listt[28] or listt[24] == listt[28] or listt[25] == listt[28] or listt[26] == listt[28] or listt[27] == listt[28]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[28]))
    print("people count : 29")


elif listt[0] == listt[29] or listt[1] == listt[29] or listt[2] == listt[29] or listt[3] == listt[29] or listt[4] == listt[29] or listt[5] == listt[29] or listt[6] == listt[29] or listt[7] == listt[29] or listt[8] == listt[29] or listt[9] == listt[29] or listt[10] == listt[29] or listt[11] == listt[29] or \
        listt[12] == listt[29] or listt[13] == listt[29] or listt[14] == listt[29] or listt[15] == listt[29] or listt[16] == listt[29] or listt[17] == listt[29] or listt[18] == listt[29] or listt[19] == listt[29] or listt[20] == listt[29] or \
        listt[21] == listt[29] or listt[22] == listt[29] or listt[23] == listt[29] or listt[24] == listt[29] or listt[25] == listt[29] or listt[26] == listt[29] or listt[27] == listt[29] or listt[28] == listt[29]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[29]))
    print("people count : 30")

elif listt[0] == listt[30] or listt[1] == listt[30] or listt[2] == listt[30] or listt[3] == listt[30] or listt[4] == listt[30] or listt[5] == listt[30] or listt[6] == listt[30] or listt[7] == listt[30] or listt[8] == listt[30] or listt[9] == listt[30] or listt[10] == listt[30] or listt[11] == listt[30] or \
        listt[12] == listt[30] or listt[13] == listt[30] or listt[14] == listt[30] or listt[15] == listt[30] or listt[16] == listt[30] or listt[17] == listt[30] or listt[18] == listt[30] or listt[19] == listt[30] or listt[20] == listt[30] or \
        listt[21] == listt[30] or listt[22] == listt[30] or listt[23] == listt[30] or listt[24] == listt[30] or listt[25] == listt[30] or listt[26] == listt[30] or listt[27] == listt[30] or listt[28] == listt[30] or \
        listt[29] == listt[30]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[30]))
    print("people count : 31")

elif listt[0] == listt[31] or listt[1] == listt[31] or listt[2] == listt[31] or listt[3] == listt[31] or listt[4] == listt[31] or listt[5] == listt[31] or listt[6] == listt[31] or listt[7] == listt[31] or listt[8] == listt[31] or listt[9] == listt[31] or listt[10] == listt[31] or listt[11] == listt[31] or \
        listt[12] == listt[31] or listt[13] == listt[31] or listt[14] == listt[31] or listt[15] == listt[31] or listt[16] == listt[31] or listt[17] == listt[31] or listt[18] == listt[31] or listt[19] == listt[31] or listt[20] == listt[31] or \
        listt[21] == listt[31] or listt[22] == listt[31] or listt[23] == listt[31] or listt[24] == listt[31] or listt[25] == listt[31] or listt[26] == listt[31] or listt[27] == listt[31] or listt[28] == listt[31] or \
        listt[29] == listt[31] or listt[30] == listt[31]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[31]))
    print("people count : 32")

elif listt[0] == listt[32] or listt[1] == listt[32] or listt[2] == listt[32] or listt[3] == listt[32] or listt[4] == listt[32] or listt[5] == listt[32] or listt[6] == listt[32] or listt[7] == listt[32] or listt[8] == listt[32] or listt[9] == listt[32] or listt[10] == listt[32] or listt[11] == listt[32] or \
        listt[12] == listt[32] or listt[13] == listt[32] or listt[14] == listt[32] or listt[15] == listt[32] or listt[16] == listt[32] or listt[17] == listt[32] or listt[18] == listt[32] or listt[19] == listt[32] or listt[20] == listt[32] or \
        listt[21] == listt[32] or listt[22] == listt[32] or listt[23] == listt[32] or listt[24] == listt[32] or listt[25] == listt[32] or listt[26] == listt[32] or listt[27] == listt[32] or listt[28] == listt[32] or \
        listt[29] == listt[32] or listt[30] == listt[32] or listt[31] == listt[32]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[32]))
    print("people count : 33")

elif listt[0] == listt[33] or listt[1] == listt[33] or listt[2] == listt[33] or listt[3] == listt[33] or listt[4] == listt[33] or listt[5] == listt[33] or listt[6] == listt[33] or listt[7] == listt[33] or listt[8] == listt[33] or listt[9] == listt[33] or listt[10] == listt[33] or listt[11] == listt[33] or \
        listt[12] == listt[33] or listt[13] == listt[33] or listt[14] == listt[33] or listt[15] == listt[33] or listt[16] == listt[33] or listt[17] == listt[33] or listt[18] == listt[33] or listt[19] == listt[33] or listt[20] == listt[33] or \
        listt[21] == listt[33] or listt[22] == listt[33] or listt[23] == listt[33] or listt[24] == listt[33] or listt[25] == listt[33] or listt[26] == listt[33] or listt[27] == listt[33] or listt[28] == listt[33] or \
        listt[29] == listt[33] or listt[30] == listt[33] or listt[31] == listt[33] or listt[32] == listt[33]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[33]))
    print("people count : 34")

elif listt[0] == listt[34] or listt[1] == listt[34] or listt[2] == listt[34] or listt[3] == listt[34] or listt[4] == listt[34] or listt[5] == listt[34] or listt[6] == listt[34] or listt[7] == listt[34] or listt[8] == listt[34] or listt[9] == listt[34] or listt[10] == listt[34] or listt[11] == listt[34] or \
        listt[12] == listt[34] or listt[13] == listt[34] or listt[14] == listt[34] or listt[15] == listt[34] or listt[16] == listt[34] or listt[17] == listt[34] or listt[18] == listt[34] or listt[19] == listt[34] or listt[20] == listt[34] or \
        listt[21] == listt[34] or listt[22] == listt[34] or listt[23] == listt[34] or listt[24] == listt[34] or listt[25] == listt[34] or listt[26] == listt[34] or listt[27] == listt[34] or listt[28] == listt[34] or \
        listt[29] == listt[34] or listt[30] == listt[34] or listt[31] == listt[34] or listt[32] == listt[34] or listt[33] == listt[34]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[34]))
    print("people count : 35")

elif listt[0] == listt[35] or listt[1] == listt[35] or listt[2] == listt[35] or listt[3] == listt[35] or listt[4] == listt[35] or listt[5] == listt[35] or listt[6] == listt[35] or listt[7] == listt[35] or listt[8] == listt[35] or listt[9] == listt[35] or listt[10] == listt[35] or listt[11] == listt[35] or \
        listt[12] == listt[35] or listt[13] == listt[35] or listt[14] == listt[35] or listt[15] == listt[35] or listt[16] == listt[35] or listt[17] == listt[35] or listt[18] == listt[35] or listt[19] == listt[35] or listt[20] == listt[35] or \
        listt[21] == listt[35] or listt[22] == listt[35] or listt[23] == listt[35] or listt[24] == listt[35] or listt[25] == listt[35] or listt[26] == listt[35] or listt[27] == listt[35] or listt[28] == listt[35] or \
        listt[29] == listt[35] or listt[30] == listt[35] or listt[31] == listt[35] or listt[32] == listt[35] or listt[33] == listt[35] or listt[34] == listt[35]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[35]))
    print("people count : 36")

elif listt[0] == listt[36] or listt[1] == listt[36] or listt[2] == listt[36] or listt[3] == listt[36] or listt[4] == listt[36] or listt[5] == listt[36] or listt[6] == listt[36] or listt[7] == listt[36] or listt[8] == listt[36] or listt[9] == listt[36] or listt[10] == listt[36] or listt[11] == listt[36] or \
        listt[12] == listt[36] or listt[13] == listt[36] or listt[14] == listt[36] or listt[15] == listt[36] or listt[16] == listt[36] or listt[17] == listt[36] or listt[18] == listt[36] or listt[19] == listt[36] or listt[20] == listt[36] or \
        listt[21] == listt[36] or listt[22] == listt[36] or listt[23] == listt[36] or listt[24] == listt[36] or listt[25] == listt[36] or listt[26] == listt[36] or listt[27] == listt[36] or listt[28] == listt[36] or \
        listt[29] == listt[36] or listt[30] == listt[36] or listt[31] == listt[36] or listt[32] == listt[36] or listt[33] == listt[36] or listt[34] == listt[36] or listt[35] == listt[36]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[36]))
    print("people count : 37")

elif listt[0] == listt[37] or listt[1] == listt[37] or listt[2] == listt[37] or listt[3] == listt[37] or listt[4] == listt[37] or listt[5] == listt[37] or listt[6] == listt[37] or listt[7] == listt[37] or listt[8] == listt[37] or listt[9] == listt[37] or listt[10] == listt[37] or listt[11] == listt[37] or \
        listt[12] == listt[37] or listt[13] == listt[37] or listt[14] == listt[37] or listt[15] == listt[37] or listt[16] == listt[37] or listt[17] == listt[37] or listt[18] == listt[37] or listt[19] == listt[37] or listt[20] == listt[37] or \
        listt[21] == listt[37] or listt[22] == listt[37] or listt[23] == listt[37] or listt[24] == listt[37] or listt[25] == listt[37] or listt[26] == listt[37] or listt[27] == listt[37] or listt[28] == listt[37] or \
        listt[29] == listt[37] or listt[30] == listt[37] or listt[31] == listt[37] or listt[32] == listt[37] or listt[33] == listt[37] or listt[34] == listt[37] or listt[35] == listt[37] or \
        listt[36] == listt[37]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[37]))
    print("people count : 38")

elif listt[0] == listt[38] or listt[1] == listt[38] or listt[2] == listt[38] or listt[3] == listt[38] or listt[4] == listt[38] or listt[5] == listt[38] or listt[6] == listt[38] or listt[7] == listt[38] or listt[8] == listt[38] or listt[9] == listt[38] or listt[10] == listt[38] or listt[11] == listt[38] or \
        listt[12] == listt[38] or listt[13] == listt[38] or listt[14] == listt[38] or listt[15] == listt[38] or listt[16] == listt[38] or listt[17] == listt[38] or listt[18] == listt[38] or listt[19] == listt[38] or listt[20] == listt[38] or \
        listt[21] == listt[38] or listt[22] == listt[38] or listt[23] == listt[38] or listt[24] == listt[38] or listt[25] == listt[38] or listt[26] == listt[38] or listt[27] == listt[38] or listt[28] == listt[38] or \
        listt[29] == listt[38] or listt[30] == listt[38] or listt[31] == listt[38] or listt[32] == listt[38] or listt[33] == listt[38] or listt[34] == listt[38] or listt[35] == listt[38] or \
        listt[36] == listt[38] or listt[37] == listt[38]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[38]))
    print("people count : 39")

elif listt[0] == listt[39] or listt[1] == listt[39] or listt[2] == listt[39] or listt[3] == listt[39] or listt[4] == listt[39] or listt[5] == listt[39] or listt[6] == listt[39] or listt[7] == listt[39] or listt[8] == listt[39] or listt[9] == listt[39] or listt[10] == listt[39] or listt[11] == listt[39] or \
        listt[12] == listt[39] or listt[13] == listt[39] or listt[14] == listt[39] or listt[15] == listt[39] or listt[16] == listt[39] or listt[17] == listt[39] or listt[18] == listt[39] or listt[19] == listt[39] or listt[20] == listt[39] or \
        listt[21] == listt[39] or listt[22] == listt[39] or listt[23] == listt[39] or listt[24] == listt[39] or listt[25] == listt[39] or listt[26] == listt[39] or listt[27] == listt[39] or listt[28] == listt[39] or \
        listt[29] == listt[39] or listt[30] == listt[39] or listt[31] == listt[39] or listt[32] == listt[39] or listt[33] == listt[39] or listt[34] == listt[39] or listt[35] == listt[39] or \
        listt[36] == listt[39] or listt[37] == listt[39] or listt[38] == listt[39]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[39]))
    print("people count : 40")

elif listt[0] == listt[40] or listt[1] == listt[40] or listt[2] == listt[40] or listt[3] == listt[40] or listt[4] == listt[40] or listt[5] == listt[40] or listt[6] == listt[40] or listt[7] == listt[40] or listt[8] == listt[40] or listt[9] == listt[40] or listt[10] == listt[40] or listt[11] == listt[40] or \
        listt[12] == listt[40] or listt[13] == listt[40] or listt[14] == listt[40] or listt[15] == listt[40] or listt[16] == listt[40] or listt[17] == listt[40] or listt[18] == listt[40] or listt[19] == listt[40] or listt[20] == listt[40] or \
        listt[21] == listt[40] or listt[22] == listt[40] or listt[23] == listt[40] or listt[24] == listt[40] or listt[25] == listt[40] or listt[26] == listt[40] or listt[27] == listt[40] or listt[28] == listt[40] or \
        listt[29] == listt[40] or listt[30] == listt[40] or listt[31] == listt[40] or listt[32] == listt[40] or listt[33] == listt[40] or listt[34] == listt[40] or listt[35] == listt[40] or \
        listt[36] == listt[40] or listt[37] == listt[40] or listt[38] == listt[40] or listt[39] == listt[40]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[40]))
    print("people count : 41")

elif listt[0] == listt[41] or listt[1] == listt[41] or listt[2] == listt[41] or listt[3] == listt[41] or listt[4] == listt[41] or listt[5] == listt[41] or listt[6] == listt[41] or listt[7] == listt[41] or listt[8] == listt[41] or listt[9] == listt[41] or listt[10] == listt[41] or listt[11] == listt[41] or \
        listt[12] == listt[41] or listt[13] == listt[41] or listt[14] == listt[41] or listt[15] == listt[41] or listt[16] == listt[41] or listt[17] == listt[41] or listt[18] == listt[41] or listt[19] == listt[41] or listt[20] == listt[41] or \
        listt[21] == listt[41] or listt[22] == listt[41] or listt[23] == listt[41] or listt[24] == listt[41] or listt[25] == listt[41] or listt[26] == listt[41] or listt[27] == listt[41] or listt[28] == listt[41] or \
        listt[29] == listt[41] or listt[30] == listt[41] or listt[31] == listt[41] or listt[32] == listt[41] or listt[33] == listt[41] or listt[34] == listt[41] or listt[35] == listt[41] or \
        listt[36] == listt[41] or listt[37] == listt[41] or listt[38] == listt[41] or listt[39] == listt[41] or listt[40] == listt[41]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[41]))
    print("people count : 42")

elif listt[0] == listt[42] or listt[1] == listt[42] or listt[2] == listt[42] or listt[3] == listt[42] or listt[4] == listt[42] or listt[5] == listt[42] or listt[6] == listt[42] or listt[7] == listt[42] or listt[8] == listt[42] or listt[9] == listt[42] or listt[10] == listt[42] or listt[11] == listt[42] or \
        listt[12] == listt[42] or listt[13] == listt[42] or listt[14] == listt[42] or listt[15] == listt[42] or listt[16] == listt[42] or listt[17] == listt[42] or listt[18] == listt[42] or listt[19] == listt[42] or listt[20] == listt[42] or \
        listt[21] == listt[42] or listt[22] == listt[42] or listt[23] == listt[42] or listt[24] == listt[42] or listt[25] == listt[42] or listt[26] == listt[42] or listt[27] == listt[42] or listt[28] == listt[42] or \
        listt[29] == listt[42] or listt[30] == listt[42] or listt[31] == listt[42] or listt[32] == listt[42] or listt[33] == listt[42] or listt[34] == listt[42] or listt[35] == listt[42] or \
        listt[36] == listt[42] or listt[37] == listt[42] or listt[38] == listt[42] or listt[39] == listt[42] or listt[40] == listt[42] or listt[41] == listt[42]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[42]))
    print("people count : 43")

elif listt[0] == listt[43] or listt[1] == listt[43] or listt[2] == listt[43] or listt[3] == listt[43] or listt[4] == listt[43] or listt[5] == listt[43] or listt[6] == listt[43] or listt[7] == listt[43] or listt[8] == listt[43] or listt[9] == listt[43] or listt[10] == listt[43] or listt[11] == listt[43] or \
        listt[12] == listt[43] or listt[13] == listt[43] or listt[14] == listt[43] or listt[15] == listt[43] or listt[16] == listt[43] or listt[17] == listt[43] or listt[18] == listt[43] or listt[19] == listt[43] or listt[20] == listt[43] or \
        listt[21] == listt[43] or listt[22] == listt[43] or listt[23] == listt[43] or listt[24] == listt[43] or listt[25] == listt[43] or listt[26] == listt[43] or listt[27] == listt[43] or listt[28] == listt[43] or \
        listt[29] == listt[43] or listt[30] == listt[43] or listt[31] == listt[43] or listt[32] == listt[43] or listt[33] == listt[43] or listt[34] == listt[43] or listt[35] == listt[43] or \
        listt[36] == listt[43] or listt[37] == listt[43] or listt[38] == listt[43] or listt[39] == listt[43] or listt[40] == listt[43] or listt[41] == listt[43] or listt[42] == listt[43]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[43]))
    print("people count : 44")

elif listt[0] == listt[44] or listt[1] == listt[44] or listt[2] == listt[44] or listt[3] == listt[44] or listt[4] == listt[44] or listt[5] == listt[44] or listt[6] == listt[44] or listt[7] == listt[44] or listt[8] == listt[44] or listt[9] == listt[44] or listt[10] == listt[44] or listt[11] == listt[44] or \
        listt[12] == listt[44] or listt[13] == listt[44] or listt[14] == listt[44] or listt[15] == listt[44] or listt[16] == listt[44] or listt[17] == listt[44] or listt[18] == listt[44] or listt[19] == listt[44] or listt[20] == listt[44] or \
        listt[21] == listt[44] or listt[22] == listt[44] or listt[23] == listt[44] or listt[24] == listt[44] or listt[25] == listt[44] or listt[26] == listt[44] or listt[27] == listt[44] or listt[28] == listt[44] or \
        listt[29] == listt[44] or listt[30] == listt[44] or listt[31] == listt[44] or listt[32] == listt[44] or listt[33] == listt[44] or listt[34] == listt[44] or listt[35] == listt[44] or \
        listt[36] == listt[44] or listt[37] == listt[44] or listt[38] == listt[44] or listt[39] == listt[44] or listt[40] == listt[44] or listt[41] == listt[44] or listt[42] == listt[44] or \
        listt[43] == listt[44]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[44]))
    print("people count : 45")


elif listt[0] == listt[45] or listt[1] == listt[45] or listt[2] == listt[45] or listt[3] == listt[45] or listt[4] == listt[45] or listt[5] == listt[45] or listt[6] == listt[45] or listt[7] == listt[45] or listt[8] == listt[45] or listt[9] == listt[45] or listt[10] == listt[45] or listt[11] == listt[45] or \
        listt[12] == listt[45] or listt[13] == listt[45] or listt[14] == listt[45] or listt[15] == listt[45] or listt[16] == listt[45] or listt[17] == listt[45] or listt[18] == listt[45] or listt[19] == listt[45] or listt[20] == listt[45] or \
        listt[21] == listt[45] or listt[22] == listt[45] or listt[23] == listt[45] or listt[24] == listt[45] or listt[25] == listt[45] or listt[26] == listt[45] or listt[27] == listt[45] or listt[28] == listt[45] or \
        listt[29] == listt[45] or listt[30] == listt[45] or listt[31] == listt[45] or listt[32] == listt[45] or listt[33] == listt[45] or listt[34] == listt[45] or listt[35] == listt[45] or \
        listt[36] == listt[45] or listt[37] == listt[45] or listt[38] == listt[45] or listt[39] == listt[45] or listt[40] == listt[45] or listt[41] == listt[45] or listt[42] == listt[45] or \
        listt[43] == listt[45] or listt[44] == listt[45]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[45]))
    print("people count : 46")

elif listt[0] == listt[46] or listt[1] == listt[46] or listt[2] == listt[46] or listt[3] == listt[46] or listt[4] == listt[46] or listt[5] == listt[46] or listt[6] == listt[46] or listt[7] == listt[46] or listt[8] == listt[46] or listt[9] == listt[46] or listt[10] == listt[46] or listt[11] == listt[46] or \
        listt[12] == listt[46] or listt[13] == listt[46] or listt[14] == listt[46] or listt[15] == listt[46] or listt[16] == listt[46] or listt[17] == listt[46] or listt[18] == listt[46] or listt[19] == listt[46] or listt[20] == listt[46] or \
        listt[21] == listt[46] or listt[22] == listt[46] or listt[23] == listt[46] or listt[24] == listt[46] or listt[25] == listt[46] or listt[26] == listt[46] or listt[27] == listt[46] or listt[28] == listt[46] or \
        listt[29] == listt[46] or listt[30] == listt[46] or listt[31] == listt[46] or listt[32] == listt[46] or listt[33] == listt[46] or listt[34] == listt[46] or listt[35] == listt[46] or \
        listt[36] == listt[46] or listt[37] == listt[46] or listt[38] == listt[46] or listt[39] == listt[46] or listt[40] == listt[46] or listt[41] == listt[46] or listt[42] == listt[46] or \
        listt[43] == listt[46] or listt[44] == listt[46] or listt[45] == listt[46]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[46]))
    print("people count : 47")

elif listt[0] == listt[47] or listt[1] == listt[47] or listt[2] == listt[47] or listt[3] == listt[47] or listt[4] == listt[47] or listt[5] == listt[47] or listt[6] == listt[47] or listt[7] == listt[47] or listt[8] == listt[47] or listt[9] == listt[47] or listt[10] == listt[47] or listt[11] == listt[47] or \
        listt[12] == listt[47] or listt[13] == listt[47] or listt[14] == listt[47] or listt[15] == listt[47] or listt[16] == listt[47] or listt[17] == listt[47] or listt[18] == listt[47] or listt[19] == listt[47] or listt[20] == listt[47] or \
        listt[21] == listt[47] or listt[22] == listt[47] or listt[23] == listt[47] or listt[24] == listt[47] or listt[25] == listt[47] or listt[26] == listt[47] or listt[27] == listt[47] or listt[28] == listt[47] or \
        listt[29] == listt[47] or listt[30] == listt[47] or listt[31] == listt[47] or listt[32] == listt[47] or listt[33] == listt[47] or listt[34] == listt[47] or listt[35] == listt[47] or \
        listt[36] == listt[47] or listt[37] == listt[47] or listt[38] == listt[47] or listt[39] == listt[47] or listt[40] == listt[47] or listt[41] == listt[47] or listt[42] == listt[47] or \
        listt[43] == listt[47] or listt[44] == listt[47] or listt[45] == listt[47] or listt[46] == listt[47]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[47]))
    print("people count : 48")

elif listt[0] == listt[48] or listt[1] == listt[48] or listt[2] == listt[48] or listt[3] == listt[48] or listt[4] == listt[48] or listt[5] == listt[48] or listt[6] == listt[48] or listt[7] == listt[48] or listt[8] == listt[48] or listt[9] == listt[48] or listt[10] == listt[48] or listt[11] == listt[48] or \
        listt[12] == listt[48] or listt[13] == listt[48] or listt[14] == listt[48] or listt[15] == listt[48] or listt[16] == listt[48] or listt[17] == listt[48] or listt[18] == listt[48] or listt[19] == listt[48] or listt[20] == listt[48] or \
        listt[21] == listt[48] or listt[22] == listt[48] or listt[23] == listt[48] or listt[24] == listt[48] or listt[25] == listt[48] or listt[26] == listt[48] or listt[27] == listt[48] or listt[28] == listt[48] or \
        listt[29] == listt[48] or listt[30] == listt[48] or listt[31] == listt[48] or listt[32] == listt[48] or listt[33] == listt[48] or listt[34] == listt[48] or listt[35] == listt[48] or \
        listt[36] == listt[48] or listt[37] == listt[48] or listt[38] == listt[48] or listt[39] == listt[48] or listt[40] == listt[48] or listt[41] == listt[48] or listt[42] == listt[48] or \
        listt[43] == listt[48] or listt[44] == listt[48] or listt[45] == listt[48] or listt[46] == listt[48] or listt[47] == listt[48]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[48]))
    print("people count : 49")

elif listt[0] == listt[49] or listt[1] == listt[49] or listt[2] == listt[49] or listt[3] == listt[49] or listt[4] == listt[49] or listt[5] == listt[49] or listt[6] == listt[49] or listt[7] == listt[49] or listt[8] == listt[49] or listt[9] == listt[49] or listt[10] == listt[49] or listt[11] == listt[49] or \
        listt[12] == listt[49] or listt[13] == listt[49] or listt[14] == listt[49] or listt[15] == listt[49] or listt[16] == listt[49] or listt[17] == listt[49] or listt[18] == listt[49] or listt[19] == listt[49] or listt[20] == listt[49] or \
        listt[21] == listt[49] or listt[22] == listt[49] or listt[23] == listt[49] or listt[24] == listt[49] or listt[25] == listt[49] or listt[26] == listt[49] or listt[27] == listt[49] or listt[28] == listt[49] or \
        listt[29] == listt[49] or listt[30] == listt[49] or listt[31] == listt[49] or listt[32] == listt[49] or listt[33] == listt[49] or listt[34] == listt[49] or listt[35] == listt[49] or \
        listt[36] == listt[49] or listt[37] == listt[49] or listt[38] == listt[49] or listt[39] == listt[49] or listt[40] == listt[49] or listt[41] == listt[49] or listt[42] == listt[49] or \
        listt[43] == listt[49] or listt[44] == listt[49] or listt[45] == listt[49] or listt[46] == listt[49] or listt[47] == listt[49] or listt[48] == listt[49]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[49]))
    print("people count : 50")

elif listt[0] == listt[50] or listt[1] == listt[50] or listt[2] == listt[50] or listt[3] == listt[50] or listt[4] == listt[50] or listt[5] == listt[50] or listt[6] == listt[50] or listt[7] == listt[50] or listt[8] == listt[50] or listt[9] == listt[50] or listt[10] == listt[50] or listt[11] == listt[50] or \
        listt[12] == listt[50] or listt[13] == listt[50] or listt[14] == listt[50] or listt[15] == listt[50] or listt[16] == listt[50] or listt[17] == listt[50] or listt[18] == listt[50] or listt[19] == listt[50] or listt[20] == listt[50] or \
        listt[21] == listt[50] or listt[22] == listt[50] or listt[23] == listt[50] or listt[24] == listt[50] or listt[25] == listt[50] or listt[26] == listt[50] or listt[27] == listt[50] or listt[28] == listt[50] or \
        listt[29] == listt[50] or listt[30] == listt[50] or listt[31] == listt[50] or listt[32] == listt[50] or listt[33] == listt[50] or listt[34] == listt[50] or listt[35] == listt[50] or \
        listt[36] == listt[50] or listt[37] == listt[50] or listt[38] == listt[50] or listt[39] == listt[50] or listt[40] == listt[50] or listt[41] == listt[50] or listt[42] == listt[50] or \
        listt[43] == listt[50] or listt[44] == listt[50] or listt[45] == listt[50] or listt[46] == listt[50] or listt[47] == listt[50] or listt[48] == listt[50] or listt[49] == listt[50]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[50]))
    print("people count : 51")

elif listt[0] == listt[51] or listt[1] == listt[51] or listt[2] == listt[51] or listt[3] == listt[51] or listt[4] == listt[51] or listt[5] == listt[51] or listt[6] == listt[51] or listt[7] == listt[51] or listt[8] == listt[51] or listt[9] == listt[51] or listt[10] == listt[51] or listt[11] == listt[51] or \
        listt[12] == listt[51] or listt[13] == listt[51] or listt[14] == listt[51] or listt[15] == listt[51] or listt[16] == listt[51] or listt[17] == listt[51] or listt[18] == listt[51] or listt[19] == listt[51] or listt[20] == listt[51] or \
        listt[21] == listt[51] or listt[22] == listt[51] or listt[23] == listt[51] or listt[24] == listt[51] or listt[25] == listt[51] or listt[26] == listt[51] or listt[27] == listt[51] or listt[28] == listt[51] or \
        listt[29] == listt[51] or listt[30] == listt[51] or listt[31] == listt[51] or listt[32] == listt[51] or listt[33] == listt[51] or listt[34] == listt[51] or listt[35] == listt[51] or \
        listt[36] == listt[51] or listt[37] == listt[51] or listt[38] == listt[51] or listt[39] == listt[51] or listt[40] == listt[51] or listt[41] == listt[51] or listt[42] == listt[51] or \
        listt[43] == listt[51] or listt[44] == listt[51] or listt[45] == listt[51] or listt[46] == listt[51] or listt[47] == listt[51] or listt[48] == listt[51] or listt[49] == listt[51] or \
        listt[50] == listt[51]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[51]))
    print("people count : 52")

elif listt[0] == listt[52] or listt[1] == listt[52] or listt[2] == listt[52] or listt[3] == listt[52] or listt[4] == listt[52] or listt[5] == listt[52] or listt[6] == listt[52] or listt[7] == listt[52] or listt[8] == listt[52] or listt[9] == listt[52] or listt[10] == listt[52] or listt[11] == listt[52] or \
        listt[12] == listt[52] or listt[13] == listt[52] or listt[14] == listt[52] or listt[15] == listt[52] or listt[16] == listt[52] or listt[17] == listt[52] or listt[18] == listt[52] or listt[19] == listt[52] or listt[20] == listt[52] or \
        listt[21] == listt[52] or listt[22] == listt[52] or listt[23] == listt[52] or listt[24] == listt[52] or listt[25] == listt[52] or listt[26] == listt[52] or listt[27] == listt[52] or listt[28] == listt[52] or \
        listt[29] == listt[52] or listt[30] == listt[52] or listt[31] == listt[52] or listt[32] == listt[52] or listt[33] == listt[52] or listt[34] == listt[52] or listt[35] == listt[52] or \
        listt[36] == listt[52] or listt[37] == listt[52] or listt[38] == listt[52] or listt[39] == listt[52] or listt[40] == listt[52] or listt[41] == listt[52] or listt[42] == listt[52] or \
        listt[43] == listt[52] or listt[44] == listt[52] or listt[45] == listt[52] or listt[46] == listt[52] or listt[47] == listt[52] or listt[48] == listt[52] or listt[49] == listt[52] or \
        listt[50] == listt[52] or listt[51] == listt[52]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[52]))
    print("people count : 53")

elif listt[0] == listt[53] or listt[1] == listt[53] or listt[2] == listt[53] or listt[3] == listt[53] or listt[4] == listt[53] or listt[5] == listt[53] or listt[6] == listt[53] or listt[7] == listt[53] or listt[8] == listt[53] or listt[9] == listt[53] or listt[10] == listt[53] or listt[11] == listt[53] or \
        listt[12] == listt[53] or listt[13] == listt[53] or listt[14] == listt[53] or listt[15] == listt[53] or listt[16] == listt[53] or listt[17] == listt[53] or listt[18] == listt[53] or listt[19] == listt[53] or listt[20] == listt[53] or \
        listt[21] == listt[53] or listt[22] == listt[53] or listt[23] == listt[53] or listt[24] == listt[53] or listt[25] == listt[53] or listt[26] == listt[53] or listt[27] == listt[53] or listt[28] == listt[53] or \
        listt[29] == listt[53] or listt[30] == listt[53] or listt[31] == listt[53] or listt[32] == listt[53] or listt[33] == listt[53] or listt[34] == listt[53] or listt[35] == listt[53] or \
        listt[36] == listt[53] or listt[37] == listt[53] or listt[38] == listt[53] or listt[39] == listt[53] or listt[40] == listt[53] or listt[41] == listt[53] or listt[42] == listt[53] or \
        listt[43] == listt[53] or listt[44] == listt[53] or listt[45] == listt[53] or listt[46] == listt[53] or listt[47] == listt[53] or listt[48] == listt[53] or listt[49] == listt[53] or \
        listt[50] == listt[53] or listt[51] == listt[53] or listt[52] == listt[53]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[53]))
    print("people count : 54")

elif listt[0] == listt[54] or listt[1] == listt[54] or listt[2] == listt[54] or listt[3] == listt[54] or listt[4] == listt[54] or listt[5] == listt[54] or listt[6] == listt[54] or listt[7] == listt[54] or listt[8] == listt[54] or listt[9] == listt[54] or listt[10] == listt[54] or listt[11] == listt[54] or \
        listt[12] == listt[54] or listt[13] == listt[54] or listt[14] == listt[54] or listt[15] == listt[54] or listt[16] == listt[54] or listt[17] == listt[54] or listt[18] == listt[54] or listt[19] == listt[54] or listt[20] == listt[54] or \
        listt[21] == listt[54] or listt[22] == listt[54] or listt[23] == listt[54] or listt[24] == listt[54] or listt[25] == listt[54] or listt[26] == listt[54] or listt[27] == listt[54] or listt[28] == listt[54] or \
        listt[29] == listt[54] or listt[30] == listt[54] or listt[31] == listt[54] or listt[32] == listt[54] or listt[33] == listt[54] or listt[34] == listt[54] or listt[35] == listt[54] or \
        listt[36] == listt[54] or listt[37] == listt[54] or listt[38] == listt[54] or listt[39] == listt[54] or listt[40] == listt[54] or listt[41] == listt[54] or listt[42] == listt[54] or \
        listt[43] == listt[54] or listt[44] == listt[54] or listt[45] == listt[54] or listt[46] == listt[54] or listt[47] == listt[54] or listt[48] == listt[54] or listt[49] == listt[54] or \
        listt[50] == listt[54] or listt[51] == listt[54] or listt[52] == listt[54] or listt[53] == listt[54]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[54]))
    print("people count : 55")

elif listt[0] == listt[55] or listt[1] == listt[55] or listt[2] == listt[55] or listt[3] == listt[55] or listt[4] == listt[55] or listt[5] == listt[55] or listt[6] == listt[55] or listt[7] == listt[55] or listt[8] == listt[55] or listt[9] == listt[55] or listt[10] == listt[55] or listt[11] == listt[55] or \
        listt[12] == listt[55] or listt[13] == listt[55] or listt[14] == listt[55] or listt[15] == listt[55] or listt[16] == listt[55] or listt[17] == listt[55] or listt[18] == listt[55] or listt[19] == listt[55] or listt[20] == listt[55] or \
        listt[21] == listt[55] or listt[22] == listt[55] or listt[23] == listt[55] or listt[24] == listt[55] or listt[25] == listt[55] or listt[26] == listt[55] or listt[27] == listt[55] or listt[28] == listt[55] or \
        listt[29] == listt[55] or listt[30] == listt[55] or listt[31] == listt[55] or listt[32] == listt[55] or listt[33] == listt[55] or listt[34] == listt[55] or listt[35] == listt[55] or \
        listt[36] == listt[55] or listt[37] == listt[55] or listt[38] == listt[55] or listt[39] == listt[55] or listt[40] == listt[55] or listt[41] == listt[55] or listt[42] == listt[55] or \
        listt[43] == listt[55] or listt[44] == listt[55] or listt[45] == listt[55] or listt[46] == listt[55] or listt[47] == listt[55] or listt[48] == listt[55] or listt[49] == listt[55] or \
        listt[50] == listt[55] or listt[51] == listt[55] or listt[52] == listt[55] or listt[53] == listt[55] or listt[54] == listt[55]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[55]))
    print("people count : 56")

elif listt[0] == listt[56] or listt[1] == listt[56] or listt[2] == listt[56] or listt[3] == listt[56] or listt[4] == listt[56] or listt[5] == listt[56] or listt[6] == listt[56] or listt[7] == listt[56] or listt[8] == listt[56] or listt[9] == listt[56] or listt[10] == listt[56] or listt[11] == listt[56] or \
        listt[12] == listt[56] or listt[13] == listt[56] or listt[14] == listt[56] or listt[15] == listt[56] or listt[16] == listt[56] or listt[17] == listt[56] or listt[18] == listt[56] or listt[19] == listt[56] or listt[20] == listt[56] or \
        listt[21] == listt[56] or listt[22] == listt[56] or listt[23] == listt[56] or listt[24] == listt[56] or listt[25] == listt[56] or listt[26] == listt[56] or listt[27] == listt[56] or listt[28] == listt[56] or \
        listt[29] == listt[56] or listt[30] == listt[56] or listt[31] == listt[56] or listt[32] == listt[56] or listt[33] == listt[56] or listt[34] == listt[56] or listt[35] == listt[56] or \
        listt[36] == listt[56] or listt[37] == listt[56] or listt[38] == listt[56] or listt[39] == listt[56] or listt[40] == listt[56] or listt[41] == listt[56] or listt[42] == listt[56] or \
        listt[43] == listt[56] or listt[44] == listt[56] or listt[45] == listt[56] or listt[46] == listt[56] or listt[47] == listt[56] or listt[48] == listt[56] or listt[49] == listt[56] or \
        listt[50] == listt[56] or listt[51] == listt[56] or listt[52] == listt[56] or listt[53] == listt[56] or listt[54] == listt[56] or listt[55] == listt[56]:
    print("birthdate of the person who born in the same day with another person:", end=" ")
    print(day_finder(listt[56]))
    print("people count : 57")

else: print("first 57 person have different birthdate. It is very rare possibility, less than %1 !!!")
