from tkinter import *
import CMSBLL
from CMSBLL import Customer
from tkinter import messagebox

def addCustData():
        "Creating object of customer class and save data in the object and call add method of customer class"
        cus=Customer()
        cus.firstName = varfirstName.get()
        cus.lastName = varLastName.get()
        cus.age = varAge.get()
        cus.mobileNo = varMobile.get()
        cus.emailId = varEmail.get()
        cus.address = varAdd.get()
        cus.city = varCity.get()
        cus.state = varState.get()
        cus.pincode = varPincode.get()
        cus.country = varCountry.get()
        cus.addCustomer()#calling of add method of customer class
        messagebox.showinfo("AJT CMS","Customer Added successfully")
        fr3.destroy()
        fr2gen()

def displayData(values):  # Displaying cust information
    global root1
    root1 = Tk()
    lblId1 = Label(root1, text="Cust ID", font=16, width=12, bg="orange")
    lblId1.grid(row=0, column=0)
    lblfname1 = Label(root1, text="Cust Fname", font=16, width=12, bg="orange")
    lblfname1.grid(row=0, column=1)
    lblLname1 = Label(root1, text="Cust Lname", font=16, width=12, bg="orange")
    lblLname1.grid(row=0, column=2)
    lblAge1 = Label(root1, text="Cust Age", font=16, width=12, bg="orange")
    lblAge1.grid(row=0, column=3)
    lblmobno1 = Label(root1, text="Cust MobileNo", font=16, width=12, bg="orange")
    lblmobno1.grid(row=0, column=4)
    lblEid1 = Label(root1, text="Cust Email", font=16, width=12, bg="orange")
    lblEid1.grid(row=0, column=5)
    lblEid1 = Label(root1, text="Cust Address", font=16, width=12, bg="orange")
    lblEid1.grid(row=0, column=6)
    lblcity1 = Label(root1, text="Cust City", font=16, width=12, bg="orange")
    lblcity1.grid(row=0, column=7)
    lblstate1 = Label(root1, text="Cust State", font=16, width=12, bg="orange")
    lblstate1.grid(row=0, column=8)
    lblpincode1 = Label(root1, text="Cust Pincode", font=16, width=12, bg="orange")
    lblpincode1.grid(row=0, column=9)
    lblcountry1 = Label(root1, text="Cust country", font=16, width=12, bg="orange")
    lblcountry1.grid(row=0, column=10)
    k = 1
    for e in range(len(values)):
        i = 0
        for j in range(len(values[e])):
            lblId2 = Label(root1, text=values[e][j], font=16, width=12, bg="yellow", wraplength=120, height=2,
                           justify="left")
            lblId2.grid(row=k, column=i)
            i += 1
        k += 1

def notFound():#Customer does not exist
    messagebox.showinfo("NOT FOUND", "Customer does not exits")
    fra.destroy()

def searchcust(val):  # Retrive data from database
    global values
    if val == 1:
        values = Customer.searchcust(cuInfo.get())
        displayData(values)
        fra.destroy()
        fr2gen()
    else:
        notFound()
        fr2gen()

def checkCustExistence():  # Check whether cust exist or not for searching
    val = Customer.checkexits(cuInfo.get())
    searchcust(val)

def modifyCust(val):#Modify Customer
    if val == 1:
        modifyFrame()
    else:
        notFound()
        fr2gen()

def modifycustcheck():  # Check whether cust data avialable or not for modification
    val = Customer.checkexits(custData.get())
    modifyCust(val)

def modifyData():#Modifying data
    cus=CMSBLL.Customer()
    cus.firstName = varfirstUName.get()
    cus.lastName = varLastUName.get()
    cus.age = varUAge.get()
    cus.mobileNo = varUMobile.get()
    cus.emailId = varUEmail.get()
    cus.address = varUAdd.get()
    cus.city = varUCity.get()
    cus.state = varUState.get()
    cus.pincode = varUPincode.get()
    cus.country = varUCountry.get()
    cus.modifyCustomer()
    messagebox.showinfo("AJT CMS","Customer Data Modified Successfully")
    fr5.destroy()
    fr2gen()

