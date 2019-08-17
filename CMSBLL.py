#BLL
import pymysql
class Customer:
    con = pymysql.connect(host="localhost", user="****", password="*****", database="CustomerManagementSystem", port=3306)
    mycur = con.cursor()

    def __init__(self):#Constructor
        self.id =0
        self.firstName=""
        self.lastName=""
        self.age=0
        self.mobileNo=0
        self.emailId=""
        self.address=""
        self.city=""
        self.state=""
        self.pincode=0
        self.country=""

    def addCustomer(self):#Add customer data in dbms
        qry="insert into Customer values(%s,'%s','%s',%s,%s,'%s','%s','%s','%s',%s,'%s')"\
            %(self.id,self.firstName,self.lastName,self.age,self.mobileNo,self.emailId,
              self.address,self.city,self.state,self.pincode,self.country)
        Customer.mycur.execute(qry)
        Customer.con.commit()

    @staticmethod
    def displayAllCustomer():#fetch data from dbms
        qry="select * from customer"
        Customer.mycur.execute(qry)
        values = Customer.mycur.fetchall()
        return values

    @staticmethod
    def searchcust(id):#search cust in dbms and return cust data
        if id.isnumeric():
            if len(id)==10:
                qry = "select * from customer where MobileNo=%s"%id
                Customer.mycur.execute(qry)
                data = Customer.mycur.fetchall()
                return data
            else:
                qry = "select * from customer where ID=%s" %id
                Customer.mycur.execute(qry)
                data = Customer.mycur.fetchall()
                return data
        else:
            qry = "select * from customer where EmailId='%s'" %id
            Customer.mycur.execute(qry)
            data = Customer.mycur.fetchall()
            return data

    @staticmethod
    def deleteCustomer(id):#delete customer data
        if id.isnumeric():
            if len(id)==10:
                qry = "delete from customer where MobileNo=%s" %id
                Customer.mycur.execute(qry)
                Customer.con.commit()
            else:
                qry = "delete from customer where ID=%s" % id
                Customer.mycur.execute(qry)
                Customer.con.commit()
        else:
            qry = "delete from customer where EmailId='%s'" % id
            Customer.mycur.execute(qry)
            Customer.con.commit()

    @staticmethod
    def checkexits(id):#check whether a customer exists or not
        if id.isnumeric():
            if len(id)==10:
                qry="select exists(select 1 from customer where MobileNo = %s) as mycheck"%id
                Customer.mycur.execute(qry)
                value=Customer.mycur.fetchone()
                val = value[0]
                return val
            else:
                qry="SELECT EXISTS(SELECT 1 FROM customer WHERE ID = %s) AS mycheck"%id
                Customer.mycur.execute(qry)
                value=Customer.mycur.fetchone()
                val = value[0]
                return val
        else:
            qry = "SELECT EXISTS(SELECT 1 FROM customer WHERE EmailId = '%s') AS mycheck"%id
            Customer.mycur.execute(qry)
            value = Customer.mycur.fetchone()
            val = value[0]
            return val

    def modifyCustomer(self):#modify the data of a customer
        qry="update customer set FirstName='%s', LastName='%s', Age=%s, MobileNo=%s, EmailId='%s', Address='%s'," \
            " City='%s',State='%s', Pincode=%s, Country='%s'"%\
            (self.firstName,self.lastName,self.age,self.mobileNo,self.emailId,self.address,
             self.city,self.state,self.pincode,self.country)
        Customer.mycur.execute(qry)
        Customer.con.commit()
