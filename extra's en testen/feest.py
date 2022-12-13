gastheer=True
gasten=True
drank=True
chips=True

if gastheer==True or gasten==True and drank==True and chips==True or gastheer==True and gasten==True and chips==False and drank==False:
    print("start de party")
else: 
    gastheer==False or drank==False and chips==True or gastheer==False and gasten==True and chips==False and drank==False or gastheer==False and gasten==False or gastheer==False and gasten==False and chips==True and drank==False
    print("no party")