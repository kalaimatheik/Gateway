import sqlite3


def login_name(ip_usr):                                        #Checks whether the user name is present in db
    try:
        conn = sqlite3.connect('data.sql')
        cur = conn.cursor()
        cmd='Select name from account_details where name=?'
        cur.execute(cmd,(ip_usr,))
        return cur.fetchone()[0]
    except:
        return False
    finally:
        conn.close()

def login_pas(ip_usr):                                          #checks for the password in db with resp to the username in db
    try:
        conn = sqlite3.connect('data.sql')
        cur = conn.cursor()
        cmd='Select password from account_details where name=?'
        cur.execute(cmd,(ip_usr,))
        return cur.fetchone()[0]    
    except:
        return False
    finally:
        conn.close()

def verify_lock(ip_usr):                                        #checks if the account is in locked state
    try:
        conn = sqlite3.connect('data.sql')
        cur = conn.cursor()
        cmd='Select status from account_details where name=?'
        cur.execute(cmd,(ip_usr,))
        return cur.fetchone()[0]
    finally:
        conn.close()

def login_lock(ip_usr):                                                 #Locks the account in db state as 'L'
    try:
        conn=sqlite3.connect('data.sql')
        cur=conn.cursor()
        cmd='Update ACCOUNT_DETAILS SET STATUS =? WHERE name=?'
        cur.execute(cmd,("L",ip_usr,))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.commit()
        conn.close()

def login_unlock(ip_usr):                                               #Unlocks the db to 'A'
    try:
        conn=sqlite3.connect('data.sql')
        cur=conn.cursor()
        cmd='Update ACCOUNT_DETAILS SET STATUS =? WHERE name=?'
        cur.execute(cmd,("A",ip_usr,))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.commit()
        conn.close()

def verify_lock(ip_usr):                                                #verifies the state of the user_account
    try:
        conn=sqlite3.connect('data.sql')
        cur=conn.cursor()
        cmd='SELECT status from ACCOUNT_DETAILS WHERE name=?'
        cur.execute(cmd,(ip_usr,))
        x=cur.fetchone()[0]
        if x=='L':
            return True
        else:
            return 0
    except:
        return False
    finally:
        conn.commit()
        conn.close()


def admin_check(ip_usr):                                        #checks if the account is a standard user or Admin
    try:
        conn = sqlite3.connect('data.sql')
        cur = conn.cursor()
        cmd='Select category from account_details where name=?'
        cur.execute(cmd,(ip_usr,))
        if cur.fetchone()[0]=='Admin':
            return True
        else:
            return False
    finally:
        conn.close()


def new_user(ip_usr,ip_pass,ip_pin,ip_token):
    try:
        conn = sqlite3.connect('data.sql')
        cur = conn.cursor()
        cmd='insert into account_details(Username,Password,PIN,Token ) values (?,?,?,?)'
        cur.execute(cmd,(ip_usr,ip_pass,ip_pin,ip_token))
        conn.commit()
        return True
    finally:
        conn.commit()
        conn.close()


#print(new_user('kaasdlai','12as1','1235','afafaf'))