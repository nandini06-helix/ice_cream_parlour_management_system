import mysql.connector as s

mycon = s.connect(host="localhost", user="rootop", passwd="2004", database="ncert")
cu = mycon.cursor()


def display_details():
    print("\t\t DETAILS of icecream ")
    cu.execute("select * from icecream\n")
    rs = cu.fetchall()
    # print(" item_code \t flavours\t type\t small\t price")
    for r in rs:
        print(r)


def modify():
    X = input('do you want to drop/add items?y/n')
    if X == 'y':
        Ms = input('do you want to drop toppings or icecream flavours?f/t')
        if Ms == 'f':
            Ps = input('which flavour do u want?')
            cu.execute('delete from icecream where flavours="{}"'.format(Ps))
        else:
            Ts = input('which topping do u want?')
            cu.execute('delete from toppings_ice_cream where toppings="{}"'.format(Ts))
    else:
        Gs = input('do you want to change toppings or flavours?F/t')
        if Gs == 'F':
            Us = input('which flavour do u want?')
            cu.execute('update icecream set where flavours="{}"'.format(Us))
        else:
            Os = input('which topping do u want?')
            cu.execute('update toppings_ice_cream set where toppings="{}"'.format(Os))
    mycon.commit()


def search_menu():
    print("\t\t SEARCH ")
    print("\tC. Search by flavours ")
    print("\tM. Search by Type ")
    print("\tCo. Search topping types")
    s = input(" Enter option for Search")
    if s == 'C':

        n = input("enter  ice cream flavours")
        print(" ice cream flavour")
        cu.execute("select * from icecream where flavours ='{}'".format(n))
        d = cu.fetchall()
        for row in d:
            print(row)
    elif s == 'M':
        m = input("Enter type")
        print("type")
        cu.execute("select item_code,flavours, , small, med, large from icecream where type ='{}'".format(m))
        d = cu.fetchall()
        for row_m in d:
            print(row_m[1], row_m[2], row_m[3])
    elif s == 'Co':

        c = input("Enter toppings ")
        # print("toppings for ice cream")
        cu.execute("select * from where color ='{}'".format(c))
        d = cu.fetchall()
        for row_c in d:
            print(row_c)


def bill(tp):
    cn = input("Name ")

    print('*' * 40)

    print(" .........V ICE CREAM PARLOUR............")
    print(" Customer Name:", cn, "Total Price :      ", tp)
    cu.execute("insert into cust_icecream values('{}','{}',curdate())".format(cn, tp))
    mycon.commit()


def sales_details():
    cu.execute("select date_of_purchase,sum(price) from cust_icecream group by date_of_purchase")
    rs = cu.fetchall()
    print("Date of Purchase\t\t Total Price")
    for gd in rs:
        print(gd[0], '\t\t\t   ', gd[1])


def main_menu():
    ans = 'y'
    while ans == 'y':
        print("\n\t MENU\t\t")
        print("1. Display  records")
        print("2. Search Record")
        print("3. Purchase")
        print("4. Modify Record")
        print("5. Sales Details")
        print("6. Exit")
        ch = int(input("Enter your choice"))
        if ch == 1:
            display_details()

        elif ch == 2:
            search_menu()

        elif ch == 3:
            pr = tp = 0
            print(" Purchase")
            ch = 'y'
            while ch == 'y':
                Fl = input("which flavour do you want?")

                cu.execute("select flavours,type,small,med,large from icecream where flavours='{}'".format(Fl))
                rs = cu.fetchall()
                for r in rs:
                    print(r[0], ' ', r[1], ' ', r[2], ' ', r[3], ' ', r[4])

                Sz = input("what size of ice cream do you want?")
                if Sz == 's':
                    pr = r[2]
                elif Sz == 'm':
                    pr = r[3]
                elif Sz == 'l':
                    pr = r[4]
                Tp = input("do you want toppings?”, ‘y/n’")

                if Tp == 'y':
                    Top = input("which toppings do you want?")

                    cu.execute("select toppings, price from toppings_ice_cream where toppings='{}'".format(Top))
                    As = cu.fetchall()
                    for a in As:
                        print(a[0], a[1])

                        pr += a[1]
                ch = input("do you want more ice cream?")
                tp += pr
            print('Total price:', tp)

            ans = input(" Prepare Bill")
            if ans == 'Y' or ans == 'y':
                bill(tp)
            else:
                print("       ")
        elif ch == 4:
            print("Update records")
            modify()
        elif ch == 5:
            sales_details()
        elif ch == 6:
            print('exit')


main_menu()
mycon.close()