def deletecust(val):#Delete customer
    if val == 1:
        Customer.deleteCustomer(custinfo.get())
        messagebox.showinfo("DELETE CUSTOMER","Customer Deleted Successfully")
        fr2gen()
        fra.destroy()
    else:
        notFound()
        fr2gen()

def deletecustcheck():#Check whether cust is in DB or not for deletion
    val = Customer.checkexits(custinfo.get())
    deletecust(val)

def displaybut_click():#Retriveing data from DB for display
    val = Customer.displayAllCustomer()
    displayData(val)

def showfr2():#called by addbut_click when delete button clicked
    fr3.destroy()
    fr2gen()

def addbut_click():#Add button clicked and asking for customer information
    fr2.destroy()
    global fr3
    fr3 = Frame(root)
    fr3.pack(side="top", pady=20)
    fr3.config(bd=5,bg='pink')
    global varfirstName,varLastName,varAge,varMobile,varEmail,varAdd,varCity,varState,varPincode,varCountry

    lblcomp= Label(fr3,width=20,text="* Mandatory fields",font=("Arial Black",10))
    lblcomp.grid(row=0,column=0,pady=5)
    lblfirstName = Label(fr3, width=20, text="*Enter Cust First Name:", font=("Times New Roman",20))
    lblfirstName.grid(row=1,column=0)
    varfirstName = StringVar()
    entryfirstName = Entry(fr3,width=20,font=("Times New Roman",20), textvariable=varfirstName)
    entryfirstName.grid(row=1,column=1)

    lblLastName = Label(fr3,width=20, text="Enter Cust Last Name:", font=("Times New Roman", 20))
    lblLastName.grid(row=2, column=0,pady="10")
    varLastName = StringVar()
    entryLastName = Entry(fr3,width=20, font=("Times New Roman", 20), textvariable=varLastName)
    entryLastName.grid(row=2, column=1,pady="10")

    lblAge =Label(fr3,width=20,text="*Enter Customer Age:",font=("Times New Roman", 20))
    lblAge.grid(row=3,column=0)
    varAge= StringVar()
    entryAge=Entry(fr3,width=20,font=("Times New Roman", 20),textvariable=varAge)
    entryAge.grid(row=3,column=1)

    lblMobile = Label(fr3,width=20, text="*Enter Cust Mobile No:", font=("Times New Roman",20))
    lblMobile.grid(row=4,column=0,pady="10")
    varMobile = StringVar()
    entryMobile = Entry(fr3, width=20,font=("Times New Roman",20), textvariable=varMobile)
    entryMobile.grid(row=4,column=1,pady="10")

    lblEmail =Label(fr3,width=20,text="*Enter Cust EmailId:", font=("Times New Roman",20))
    lblEmail.grid(row=5,column=0)
    varEmail=StringVar()
    entryEmail =Entry(fr3,width=20,font=("Times New Roman",20),textvariable=varEmail)
    entryEmail.grid(row=5,column=1)

    lblAdd = Label(fr3,width=20, text="Enter Cust Address:", font=("Times New Roman",20))
    lblAdd.grid(row=1,column=3,padx="10")
    varAdd=StringVar()
    entryADD=Entry(fr3,width=20,font=("Times New Roman",20),textvariable=varAdd)
    entryADD.grid(row=1,column=4)

    lblCity =Label(fr3,width=20,text="*Enter Cust City:",font=("Times New Roman",20))
    lblCity.grid(row=2,column=3,padx="10")
    varCity=StringVar()
    entryCity=Entry(fr3,width=20,font=("Times New Roman",20),textvariable=varCity)
    entryCity.grid(row=2,column=4)

    lblState =Label(fr3,width=20,text="*Enter Cust State:",font=("Times New Roman",20))
    lblState.grid(row=3,column=3,padx="10")
    varState=StringVar()
    entryState=Entry(fr3,width=20,font=("Times New Roman",20),textvariable=varState)
    entryState.grid(row=3,column=4)

    lblPincode =Label(fr3,width=20,text="*Enter Cust pincode:",font=("Times New Roman",20))
    lblPincode.grid(row=4,column=3,padx="10")
    varPincode=StringVar()
    entryPincode=Entry(fr3,width=20,font=("Times New Roman",20),textvariable=varPincode)
    entryPincode.grid(row=4,column=4)

    lblCountry=Label(fr3,width=20,text="*Enter Cust Country:",font=("Times New Roman",20))
    lblCountry.grid(row=5,column=3,padx="10")
    varCountry=StringVar()
    entryCountry=Entry(fr3,width=20,font=("Times New Roman",20),textvariable=varCountry)
    entryCountry.grid(row=5,column=4)

    submitBut=Button(fr3,width=20,text = "SUBMIT",font=("Times New Roman",20), bg="lightgreen", command=addCustData)
    submitBut.grid(row=6,column=3,pady=10)

    canclebut= Button(fr3,width=20,text="Cancel",font=("Times New Roman",20),bg="red",command=showfr2)
    canclebut.grid(row=6,column=1,pady=10)

