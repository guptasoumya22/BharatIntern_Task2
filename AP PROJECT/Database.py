import sqlite3
connect = sqlite3.Connection("Bus_Booking_System.db")
c = connect.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS BUS(Bus_ID int AUTO INCREMENT, Type text, Capacity int, Fare int, Route_ID int, Operator_ID int, PRIMARY KEY(BUS_ID),
FOREIGN KEY(Operator_ID) references OPERATOR(Operator_ID), FOREIGN KEY(Route_ID) references Route(Route_ID))""")
c.execute("""CREATE TABLE IF NOT EXISTS OPERATOR(Operator_ID int AUTO INCREMENT,Bus_ID int, Opt_Name text, Address text, Email_ID text,Phone_no int, PRIMARY KEY(OPERATOR_ID),
FOREIGN KEY(Bus_ID) references BUS(Bus_Id))""")
c.execute("""CREATE TABLE IF NOT EXISTS ROUTE(Route_ID int , Station_ID int , Station_Name text,Bus_ID int, PRIMARY KEY(Route_ID, Station_ID),
FOREIGN KEY(Bus_ID) references BUS(Bus_ID))""")
c.execute("""CREATE TABLE IF NOT EXISTS RUN(Bus_ID int, Date date, Seat_Availavle int, PRIMARY KEY(BUS_ID, Date),
FOREIGN KEY(BUS_ID) references BUS(Bus_ID))""")
c.execute("""CREATE TABLE IF NOT EXISTS BOOKING_HISTORY(Booking_ID int AUTO INCREMENT, Passengers_Name text, Gender text, No_of_seats int, Mobile_no int,
Fare int, Bus_ID int, PRIMARY KEY(Booking_ID), FOREIGN KEY(BUS_ID) references BUS(BUS_ID))""")

#c.execute('''Select o.Opt_name, b.type, r.Seat_Availavle, b.fare from bus as b, operator as o, run as r, route as re where b.operator_id = o.operator_id and b.bus_id = r.bus_id
#and re.route_id = b.route_id and re.Station_Name = Guna''')#,(Guna,))
c.execute("select * from booking_history")
records = c. fetchall()
print(records)


connect.commit()
connect.close()
