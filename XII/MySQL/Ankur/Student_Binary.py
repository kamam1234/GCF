'''
WAP that performs following menu driven operations 
on binary file containing students' record (Roll no, Name, Marks):
    1: Insert records in a file
    2: Read records from a file
    3: Display records having marks >= 60
    4: Update record by roll number
'''
import pickle
import os

def append():
    f = open("stu_rec.dat","ab")
    while True:
        rno = int(input("Enter your rollno:="))
        name = input("Enter your Name:=")
        marks = float(input("Enter your marks:="))
        
        data = [rno, name, marks]
        pickle.dump(data,f)
        
        ch = input("Do you want to enter more records (y/n) ?:=")
        if ch == 'n':
            break
    f.close()

def read():
    try:
        f = open("stu_rec.dat","rb")
    except IOError:
        print("File not found.")
        return
    
    print("=" * 41)
    obj_string = "{:<6} {:^15} {:>8}"
    print(obj_string.format("Roll", "Name", "%"))
    print("=" * 41)
    
    rec = 0
    while True:
        try:
            data = pickle.load(f)
            rec += 1

            obj_string = "{:<6} {:^15} {:>8.2f}"
            print(obj_string.format(data[0], data[1], data[2])) 
        except EOFError:
            print("=" * 41)
            print(rec, "record(s) found.")
            break
    f.close()
    
def src_marks():
    try:
        f = open("stu_rec.dat","rb")
    except IOError:
        print("File not found.")
        return
    
    print("=" * 41)
    obj_string = "{:<6} {:^15} {:>8}"
    print(obj_string.format("Roll", "Name", "%"))
    print("=" * 41)
    
    rec = 0
    while True:
        try:
            data = pickle.load(f)
            if data[2] >= 60:
                rec += 1
    
                obj_string = "{:<6} {:^15} {:>8.2f}"
                print(obj_string.format(data[0], data[1], data[2])) 
            
        except EOFError:
            print("=" * 41)
            print(rec, "record(s) found.")
            break
    f.close()
    
def update():
    sf = open("stu_rec.dat","rb")
    tp = open("temp.dat","wb")
    
    roll = int(input("Enter roll number to update:"))
    rec = 0
    while True:
        try:
            data = pickle.load(sf)
            if data[0] == roll:
                rec += 1
                print("\nRoll no:", data[0])
                print("Name:", data[1])
                print("Marks:", data[2])
                
                data[0] = int(input("Enter your rollno:="))
                data[1] = input("Enter your Name:=")
                data[2] = float(input("Enter your marks:="))
            
            pickle.dump(data,tp)
            
        except EOFError:
            print(rec, "record(s) updated.")
            break
            
    sf.close() 
    tp.close()
    
    os.remove("stu_rec.dat")
    os.rename("temp.dat", "stu_rec.dat")

# ___main___
while True:
    print("\n" * 5)
    print("Choose an option from following")
    print("1: Insert records in a file")
    print("2: Read records from a file")
    print("3: Display records having marks >= 60")
    print("4: Update record by roll number")   
    print("0: Exit")
    ch = int(input("Enter your choice:"))
    
    if ch == 1:
        append()
        
    elif ch == 2:
        read()
        
    elif ch == 3:
        src_marks()    
    
    elif ch == 4:
        update()
        
    elif ch == 0:
        break
        
    else:
        print("Invalid Input.")
    
    input("\n\nPress 'ENTER' to continue...")
    
    
    
    
    
    
    
    
    