def frameGen():#Comman frame for delete and search choices
    global fra
    fra = Frame(root)
    fra.pack(side="top", pady=50)
    fra.config(bd=5, bg="pink")

def showfr4():#Showing search choices again after cancelling the previous choice
    fra.destroy()
    searchbut_click()

def butid_click():#search through id button is pressed
    fr4.destroy()
    frameGen()
    global cuInfo
    lbid = Label(fra, text="Enter Customer ID: ", font=("Times New Roman", 20))
    lbid.grid(row=0, column=0)
    cuInfo = StringVar()
    entrycustid = Entry(fra, font=("Times New Roman", 20), textvariable=cuInfo)
    entrycustid.grid(row=0, column=1)
    submitbutt = Button(fra, text="SEARCH", font=("Times New Roman", 20), bg="lightgreen",command=checkCustExistence)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=showfr4)
    cancelbut.grid(row=1, column=0, pady=20)

def butmobno_click():#search through mobile no button is pressed
    fr4.destroy()
    frameGen()
    global cuInfo
    lbmob = Label(fra, text="Enter Customer Mobile No: ", font=("Times New Roman", 20))
    lbmob.grid(row=0, column=0)
    cuInfo = StringVar()
    entrycustmob = Entry(fra, font=("Times New Roman", 20), textvariable=cuInfo)
    entrycustmob.grid(row=0, column=1)
    submitbutt = Button(fra, text="SEARCH", font=("Times New Roman", 20), bg="lightgreen",command=checkCustExistence)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=showfr4)
    cancelbut.grid(row=1, column=0, pady=20)

def butEid_click():#search through Eid button is pressed
    fr4.destroy()
    frameGen()
    global cuInfo
    lbeid = Label(fra, text="Enter Customer Email ID: ", font=("Times New Roman", 20))
    lbeid.grid(row=0, column=0)
    cuInfo = StringVar()
    entrycusteid = Entry(fra, font=("Times New Roman", 20), textvariable=cuInfo)
    entrycusteid.grid(row=0, column=1)
    submitbutt = Button(fra, text="SEARCH", font=("Times New Roman", 20), bg="lightgreen",command=checkCustExistence)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=showfr4)
    cancelbut.grid(row=1, column=0, pady=20)

def showallbut():#Search cancelled
    fr4.destroy()
    fr2gen()#frame 2 generated again

def searchbut_click():#search button clicked and showing different choices
    fr2.destroy()
    global fr4
    fr4 = Frame(root)
    fr4.pack(side="top", pady=20)
    fr4.config(bd=5, bg='pink')

    lblchoice = Label(fr4,width=35, text="How do you want to Search a Customer: ", font=("Times New Roman", 20))
    lblchoice.grid(row=0, column=0, pady=15)
    butid = Button(fr4, width=25, text="Search through customer ID", font=("Times New Roman", 20), bg="lightgreen", command=butid_click)
    butid.grid(row=1, column=0)
    butmobno = Button(fr4, width=25, text="Search through cust MobileNO", font=("Times New Roman", 20), bg="lightgreen",command=butmobno_click)
    butmobno.grid(row=3, column=0)
    butEid = Button(fr4, width=25, text="Search through cust Email ID", font=("Times New Roman", 20), bg="lightgreen",command=butEid_click)
    butEid.grid(row=2, column=0,pady=15)
    cancelbut = Button(fr4, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=showallbut)
    cancelbut.grid(row=4, column=0, pady=20)

