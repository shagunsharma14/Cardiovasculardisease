from django.shortcuts import render
from Cardiovasculardiseaseapp.models import users
from Cardiovasculardiseaseapp.models import udetails

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Create your views here.

def loginview(request):
    return render(request,'login.html')

def regview(request):
    return render(request,'reg.html')

def saveuserview(request):
    vname=request.POST["rname"]
    vemail=request.POST["remail"]
    vaddress=request.POST["raddress"]
    vpnum=request.POST["rpnum"]
    vusername=request.POST["rusername"]
    vpassword=request.POST["rpassword"]
    newuser=users(name=vname,pnum=vpnum,email=vemail,address=vaddress,username=vusername,password=vpassword)
    newuser.save()
    return render(request,'login.html')

def loginuserview(request):
    usern=request.POST["lusername"]
    pswd=request.POST["lpassword"]
    luser=users.objects.filter(username=usern)
    for u in luser:
        if u.password==pswd:
            return render(request,'home.html')
        else:
            return render(request,'login.html')

## ORIGINAL ####
# def userdetailsview(request):
#     vage=request.POST["hage"]
#     vgender=request.POST["hgender"]
#     vheight=request.POST["hheight"]
#     vweight=request.POST["hweight"]
#     vsystolic=request.POST["hsystolic"]
#     vdiastolic=request.POST["hdiastolic"]
#     vcholestrol=request.POST["hcholestrol"]
#     vcglucose=request.POST["hglucose"]
#     vsmoke=request.POST["hsmoke"]
#     valchohol=request.POST["halchohol"]
#     vactive=request.POST["hactive"]

#     # details=udetails(pregnancies=vpregnancies,glucose=vglucose,bp=vbp,skinthick=vskinthick,insulin=vinsulin,bmi=vbmi,dpf=vdpf,age=vage)
#     # details.save()

#     dataset=pd.read_csv("cardio_train.csv")

#     x=dataset.iloc[:,:-1]
#     y=dataset.iloc[:,-1]

#     xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=30,random_state=1) #test size=0.10 or train size=0.90
#     model=RandomForestClassifier(random_state=48)
#     model.fit(xtrain,ytrain)

#     #p=np.array([6,148,72.0,35,0,33.6,0.627,50]).reshape(1,-1)
#     p=np.array([vage,vgender,vheight,vweight,vsystolic,vdiastolic,vcholestrol,vcglucose,vsmoke,valchohol,vactive]).reshape(1,-1)

#     predicted_result=model.predict(p)
#     predicted_result[0]

#     if predicted_result[0]==1:
#         print("You have Cardiovascular disease")
#         result="You have Cardiovascular disease"
#     else:
#         print("You are Normal")
#         result="You are Normal"

#     return render(request,'result.html',{'result':result})


####### MODIFIED ######
def userdetailsview(request):
    vage=request.POST["hage"]
    vgender=request.POST["hgender"]
    vheight=request.POST["hheight"]
    vweight=request.POST["hweight"]
    vsystolic=request.POST["hsystolic"]
    vdiastolic=request.POST["hdiastolic"]
    vcholestrol=request.POST["hcholestrol"]
    vcglucose=request.POST["hglucose"]
    vsmoke=request.POST["hsmoke"]
    valchohol=request.POST["halchohol"]
    vactive=request.POST["hactive"]

    # details=udetails(pregnancies=vpregnancies,glucose=vglucose,bp=vbp,skinthick=vskinthick,insulin=vinsulin,bmi=vbmi,dpf=vdpf,age=vage)
    # details.save()

    dataset=pd.read_csv("cardio_train.csv")
    print(dataset)
    
    # x=dataset.iloc[:,:-1]
    # x = dataset.iloc[:, 1:-1]
    x = dataset.drop(columns=['id', 'cardio'])
    print('x: ',x)

    y = dataset['cardio']
    print('y: ',y)


    # y=dataset.iloc[:,-1]
    # y = dataset.iloc[:, :-1]

    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=30,random_state=1) #test size=0.10 or train size=0.90
    model=RandomForestClassifier(random_state=48)
    model.fit(xtrain,ytrain)

    #p=np.array([6,148,72.0,35,0,33.6,0.627,50]).reshape(1,-1)
    p=np.array([vage,vgender,vheight,vweight,vsystolic,vdiastolic,vcholestrol,vcglucose,vsmoke,valchohol,vactive]).reshape(1,-1)

    predicted_result=model.predict(p)
    predicted_result[0]

    if predicted_result[0]==1:
        print("You have Cardiovascular disease")
        result="You have Cardiovascular disease"
    else:
        print("You are Normal")
        result="You are Normal"

    return render(request,'result.html',{'result':result})