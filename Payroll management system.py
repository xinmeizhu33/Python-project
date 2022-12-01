from tkinter import *
import random
import time
import datetime

payroll = Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management System")

def Exit():
    payroll.destroy()

def Reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    City.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    Deductions.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtherPaymentDue.set("")
    
def PayRef():
    PayDate.set(time.strftime("%d/%m/%Y"))
    #PayDate.set(time.strftime("%x"))
    Refpay=random.randint(20000,709467)
    Refpaid=("PR"+str(Refpay))
    Reference.set(Refpaid)

    NIpay=random.randint(20000,709467)
    NIpaid=("NI"+str(NIpay))
    NINumber.set(NIpaid)

def PayPeriod():
    i=datetime.datetime.now()
    TaxPeriod.set(i.month)

    NCode=random.randint(2000,4467)
    CodeNI=("NI"+str(NCode))
    NICode.set(CodeNI)

def MonthlySalary():
    BS = float(BasicSalary.get())
    CW = float(City.get())
    OT = float(OverTime.get())

    MTax = ((BS+CW+OT)*0.17)
    TTax = "$",str('%.2f'%(MTax))
    Tax.set(TTax)

    M_Pension = ((BS+CW+OT)*0.02)
    MM_Pension = "$",str('%.2f'%(M_Pension))
    Pension.set(MM_Pension)

    M_StudentLoan = ((BS+CW+OT)*0.012)
    MM_StudentLoan = "$",str('%.2f'%(M_StudentLoan))
    StudentLoan.set(MM_StudentLoan)

    M_NIPayment = ((BS+CW+OT)*0.011)
    MM_NIPayment = "$",str('%.2f'%(M_NIPayment))
    NIPayment.set(MM_NIPayment)

    Deduct = (MTax + M_Pension + M_StudentLoan + M_NIPayment)
    Deduct_Payment = "$",str('%.2f'%(Deduct))     
    Deductions.set(Deduct_Payment)
    
    Gross_Pay = "$", str('%.2f'%(BS+CW+OT))
    GrossPay.set(Gross_Pay)

    NetPayAfter = (BS + CW + OT)-Deduct
    NetAfter = "$", str('%.2f'%(NetPayAfter))
    NetPay.set(NetAfter)  
    
    TaxablePay.set(TTax)
    PensionablePay.set(MM_Pension)
    OtherPaymentDue.set("0.00")
    
    
EmployeeName = StringVar()
Address = StringVar()
Reference = StringVar()
EmployerName = StringVar()
City = StringVar()
BasicSalary = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
NetPay = StringVar()
Tax = StringVar()
Pension = StringVar()
StudentLoan = StringVar()
NIPayment = StringVar()
Deductions = StringVar()
PostCode = StringVar()
Gender = StringVar()
PayDate = StringVar()
TaxPeriod = StringVar()
NINumber = StringVar()
NICode = StringVar()
TaxablePay = StringVar()
PensionablePay = StringVar()
OtherPaymentDue = StringVar()


text_Input = StringVar()

Tops = Frame(payroll, width = 1350, height = 50, bd=16, relief="raise")
Tops.pack(side = TOP)
LF = Frame(payroll, width = 700, height = 650, bd=16, relief="raise")
LF.pack(side = LEFT)
RF = Frame(payroll, width = 600, height = 650, bd=16, relief="raise")
RF.pack(side = RIGHT)

lblInfo = Label(Tops, font = ('arial',50, 'bold'), text = "Payroll Management System",fg = "Steel Blue", bd = 1)
lblInfo.grid(row = 0, column = 0)