def genframe():#Showing Modify choices again after cancelling the previous choice
    fra.destroy()
    Modify_click()

def idmod_click():#modifyThroughID button clicked
    frr.destroy()
    frameGen()
    global custData
    lbid = Label(fra, text="Enter Customer ID: ", font=("Times New Roman", 20))
    lbid.grid(row=0, column=0)
    custData = StringVar()
    entrycustd = Entry(fra, font=("Times New Roman", 20), textvariable=custData)
    entrycustd.grid(row=0, column=1)
    submitbutt = Button(fra, text="MODIFY", font=("Times New Roman", 20), bg="lightgreen", command=modifycustcheck)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=genframe)
    cancelbut.grid(row=1, column=0, pady=20)

def mobmod_click():#modifyThroughMOBNO button clicked
    frr.destroy()
    frameGen()
    global custData
    lbmob = Label(fra, text="Enter Customer Mobile No: ", font=("Times New Roman", 20))
    lbmob.grid(row=0, column=0)
    entrycustmob = Entry(fra, font=("Times New Roman", 20), textvariable=custData)
    entrycustmob.grid(row=0, column=1)
    submitbutt = Button(fra, text="MODIFY", font=("Times New Roman", 20), bg="lightgreen", command=modifycustcheck)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=genframe)
    cancelbut.grid(row=1, column=0, pady=20)

def eidmod_click():#modifyThroughEID button clicked
    frr.destroy()
    frameGen()
    global custData
    lbmob = Label(fra, text="Enter Customer Email ID: ", font=("Times New Roman", 20))
    lbmob.grid(row=0, column=0)
    entrycustmob = Entry(fra, font=("Times New Roman", 20), textvariable=custData)
    entrycustmob.grid(row=0, column=1)
    submitbutt = Button(fra, text="MODIFY", font=("Times New Roman", 20), bg="lightgreen", command=modifycustcheck)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=genframe)
    cancelbut.grid(row=1, column=0, pady=20)

def showOperation():#Modify operation cancelled
    frr.destroy()
    fr2gen()

def Modify_click():#Modify button clicked and showing different choices
    fr2.destroy()
    global frr
    frr = Frame(root)
    frr.pack(side="top", pady=70)
    frr.config(bd=5, bg='pink')

    lblchoice= Label(frr, text="How do you want to Modify a Customer: ", font=("Times New Roman",20))
    lblchoice.grid(row=0,column=0,pady=20)
    butid=Button(frr, width=22,text="Modify through cust ID", font=("Times New Roman", 20),bg="lightgreen",command=idmod_click)
    butid.grid(row=1,column=0)
    butmobno = Button(frr, width=22,text="Modify through cust MobNO", font=("Times New Roman", 20), bg="lightgreen",command=mobmod_click)
    butmobno.grid(row=2, column=0,pady=20)
    butEid = Button(frr, width=22,text="Modify through cust Email ID", font=("Times New Roman", 20), bg="lightgreen",command=eidmod_click)
    butEid.grid(row=3, column=0)
    cancelbut=Button(frr,width=15,text="Cancel",font=("Times New Roman",20), bg="red", command=showOperation)
    cancelbut.grid(row=4,column=0,pady=20)

