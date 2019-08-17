import pymysql
con = pymysql.connect(host="localhost", user="******", password="*******", port=3306)
mycur = con.cursor()


mycur.execute("create database CustomerManagementSystem")
con.commit()

mycur.execute("use CustomerManagementSystem")
mycur.execute("create table customer(ID INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255) NOT NULL, LastName VARCHAR(255), Age INT NOT NULL,\
              MobileNo BIGINT NOT NULL, EmailId VARCHAR(255) NOT NULL, Address VARCHAR(255), City VARCHAR(255) NOT NULL,\
              State VARCHAR(255) NOT NULL, Pincode INT NOT NULL, Country VARCHAR(255) NOT NULL)")
con.commit()
