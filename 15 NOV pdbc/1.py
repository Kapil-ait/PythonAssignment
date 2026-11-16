import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="Kapil@123"
)
cursor=conn.cursor()
query="create database if not exists pdbc"
cursor.execute(query)
query="use pdbc"
cursor.execute(query)
query="create table if not exists customer_order_pdbc(customer_id int primary key,customer_name varchar(20),city varchar(40) ,email varchar(80))"
cursor.execute(query)
query="insert ignore into customer_order_pdbc values(1,'Amit','Indore','amit@gmail.com'),(2,'priya','Bhopal','priya@gmail.com'),(3,'Rahul','Inodre','rahul@gmail.com'),(4,'Neha','Ujjain','neha@gmail.com'),(5,'Karan','Dewas','Karan@gmail.com')"
cursor.execute(query)
query="create table if not exists product_order_pdbc(product_id int primary key,product_name varchar(20),category varchar(40),price decimal(10,2),stock int)"
cursor.execute(query)
query="insert ignore into product_order_pdbc values(101,'Laptop','Electronics',55000.00,10),(102,'Mouse','Electronics',800.00,50),(103,'Keyboard','Electronics',1500.00,30),(104,'Notebook','Stationary',100.00,100),(105,'Monitor', 'Electronics',12000.00,15),(106,'Pen','Stationary',20.00,200)"
cursor.execute(query)
query="create table if not exists customer_order_details(order_id int primary key,customer_id int,product_id int,quantity int,order_status varchar(30),foreign key(customer_id) references customer_order_pdbc(customer_id),foreign key(product_id) references product_order_pdbc(product_id))"
cursor.execute(query)
query="insert ignore into customer_order_details values(1001,1,101,1,'Delivered'),(1002,1,102,2,'Delivered'),(1003,2,103,1,'Shipped'),(1004,3,105,2,'Delivered'),(1005,3,104,5,'Pending'),(1006,4,101,1,'Pending'),(1007,5,106,10,'Delivered')"
cursor.execute(query)
conn.commit()
while True:
    print("Add Customer")
    print("Add Product")
    print("Place Order")
    print("Display All Orders with Customer and Product Details")
    print("Search Customer by Name")
    print("Update Product Price")
    print("Update order Status")
    print("Update Product Size")
    print("Delete order")
    print("Display Order")
    print("Display Customer-wise Total Purchase Amount")
    print("Display Products Costing More Than Average Product Price")
    print("Display Customers Who Have Placed at Least One Order")
    print("12. Display Customers Who Have Not Placed Any Order")
    print("Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        customer_id=int(input("enter customer id:"))
        customer_name=input("enter name:")
        city=input("enter city:")
        email=input("enter email:")
        query="insert into customer_order_pdbc values(%s,%s,%s,%s)"
        values=(customer_id,customer_name,city,email)
        print("insertion success")
        cursor.execute(query,values)
        conn.commit()
    elif choice==2:
        product_id=int(input("enter product id:"))
        product_name=input("enter product name:")
        category=input("enter category:")
        price=float(input("enter price:"))
        stock=int(input("enter stock:"))
        query="insert into product_order_pdbc values(%s,%s,%s,%s,%s)"
        values=(product_id,product_name,category,price,stock)
        cursor.execute(query,values)
        conn.commit()
        print("product insert successfully")
    elif choice==3:
        order_id=int(input("enter order id:"))
        customer_id=int(input("enter customer_id:"))
        product_id=int(input("enter product id:"))
        quantity=int(input("enter quantity:"))
        status=input("enter status:")
        query="insert into customer_order_details values(%s,%s,%s,%s,%s)"
        values=(order_id,customer_id,product_id,quantity,status)
        cursor.execute(query,values)
        conn.commit()
        print("order placed successfully")
    elif choice==4:
        query=" select cod.order_id,cop.customer_name,pop.product_name,cod.quantity,pop.price,(cod.quantity*pop.price),cod.order_status from customer_order_details as cod inner join customer_order_pdbc as cop on cod.customer_id=cop.customer_id inner join product_order_pdbc as pop on pop.product_id=cod.product_id"
        cursor.execute(query)
        r=cursor.fetchall()
        for i in r:
            print(i)
    elif choice==5:
        customer_name=input("enter customer name to search:")
        query="select cop.customer_name from customer_order_pdbc as cop where cop.customer_name like '%an%'"
        cursor.execute(query)
        r=cursor.fetchall()
        for i in r:
            print(i)
    elif choice==6:
        product_id=int(input("enter product id:"))
        price=int(input("enter new price:"))
        query="update product_order_pdbc set price=%s where product_id=%s"
        values=(price,product_id)
        cursor.execute(query,values)
        conn.commit()
        print("Product price updated successfully")
        
    elif choice==7:
        order_id=int(input("enter order id:"))
        status=input("enter status:")
        query="update customer_order_details set status=%s where order_id=%s"
        values=(status,order_id)
        cursor.execute(query,values)
        conn.commit()
        print("Order status updated successfully")
    elif choice==8:
        order_id=int(input("enter ID:"))
        query="delete from customer_order_details where order_id=%s"
        cursor.execute(query,(order_id,))
        conn.commit()
        print("Order deleted successfully")
    elif choice==9:
        query="select cop.customer_id,cop.customer_name,sum(cod.quantity*pop.price) from customer_order_pdbc as cop inner join customer_order_details as cod on cod.customer_id=cop.customer_id inner join product_order_pdbc as pop on pop.product_id=cod.product_id group by customer_id"
        cursor.execute(query)
        r=cursor.fetchall()
        for i in r:
            print(i)
    elif choice==10:
        query="select pop.product_id,pop.product_name,pop.price from product_order_pdbc as pop where price>(select avg(price) from product_order_pdbc)"
        cursor.execute(query)
        r=cursor.fetchall()
        for i in r:
            print(i)
    elif choice==11:
        query="select cop.customer_id,cop.customer_name from customer_order_pdbc as cop where cop.customer_id in (select cod.customer_id from customer_order_details as cod where quantity>=1)"
        cursor.execute(query)
        r=cursor.fetchall()
        for i in r:
            print(i)
    elif choice==12:
        query="select * from customer_order_pdbc where customer_id not in (select customer_id from customer_order_details)"
        cursor.execute(query)
        r=cursor.fetchall()
        for i in r:
            print(i)
    elif choice==13:
        order_id=int(input("enter ID:"))
        customer_id=int(input("enter customer_id:"))
        product_id=int(input("enter product id:"))
        quantity=int(input("enter quantity:"))
        status=input("enter status:")
        query="insert into customer_order_details values(%s,%s,%s,%s,%s)"
        values=(order_id,customer_id,product_id,quantity,status)
        cursor.execute(query,values)
        conn.commit()
    elif choice==14:
        print("Thankyou")
        break