LeftInsideLF = Frame(LF, width = 700, height=200, bd=16, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF = Frame(LF, width = 325, height=400,bd=16, relief="raise")
LeftInsideLFLF.pack(side=LEFT)
LeftInsideRFRF = Frame(LF, width = 325, height=400,bd=16, relief="raise")
LeftInsideRFRF.pack(side=RIGHT)


RightInsideLF = Frame(RF, width=650, height=200, bd=16, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF = Frame(RF, width=300, height=400,bd=16, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF = Frame(RF, width=300, height=400, bd=16, relief="raise")
RightInsideRFRF.pack(side=RIGHT)

#==================================Left Side================================
lblEmployeeName = Label(LeftInsideLF,font=('arial',12,'bold'),text="Employee Name",
                        fg="Steel Blue",bd=10, anchor='w')
lblEmployeeName.grid(row=0,column=0)
txtEmployeeName=Entry(LeftInsideLF,font=('arial',12,'bold'),bd=10,width=56,
                      bg="powder blue", justify='right',textvariable=EmployeeName)
txtEmployeeName.grid(row=0,column=1)
lblAddress=Label(LeftInsideLF,font=('arial',12,'bold'),text="Address",
                 fg="Steel Blue", bd=10, anchor='w')
lblAddress.grid(row=1,column=0)
txtAddress=Entry(LeftInsideLF,font=('arial',12,'bold'),bd=10,width=56,
                 bg="powder blue", justify='right',textvariable=Address)
txtAddress.grid(row=1,column=1)


lblReference = Label(LeftInsideLF,font=('arial',12,'bold'),text="Reference",
                        fg="Steel Blue", bd=10,anchor='w')
lblReference.grid(row=2,column=0)
txtReference=Entry(LeftInsideLF,font=('arial',12,'bold'),bd=10,width=56,
                      bg="powder blue",justify='right',textvariable=Reference)
txtReference.grid(row=2,column=1)
lblEmployerName=Label(LeftInsideLF,font=('arial',12,'bold'),text="EmployerName",
                      fg="Steel Blue", bd=10,anchor='w')
lblEmployerName.grid(row=3,column=0)
txtEmployerName=Entry(LeftInsideLF,font=('arial',12,'bold'),bd=10,width=56,
                      bg="powder blue",justify='right', textvariable=EmployerName)
txtEmployerName.grid(row=3,column=1)

#==========================Left inner side==================================
#-------------Left inner left side

lblCity = Label(LeftInsideLFLF,font=('arial',12,'bold'),text="City Weighting",
                        fg="Steel Blue", bd=10,anchor='w')
lblCity.grid(row=0,column=0)
txtCity=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=City)
txtCity.grid(row=0,column=1)
#-----------------
lblBasicSalary=Label(LeftInsideLFLF,font=('arial',12,'bold'),text="Basic Salary",
                      fg="Steel Blue", bd=10,anchor='w')
lblBasicSalary.grid(row=1,column=0)
txtBasicSalary=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=BasicSalary)
txtBasicSalary.grid(row=1,column=1)

#------------------

lblOverTime = Label(LeftInsideLFLF,font=('arial',12,'bold'),text="Over Time",
                        fg="Steel Blue", bd=10,anchor='w')
lblOverTime.grid(row=2,column=0)
txtOverTime=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=OverTime)
txtOverTime.grid(row=2,column=1)
#-------------------
lblGrossPay=Label(LeftInsideLFLF,font=('arial',12,'bold'),text="Gross Pay",
                      fg="Steel Blue", bd=10,anchor='w')
lblGrossPay.grid(row=3,column=0)
txtGrossPay=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=GrossPay)
txtGrossPay.grid(row=3,column=1)
#--------------------
lblNetPay=Label(LeftInsideLFLF,font=('arial',12,'bold'),text="Net Pay",
                      fg="Steel Blue", bd=10,anchor='w')
lblNetPay.grid(row=4,column=0)
txtNetPay=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=NetPay)
txtNetPay.grid(row=4,column=1)

#==============LeftInsideRFRF
#-------------
lblTax = Label(LeftInsideRFRF,font=('arial',12,'bold'),text="Tax",
                        fg="Steel Blue", bd=10,anchor='w')
lblTax.grid(row=0,column=2)
txtTax=Entry(LeftInsideRFRF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=Tax)
txtTax.grid(row=0,column=3)
#-----------------
lblPension=Label(LeftInsideRFRF,font=('arial',12,'bold'),text="Pension",
                      fg="Steel Blue", bd=10,anchor='w')
lblPension.grid(row=1,column=2)
txtPension=Entry(LeftInsideRFRF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=Pension)
txtPension.grid(row=1,column=3)

#------------------

lblStudentLoan = Label(LeftInsideRFRF,font=('arial',12,'bold'),text="Student Loan",
                        fg="Steel Blue", bd=10,anchor='w')
lblStudentLoan.grid(row=2,column=2)
txtStudentLoan=Entry(LeftInsideRFRF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=StudentLoan)
txtStudentLoan.grid(row=2,column=3)
#-------------------
lblNIPayment=Label(LeftInsideRFRF,font=('arial',12,'bold'),text="NI Payment",
                      fg="Steel Blue", bd=10,anchor='w')
lblNIPayment.grid(row=3,column=2)
txtNIPayment=Entry(LeftInsideRFRF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=NIPayment)
txtNIPayment.grid(row=3,column=3)
#-----------------------
lblDeductions=Label(LeftInsideRFRF,font=('arial',12,'bold'),text="Deductions",
                      fg="Steel Blue", bd=10,anchor='w')
lblDeductions.grid(row=4,column=2)
txtDeductions=Entry(LeftInsideRFRF,font=('arial',12,'bold'),bd=10,width=18,
                      bg="powder blue",justify='right', textvariable=Deductions)