def modifyFrame():#Show frames for updated data
    fra.destroy()
    global fr5
    fr5 = Frame(root)
    fr5.pack(side="top", pady=70)
    fr5.config(bd=5, bg='pink')
    global varfirstUName, varLastUName, varUAge, varUMobile, varUEmail, varUAdd, varUCity, varUState, varUPincode, varUCountry

    lblfirstName = Label(fr5,width= 20,text="Cust Updated First Name:", font=("Times New Roman", 20))
    lblfirstName.grid(row=0, column=0)
    varfirstUName = StringVar()
    entryfirstName = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varfirstUName)
    entryfirstName.grid(row=0, column=1)

    lblLastName = Label(fr5,width= 20, text="Cust Updated Last Name:", font=("Times New Roman", 20))
    lblLastName.grid(row=1, column=0, pady="10")
    varLastUName = StringVar()
    entryLastName = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varLastUName)
    entryLastName.grid(row=1, column=1, pady="10")

    lblAge = Label(fr5,width= 20, text="Cust Updated Age:", font=("Times New Roman", 20))
    lblAge.grid(row=2, column=0)
    varUAge = StringVar()
    entryAge = Entry(fr5, width= 20,font=("Times New Roman", 20), textvariable=varUAge)
    entryAge.grid(row=2, column=1)

    lblMobile = Label(fr5,width= 20, text="Cust Updated Mobile No:", font=("Times New Roman", 20))
    lblMobile.grid(row=3, column=0, pady="10")
    varUMobile = StringVar()
    entryMobile = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varUMobile)
    entryMobile.grid(row=3, column=1, pady="10")

    lblEmail = Label(fr5,width= 20, text="Cust Updated EmailId:", font=("Times New Roman", 20))
    lblEmail.grid(row=4, column=0)
    varUEmail = StringVar()
    entryEmail = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varUEmail)
    entryEmail.grid(row=4, column=1)

    lblAdd = Label(fr5,width= 20, text="Cust Updated Address:", font=("Times New Roman", 20))
    lblAdd.grid(row=0, column=3, padx="10")
    varUAdd = StringVar()
    entryADD = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varUAdd)
    entryADD.grid(row=0, column=4)

    lblCity = Label(fr5,width= 20, text="Cust Updated City:", font=("Times New Roman", 20))
    lblCity.grid(row=1, column=3, padx="10")
    varUCity = StringVar()
    entryCity = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varUCity)
    entryCity.grid(row=1, column=4)

    lblState = Label(fr5,width= 20, text="Cust Updated State:", font=("Times New Roman", 20))
    lblState.grid(row=2, column=3, padx="10")
    varUState = StringVar()
    entryState = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varUState)
    entryState.grid(row=2, column=4)

    lblPincode = Label(fr5,width= 20, text="Enter Cust pincode:", font=("Times New Roman", 20))
    lblPincode.grid(row=3, column=3, padx="10")
    varUPincode = StringVar()
    entryPincode = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varUPincode)
    entryPincode.grid(row=3, column=4)

    lblCountry = Label(fr5,width= 20, text="Cust Updated Country:", font=("Times New Roman", 20))
    lblCountry.grid(row=4, column=3, padx="10")
    varUCountry = StringVar()
    entryCountry = Entry(fr5,width= 20, font=("Times New Roman", 20), textvariable=varUCountry)
    entryCountry.grid(row=4, column=4)

    submitBut = Button(fr5,width= 20, text="SUBMIT", font=("Times New Roman", 20), bg="lightgreen", command=modifyData)
    submitBut.grid(row=5, column=3)

def genfr():#Showing delete choices again after cancelling the previous choice
    deletebut_click()
    fra.destroy()

def idbut_click():#deleteThroughID button clicked
    fr.destroy()
    frameGen()
    global custinfo
    lbid=Label(fra, text="Enter Customer ID: ",font=("Times New Roman",20))
    lbid.grid(row=0, column=0)
    custinfo=StringVar()
    entrycustd=Entry(fra,font=("Times New Roman",20), textvariable=custinfo)
    entrycustd.grid(row=0,column=1)
    submitbutt = Button(fra, text="DELETE", font=("Times New Roman", 20), bg="lightgreen", command=deletecustcheck)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=genfr)
    cancelbut.grid(row=1, column=0, pady=20)

def mobBut_click():#deleteThroughMobileNo button clicked
    fr.destroy()
    frameGen()
    global custinfo
    lbmob = Label(fra, text="Enter Customer Mobile No: ", font=("Times New Roman", 20))
    lbmob.grid(row=0, column=0)
    custinfo=StringVar()
    entrycustmob = Entry(fra, font=("Times New Roman", 20), textvariable=custinfo)
    entrycustmob.grid(row=0, column=1)
    submitbutt = Button(fra, text="DELETE", font=("Times New Roman", 20), bg="lightgreen", command=deletecustcheck)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=genfr)
    cancelbut.grid(row=1, column=0, pady=20)

