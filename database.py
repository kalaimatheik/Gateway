import sqlite3


def login_name(ip_usr):
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

def login_pas(ip_usr):
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

def verify_lock(ip_usr):
    try:
        conn = sqlite3.connect('data.sql')
        cur = conn.cursor()
        cmd='Select status from account_details where name=?'
        cur.execute(cmd,(ip_usr,))
        return cur.fetchone()[0]
    finally:
        conn.close()

def login_lock(ip_usr):
    try:
        conn=sqlite3.connect('data.sql')
        cur=conn.cursor()
        cmd='Update ACCOUNT_DETAILS SET STATUS =? WHERE name=?'
        cur.execute(cmd,("D",ip_usr,))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.commit()
        conn.close()

def login_unlock(ip_usr):
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

def verify_lock(ip_usr):
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


#print(login_lock('root'))
#print(verify_lock('root'))