txtDeductions.grid(row=4,column=3)

#==================================Right Side===============================

lblPostCode = Label(RightInsideLF,font=('arial',12,'bold'),text="Post Code",
                        fg="Steel Blue", bd=10,anchor='w')
lblPostCode.grid(row=0,column=0)
txtPostCode=Entry(RightInsideLF,font=('arial',12,'bold'),bd=10,width=48,
                      bg="powder blue",justify='right', textvariable=PostCode)
txtPostCode.grid(row=0,column=1)
lblGender=Label(RightInsideLF,font=('arial',12,'bold'),text="Gender",
                      fg="Steel Blue", bd=10,anchor='w')
lblGender.grid(row=1,column=0)
txtGender=Entry(RightInsideLF,font=('arial',12,'bold'),bd=10,width=48,
                      bg="powder blue",justify='right', textvariable=Gender)
txtGender.grid(row=1,column=1)

#=============================Right inner side===============================

#-------------Left inner left side

lblPayDate = Label(RightInsideLFLF,font=('arial',12,'bold'),text="Pay Date",
                        fg="Steel Blue", bd=10,anchor='w')
lblPayDate.grid(row=0,column=0)
txtPayDate=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=10,width=16,
                      bg="powder blue",justify='right', textvariable=PayDate)
txtPayDate.grid(row=0,column=1)

lblTaxPeriod = Label(RightInsideLFLF,font=('arial',12,'bold'),text="Tax Period",
                        fg="Steel Blue", bd=10,anchor='w')
lblTaxPeriod.grid(row=1,column=0)
txtTaxPeriod=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=10,width=16,
                      bg="powder blue",justify='right', textvariable=TaxPeriod)
txtTaxPeriod.grid(row=1,column=1)
#-----------------
lblNINumber=Label(RightInsideLFLF,font=('arial',12,'bold'),text="NI Number",
                      fg="Steel Blue", bd=10,anchor='w')
lblNINumber.grid(row=2,column=0)
txtNINumber=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=10,width=16,
                      bg="powder blue",justify='right', textvariable=NINumber)
txtNINumber.grid(row=2,column=1)

#------------------

lblNICode = Label(RightInsideLFLF,font=('arial',12,'bold'),text="NI Code",
                        fg="Steel Blue", bd=10,anchor='w')
lblNICode.grid(row=3,column=0)
txtNICode=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=10,width=16,
                      bg="powder blue",justify='right', textvariable=NICode)
txtNICode.grid(row=3,column=1)
#-------------------
lblTaxablePay=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Taxable Pay",
                      fg="Steel Blue", bd=10,anchor='w')
lblTaxablePay.grid(row=4,column=0)
txtTaxablePay=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=10,width=16,
                      bg="powder blue",justify='right', textvariable=TaxablePay)
txtTaxablePay.grid(row=4,column=1)
#--------------------
lblPensionablePay=Label(RightInsideLFLF,font=('arial',12,'bold'),text="PensionablePay",
                      fg="Steel Blue", bd=10,anchor='w')
lblPensionablePay.grid(row=5,column=0)
txtPensionablePay=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=10,width=16,
                      bg="powder blue",justify='right', textvariable=PensionablePay)
txtPensionablePay.grid(row=5,column=1)
#-------------------------
lblOtherPaymentDue=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Other Payment Due",
                      fg="Steel Blue", bd=10,anchor='w')
lblOtherPaymentDue.grid(row=6,column=0)
txtOtherPaymentDue=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=10,width=16,
                      bg="powder blue",justify='right', textvariable=OtherPaymentDue)
txtOtherPaymentDue.grid(row=6,column=1)

#==============LeftInsideRFRF


btnWagePayment=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',12,'bold'),width=12,
                      text="Wage Payment", bg="sky blue", command=MonthlySalary).grid(row=0,column=0)
btnResetSystem=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',12,'bold'),width=12,
                      text="Reset System", bg="sky blue",command=Reset).grid(row=1,column=0)
btnPayRef=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',12,'bold'),width=12,
                      text="Pay Reference", bg="sky blue",command=PayRef).grid(row=2,column=0)
btnPayCode=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',12,'bold'),width=12,
                      text="Pay Code", bg="sky blue", command=PayPeriod).grid(row=3,column=0)

'''
btnPayCode=Button(RightInsideRFRF,padx=8,bd=8,fg="black",font=('arial',12,'bold'),width=14,
                      text="Pay Code", bg="sky blue").grid(row=3,column=0)
'''
btnExit=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',12,'bold'),width=12,
                      text="Exit", bg="sky blue",command=Exit).grid(row=4,column=0)



payroll.mainloop()


            