def eidBut_click():#deleteThroughEID button clicked
    fr.destroy()
    frameGen()
    global custinfo
    lbeid = Label(fra, text="Enter Customer Email ID: ", font=("Times New Roman", 20))
    lbeid.grid(row=0, column=0)
    custinfo = StringVar()
    entrycusteid = Entry(fra, font=("Times New Roman", 20), textvariable=custinfo)
    entrycusteid.grid(row=0, column=1)
    submitbutt = Button(fra, text="DELETE", font=("Times New Roman", 20), bg="lightgreen", command=deletecustcheck)
    submitbutt.grid(row=1, column=1)
    cancelbut = Button(fra, width=15, text="Cancel", font=("Times New Roman", 20), bg="red", command=genfr)
    cancelbut.grid(row=1, column=0, pady=20)

def showmain():#Delete operation cancelled
    fr.destroy()
    fr2gen()#frame 2 geretaed again

def deletebut_click():#Delete button clicked
    fr2.destroy()
    global fr
    fr = Frame(root)
    fr.pack(side="top",pady=70)
    fr.config(bd=5, bg="pink")

    lblchoice= Label(fr, text="How do you want to delete a Customer: ", font=("Times New Roman",20))
    lblchoice.grid(row=0,column=0,pady=20)
    butid=Button(fr, width=22,text="Delete through cust ID", font=("Times New Roman", 20),bg="lightgreen",command=idbut_click)
    butid.grid(row=1,column=0)
    butmobno = Button(fr, width=22,text="Delete through cust MobNO", font=("Times New Roman", 20), bg="lightgreen",command=mobBut_click)
    butmobno.grid(row=2, column=0,pady=20)
    butEid = Button(fr, width=22,text="Delete through cust Email ID", font=("Times New Roman", 20), bg="lightgreen",command=eidBut_click)
    butEid.grid(row=3, column=0)
    cancelbut=Button(fr,width=15,text="Cancel",font=("Times New Roman",20), bg="red", command=showmain)
    cancelbut.grid(row=4,column=0,pady=20)

def exitClick():#Exit from cms
    messagebox.showinfo("My CMS", "Thanks for using AJT CMS")
    root.destroy()

def fr2gen():#Show ALL the Buttons with their operations
    global fr2
    fr2 = Frame(root)#FRame2
    fr2.pack(side="top",pady=70)
    fr2.config(bd=5,bg="VIOLET")
    addBut=Button(fr2,text="ADD CUSTOMER",width=20, font=("Times New Roman",25),bg="SKYBLUE",command=addbut_click)#addcustbutton
    addBut.grid(row =1, column=0 )
    searchBut = Button(fr2,text = "SEARCH CUSTOMER", width=20,font=("Times New Roman",25), bg="SKYBLUE", command=searchbut_click)#searchcustbutton
    searchBut.grid(row=1,column=1,padx=20)
    modifyBut = Button(fr2,text = "MODIFY CUSTOMER",width=20,font=("Times New Roman",25), bg="SKYBLUE", command=Modify_click)#modifycustbutton
    modifyBut.grid(row=1,column=2)
    deleteBut = Button(fr2,text = "DELETE CUSTOMER",width=20,font=("Times New Roman",25), bg="SKYBLUE", command=deletebut_click)#deletecustbutton
    deleteBut.grid(row=2,column=0,pady=20)
    displayBut = Button(fr2,text = "DISPLAY CUSTOMERS",width=20,font=("Times New Roman",25), bg="SKYBLUE", command=displaybut_click)#disallcustbutton
    displayBut.grid(row=2,column=1,padx=20,pady=20)
    exitBut = Button(fr2,text = "EXIT",width=15,font=("Times New Roman",25), bg="gold", command=exitClick)#exitbutton
    exitBut.grid(row=2,column=2,pady=20)

#Root generation
root = Tk()
root.state("zoomed")
root.title("AB CMS")
root.config(bg = "orange")
#Frame one generate with heading(AB CMS)
fr1 = Frame(root)
fr1.config(bd=5,bg="red")
fr1.pack()
lal = Label(fr1,text="WELCOME TO AJT CMS",bg='green',font=("Times New Roman",75,"bold"))
lal.pack()
fr2gen()#Calling for all opeartion frame
root.mainloop()
