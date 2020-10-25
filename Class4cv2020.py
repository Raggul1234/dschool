from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyodbc


#ConnectingDatabase#

from tkinter import messagebox
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MUTHUCOMPUTER;'
                      'Database=Class4c v4;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

#Adding new record#





def Save():
    Names=   (Name.get())
    Ages=    (Age.get())
    Heights= (Height.get())
    Weights= (Weight.get())
    StudentIds= (StudentId.get())
    Activitytypes=(Activitytype.get())
    Activitys=(Activity.get())
    Extras=(Extra.get())

    Validate(Names,Ages,Heights,Weights,StudentIds,Activitytypes,Activitys,Extras)

def clearfields():
    Name.delete(0 ,tk.END)
    Age.delete(0 ,tk.END)
    G1.deselect()
    G2.deselect()
    Height.delete(0 ,tk.END)
    Weight.delete(0 ,tk.END)
    StudentId.delete(0 ,tk.END)
    Activitytype.delete(0 ,tk.END)
    Activity.delete(0 ,tk.END)
    Extra.delete(0 ,tk.END)
#function to Validate entries
def Validate(Names,Ages,Heights,Weights,StudentIds,Activitytypes,Activitys,Extras):

    while True:
        
            if len(Names)==0:
                messagebox.showinfo("Tkinter", "Name cannot be empty")
                break
            elif len(Ages)==0:
                messagebox.showinfo("Tkinter", "Age cannot be empty")
                break
            elif (M.get() == 0) and (F.get() == 0):
                messagebox.showinfo("Tkinter", "Genders cannot be empty")
                break
            elif len(StudentIds)==0:
                messagebox.showinfo("Tkinter", "StudentId cannot be empty")
                break
            elif len(Names)==0 and len(Ages)==0 and (M.get()==0 and M.get()==0)  and len(StudentIds)==0:
                messagebox.showinfo("Tkinter", "Atleast Name,Age,Gender and StudentId must be given!!")
                break
            
            try:
            
                int(Names)
                messagebox.showinfo("Tkinter", "Name must be string")
                break
            except ValueError:
                try:
                    if (M.get() == 1) and (F.get() == 0):
                          
                        cursor.execute("""
                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                        VALUES (?,?,?,?,?)
                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                    elif (M.get() == 0) and (F.get() == 1):
                          
                        cursor.execute("""
                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                        conn.commit()
                        cursor.execute("""
                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                        VALUES (?,?,?,?,?)
                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                        conn.commit()
                        clearfields()
                        
                        messagebox.showinfo("Tkinter", "Saved successfully!")
                        break
                except pyodbc.DataError:
                    
                    try:
                        int(Ages)
                        break
                    except :
                        messagebox.showinfo("Tkinter", "Age must be integer")
                        break
                    else:
                        try:
                            if (M.get() == 1) and (F.get() == 0):
                                  
                                cursor.execute("""
                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                conn.commit()
                                cursor.execute("""
                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                VALUES (?,?,?,?,?)
                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                conn.commit()
                                clearfields()
                        
                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                break
                            elif (M.get() == 0) and (F.get() == 1):
                                  
                                cursor.execute("""
                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                conn.commit()
                                cursor.execute("""
                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                VALUES (?,?,?,?,?)
                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                conn.commit()
                                clearfields()
                        
                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                break
                        

                        except pyodbc.DataError:
                            try:
                                int(Heights)
                                break
                            except :
                                messagebox.showinfo("Tkinter", "Height must be integer")
                                break
                            else:
                                try:
                                    if (M.get() == 1) and (F.get() == 0):
                                          
                                        cursor.execute("""
                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                        conn.commit()
                                        cursor.execute("""
                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                        VALUES (?,?,?,?,?)
                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                        conn.commit()
                                        clearfields()
                                
                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                        break
                                    elif (M.get() == 0) and (F.get() == 1):
                                          
                                        cursor.execute("""
                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                        conn.commit()
                                        cursor.execute("""
                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                        VALUES (?,?,?,?,?)
                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                        conn.commit()
                                        clearfields()
                                
                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                        break
                                except pyodbc.DataError:
                                    try:
                                        int(Weights)
                                        break
                                    except :
                                        messagebox.showinfo("Tkinter", "Weight must be integer")
                                        break
                                    else:
                                        try:
                                            if (M.get() == 1) and (F.get() == 0):
                                                  
                                                cursor.execute("""
                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                conn.commit()
                                                cursor.execute("""
                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                VALUES (?,?,?,?,?)
                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                conn.commit()
                                                clearfields()
                                        
                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                break
                                            elif (M.get() == 0) and (F.get() == 1):
                                                  
                                                cursor.execute("""
                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                conn.commit()
                                                cursor.execute("""
                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                VALUES (?,?,?,?,?)
                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                conn.commit()
                                                clearfields()
                                        
                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                break
                                        except pyodbc.DataError:

                                                    try:
                                                        int(StudentIds)
                                                        break
                                                    except  :
                                                        messagebox.showinfo("Tkinter", "StudentId must be integer")
                                                        break
                                                    else:
                                                        try:
                                                            if (M.get() == 1) and (F.get() == 0):
                                                                  
                                                                cursor.execute("""
                                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                                conn.commit()
                                                                cursor.execute("""
                                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                VALUES (?,?,?,?,?)
                                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                conn.commit()
                                                                clearfields()
                                                        
                                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                break
                                                            elif (M.get() == 0) and (F.get() == 1):
                                                                  
                                                                cursor.execute("""
                                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                                conn.commit()
                                                                cursor.execute("""
                                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                VALUES (?,?,?,?,?)
                                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                conn.commit()
                                                                clearfields()
                                                        
                                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                break
                                                        except pyodbc.DataError:
                                                            try:
                                                                int(Activitytypes)
                                                                messagebox.showinfo("Tkinter", "Activitytype must be string")
                                                                break
                                                            except ValueError:
                                                                try:
                                                                    if (M.get() == 1) and (F.get() == 0):
                                                                          
                                                                        cursor.execute("""
                                                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                                        conn.commit()
                                                                        cursor.execute("""
                                                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                        VALUES (?,?,?,?,?)
                                                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                        conn.commit()
                                                                        clearfields()
                                                                        
                                                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                        break
                                                                    elif (M.get() == 0) and (F.get() == 1):
                                                                          
                                                                        cursor.execute("""
                                                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                                        conn.commit()
                                                                        cursor.execute("""
                                                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                        VALUES (?,?,?,?,?)
                                                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                        conn.commit()
                                                                        clearfields()
                                                                        
                                                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                        break
                                                                except pyodbc.DataError:
                                                                    try:
                                                                        int(Activitys)
                                                                        messagebox.showinfo("Tkinter", "Activity must be string")
                                                                        break
                                                                    except ValueError:
                                                                        try:
                                                                            if (M.get() == 1) and (F.get() == 0):
                                                                                  
                                                                                cursor.execute("""
                                                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                                                conn.commit()
                                                                                cursor.execute("""
                                                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                VALUES (?,?,?,?,?)
                                                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                conn.commit()
                                                                                clearfields()
                                                                                
                                                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                                break
                                                                            elif (M.get() == 0) and (F.get() == 1):
                                                                                  
                                                                                cursor.execute("""
                                                                                INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                                                conn.commit()
                                                                                cursor.execute("""
                                                                                INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                VALUES (?,?,?,?,?)
                                                                                """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                conn.commit()
                                                                                clearfields()
                                                                                
                                                                                messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                                break
                                                                        except pyodbc.DataError:
                                                                            try:
                                                                                int(Extra)
                                                                                messagebox.showinfo("Tkinter", "Extra must be string")
                                                                                break
                                                                            except ValueError:

                                                                                    if (M.get() == 1) and (F.get() == 0):
                                                                                          
                                                                                        cursor.execute("""
                                                                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'m',Heights,Weights))
                                                                                        conn.commit()
                                                                                        cursor.execute("""
                                                                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                        VALUES (?,?,?,?,?)
                                                                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                        conn.commit()
                                                                                        clearfields()
                                                                                        
                                                                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                                        break
                                                                                    elif (M.get() == 0) and (F.get() == 1):
                                                                                          
                                                                                        cursor.execute("""
                                                                                        INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                        VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,'f',Heights,Weights))
                                                                                        conn.commit()
                                                                                        cursor.execute("""
                                                                                        INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                        VALUES (?,?,?,?,?)
                                                                                        """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                        conn.commit()
                                                                                        clearfields()
                                                                                        
                                                                                        messagebox.showinfo("Tkinter", "Saved successfully!")
                                                                                        break
                                                                
                                                        
                                                        
                                

            
      
            

            
                    

            
                
            
                    
                    

            


                    


def Update_Function(StudentIds,Names,Ages,Genders,Heights,Weights,Activitytypes,Activitys,Extras):
    def clear_fielads():
        Name1.delete(0 ,tk.END)
        Age1.delete(0 ,tk.END)
        Gender1.delete(0 ,tk.END)
        Height1.delete(0 ,tk.END)
        Weight1.delete(0 ,tk.END)
        StudentId1.delete(0 ,tk.END)
        Activitytype1.delete(0 ,tk.END)
        Activity1.delete(0 ,tk.END)
        Extra1.delete(0 ,tk.END)
    while True:
        
            if len(Names)==0:
                messagebox.showinfo("Tkinter", "Name cannot be empty")
                break
            elif len(Ages)==0:
                messagebox.showinfo("Tkinter", "Age cannot be empty")
                break
            elif len(Genders)==0:
                messagebox.showinfo("Tkinter", "Genders cannot be empty")
                break
            elif len(StudentIds)==0:
                messagebox.showinfo("Tkinter", "StudentId cannot be empty")
                break
            elif len(Names)==0 and len(Ages)==0 and len(Gender)==0 and len(StudentIds)==0:
                messagebox.showinfo("Tkinter", "Atleast Name,Age,Gender and StudentId must be given!!")
                break
            try:
                
                
                int(Names)
                messagebox.showinfo("Tkinter", "Name must be string")
                break
            except ValueError:
                try:
                    cursor.execute("""delete Students
                            where StudentId = (?)
                            """,(StudentIds))
                    conn.commit()
                    cursor.execute("""delete Activities
                                where StudentId = (?)
                                """,(StudentIds))
                    
                    conn.commit()
                    
                                             
                    cursor.execute("""
                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                    conn.commit()
                    cursor.execute("""
                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                    VALUES (?,?,?,?,?)
                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                    conn.commit()
                    clear_fields()
                        
                    messagebox.showinfo("Tkinter", "Updated successfully!")
                    break

                          
                except pyodbc.DataError:
                    try:
                        int(Ages)
                        break
                    except :
                        messagebox.showinfo("Tkinter", "Age must be integer")
                        break
                    else:
                        try:

                                  
                            cursor.execute("""
                            INSERT INTO Students(studentId,name,age,gender,height,weight)
                            VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                            conn.commit()
                            cursor.execute("""
                            INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                            VALUES (?,?,?,?,?)
                            """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                            conn.commit()
                            clear_fields()
                        
                            messagebox.showinfo("Tkinter", "Updated successfully!")
                            break
                           

                        except pyodbc.DataError:
                            try:
                                int(Genders)
                                messagebox.showinfo("Tkinter", "enter m for male and f for female")
                                break
                            except ValueError:
                                try:
                                    cursor.execute("""delete Students
                                            where StudentId = (?)
                                            """,(StudentIds))
                                    conn.commit()
                                    cursor.execute("""delete Activities
                                                where StudentId = (?)
                                                """,(StudentIds))
                                    
                                    conn.commit()
                                    
                                                             
                                    cursor.execute("""
                                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                    conn.commit()
                                    cursor.execute("""
                                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                    VALUES (?,?,?,?,?)
                                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                    conn.commit()
                                    clear_fields()
                                        
                                    messagebox.showinfo("Tkinter", "Updated successfully!")
                                    break

                                          
                                except pyodbc.DataError:
                                    try:
                                        int(Heights)
                                        break
                                    except :
                                        messagebox.showinfo("Tkinter", "Height must be integer")
                                        break
                                    else:
                                        try:

                                                  
                                            cursor.execute("""
                                            INSERT INTO Students(studentId,name,age,gender,height,weight)
                                            VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                            conn.commit()
                                            cursor.execute("""
                                            INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                            VALUES (?,?,?,?,?)
                                            """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                            conn.commit()
                                            clear_fields()
                                        
                                            messagebox.showinfo("Tkinter", "Updated successfully!")
                                            break
                                           

                                        except pyodbc.DataError:
                                            try:
                                                int(Weights)
                                                break
                                            except :
                                                messagebox.showinfo("Tkinter", "Weight must be integer")
                                                break
                                            else:
                                                try:

                                                          
                                                    cursor.execute("""
                                                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                    conn.commit()
                                                    cursor.execute("""
                                                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                    VALUES (?,?,?,?,?)
                                                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                    conn.commit()
                                                    clear_fields()
                                                
                                                    messagebox.showinfo("Tkinter", "Updated successfully!")
                                                    break
                                                except pyodbc.DataError:
                                                    try:
                                                        int(StudentIds)
                                                        break
                                                    except :
                                                        messagebox.showinfo("Tkinter", "StudentId must be integer")
                                                        break
                                                    else:
                                                        try:

                                                                  
                                                            cursor.execute("""
                                                            INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                            VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                            conn.commit()
                                                            cursor.execute("""
                                                            INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                            VALUES (?,?,?,?,?)
                                                            """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                            conn.commit()
                                                            clear_fields()
                                                        
                                                            messagebox.showinfo("Tkinter", "Updated successfully!")
                                                            break
                                                        except pyodbc.DataError:
                                                            try:
                
                
                                                                int(Activtytypes)
                                                                messagebox.showinfo("Tkinter", "Activity type must be string")
                                                                break
                                                            except ValueError:
                                                                try:
                                                                    cursor.execute("""delete Students
                                                                            where StudentId = (?)
                                                                            """,(StudentIds))
                                                                    conn.commit()
                                                                    cursor.execute("""delete Activities
                                                                                where StudentId = (?)
                                                                                """,(StudentIds))
                                                                    
                                                                    conn.commit()
                                                                    
                                                                                             
                                                                    cursor.execute("""
                                                                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                                    conn.commit()
                                                                    cursor.execute("""
                                                                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                    VALUES (?,?,?,?,?)
                                                                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                    conn.commit()
                                                                    clear_fields()
                                                                        
                                                                    messagebox.showinfo("Tkinter", "Updated successfully!")
                                                                    break

                                                                          
                                                                except pyodbc.DataError:
                                                                    try:
                
                
                                                                        int(Activitys)
                                                                        messagebox.showinfo("Tkinter", "Activity must be string")
                                                                        break
                                                                    except ValueError:
                                                                        try:
                                                                            cursor.execute("""delete Students
                                                                                    where StudentId = (?)
                                                                                    """,(StudentIds))
                                                                            conn.commit()
                                                                            cursor.execute("""delete Activities
                                                                                        where StudentId = (?)
                                                                                        """,(StudentIds))
                                                                            
                                                                            conn.commit()
                                                                            
                                                                                                     
                                                                            cursor.execute("""
                                                                            INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                            VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                                            conn.commit()
                                                                            cursor.execute("""
                                                                            INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                            VALUES (?,?,?,?,?)
                                                                            """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                            conn.commit()
                                                                            clear_fields()
                                                                                
                                                                            messagebox.showinfo("Tkinter", "Updated successfully!")
                                                                            break

                                                                                  
                                                                        except pyodbc.DataError:
                                                                            try:
                
                
                                                                                int(Names)
                                                                                messagebox.showinfo("Tkinter", "Name must be string")
                                                                                break
                                                                            except ValueError:
                                                                                try:
                                                                                    cursor.execute("""delete Students
                                                                                            where StudentId = (?)
                                                                                            """,(StudentIds))
                                                                                    conn.commit()
                                                                                    cursor.execute("""delete Activities
                                                                                                where StudentId = (?)
                                                                                                """,(StudentIds))
                                                                                    
                                                                                    conn.commit()
                                                                                    
                                                                                                             
                                                                                    cursor.execute("""
                                                                                    INSERT INTO Students(studentId,name,age,gender,height,weight)
                                                                                    VALUES (?,?,?,?,?,?)""",(StudentIds,Names,Ages,Genders,Heights,Weights))
                                                                                    conn.commit()
                                                                                    cursor.execute("""
                                                                                    INSERT INTO Activities(studentId,name,activity_type,activity,extra_activity)
                                                                                    VALUES (?,?,?,?,?)
                                                                                    """,(StudentIds,Names,Activitytypes,Activitys,Extras))
                                                                                    conn.commit()
                                                                                    clear_fields()
                                                                                        
                                                                                    messagebox.showinfo("Tkinter", "Updated successfully!")
                                                                                    break
                                                                                except:
                                                                                    pass

                                                                                          
                                                                                
                                            
                                            
                        
    

        
    
def Search():
 
        Names= Name.get()
        Ages= Age.get()

        Heights= Height.get()
        Weights= Height.get()
        StudentIds= StudentId.get()
        Activitytypes=Activitytype.get()
        Activitys=Activity.get()
        Extras=Extra.get()

        

# clearing the tree
       
        t=tree.get_children()
        for f in t:
            tree.delete(f)
        

#Search starts
            

        if len(Names)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Name like(?)""",(Names))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
                    
		
        elif  len(Ages)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Age like(?)""",(Ages))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif (M.get() == 1) and (F.get() == 0):
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Gender like 'm'""")
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
        elif (M.get() == 0) and (F.get() == 1):
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Gender like 'f'""")
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

        elif  len(Heights)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.Height like(?)""",(Heights))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)          


        elif  len(Weights)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where A.weight like(?)""",(Weights))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(StudentIds)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Sports B on A.StudentId=B.StudentId where A.StudentId like(?)""",(Rollnos))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)


        elif  len(Activitytypes)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where B.activitytypes like(?)""",(Activitytypes))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

                
        elif  len(Activitys)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where B.activity like(?)""",(Activitys))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)
                

        elif  len(Extras)!=0:
            cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
            from Students A inner join Activities B on A.StudentId=B.StudentId where B.extra like(?)""",(estras))
            records=cursor.fetchall()
            for row in records:
                tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
                tree.pack(side=tk.TOP,fill=tk.X)

        else:
            
            messagebox.showinfo("Tkinter", "Atleast one search criteria must be given!")     

#Search ends

def Delete():
        x=StudentId.get()
        cursor.execute("""
        DELETE FROM Students
        WHERE StudentId = (?)""",(x))
        conn.commit()
        cursor.execute("""
        DELETE FROM Activities
        WHERE StudentId = (?)""",(x))
        conn.commit()
        clearfields()
        messagebox.showinfo("Tkinter", "Deleted successfully!")

def getallrecords():
    t=tree.get_children()
    for f in t:
        tree.delete(f)
    cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity
    from Students A inner join Activities B on A.studentId=B.studentId""")
    records=cursor.fetchall()
    for row in records:
        tree.insert("", 3, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))
        tree.pack(side=tk.TOP,fill=tk.X)




def create_new_window():
    def Search():
     
            Name1s= Name1.get()
            Age1s= Age1.get()
            Height1s= Height1.get()
            Weight1s= Weight1.get()
            StudentId1s= StudentId1.get()
            Activitytype1s=Activitytype1.get()
            Activitie1s=Activity1.get()
            Extra1s=Extra1.get()

            

    
           

            

    #Search starts
                

            if len(Name1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A.Name like(?)""",(Name1s))
                records=cursor.fetchall()
                for row in records:
                    
                    Age1.insert(0,row[1])
                    
                    Gender1.insert(0,row[2])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])
                    
                        
                    
            elif  len(Age1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A.Age like(?)""",(Age1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Gender1.insert(0,row[2])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])




                    
            elif  len(Gender1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A.Gender like(?) """,(Gender1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Gender1.insert(0,row[2])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])


            elif  len(Height1s!=0):
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A.Height like(?)""",(Height1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Gender1.insert(0,row[2])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])          


            elif  len(Weight1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where A._Weight like(?)""",(Weight1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Height1.insert(0,row[3])
                    Gender1.insert(0,row[2])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])


            elif  len(StudentId1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Sports B on A.StudentId=B.StudentId where A.StudentId like(?)""",(StudentId1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    Gender1.insert(0,row[2])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])


            elif  len(Activitytype1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where B.Activitytypes like(?)""",(Activitytype1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Gender1.insert(0,row[2])
                    Activity1.insert(0,row[7])
                    Extra1.insert(0,row[8])

                    
            elif  len(Activitie1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where B.Activity like(?)""",(Activitie1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Gender1.insert(0,row[2])
                    Extra1.insert(0,row[8])
                    

            elif  len(Extra1s)!=0:
                cursor.execute("""select A.name,A.age,A.gender,A.height,A.weight,A.studentId,B.activity_type,B.activity,B.extra_activity
                from Students A inner join Activities B on A.StudentId=B.StudentId where B.Extra like(?)""",(Estra1s))
                records=cursor.fetchall()
                for row in records:
                    Name1.insert(0,row[0])
                    Age1.insert(0,row[1])
                    Gender1.insert(0,row[2])
                    Height1.insert(0,row[3])
                    Weight1.insert(0,row[4])
                    StudentId1.insert(0,row[5])
                    Activitytype1.insert(0,row[6])
                    Activity1.insert(0,row[7])
                    

            else:
                
                messagebox.showinfo("Tkinter", "Atleast one search criteria must be given!")

    

    def Update():
        Name1s= Name1.get()
        Age1s= Age1.get()
        Height1s= Height1.get()
        Weight1s= Weight1.get()
        StudentId1s= StudentId1.get()
        Activitytype1s=Activitytype1.get()
        Activitie1s=Activity1.get()
        Extra1s=Extra1.get()
        Gender1s=Gender1.get()
        Update_Function(StudentId1s,Name1s,Age1s,Gender1s,Height1s,Weight1s,Activitytype1s,Activitie1s,Extra1s)


        
    root2=tk.Tk()
    root2.title("Class4c-update record")
    canvas2 = tk.Canvas(root2, width = 900, height = 300)
    canvas2.pack()




    Name1 = tk.Entry (root2)
    canvas2.create_window(300, 10, window=Name1)
    label1 = tk.Label(root2, text='Name:')
    label1.config(font=('helvetica', 10))
    canvas2.create_window(200, 10, window=label1)


    Age1 = tk.Entry (root2)
    canvas2.create_window(300, 40, window=Age1)
    label2 = tk.Label(root2 , text='Age:')
    label2.config(font=('helvetica', 10))
    canvas2.create_window(200, 40, window=label2)



    label31 = tk.Label(root2, text='Gender:')
    label31.config(font=('helvetica', 10))
    canvas2.create_window(200, 70, window=label31)
    Gender1 = tk.Entry (root2)
    canvas2.create_window(300, 70, window=Gender1)

    


    Height1 = tk.Entry (root2)
    canvas2.create_window(300, 100, window=Height1)
    label4 = tk.Label(root2, text='height in cm:')
    label4.config(font=('helvetica', 10))
    canvas2.create_window(195, 100, window=label4)

    Weight1 = tk.Entry (root2)
    canvas2.create_window(300, 130, window=Weight1)
    label5 = tk.Label(root2, text='weight in kg:')
    label5.config(font=('helvetica', 10))
    canvas2.create_window(195, 130, window=label5)

    StudentId1 = tk.Entry (root2)
    canvas2.create_window(300, 160, window=StudentId1)
    label6 = tk.Label(root2, text='StudentId:')
    label6.config(font=('helvetica', 10))
    canvas2.create_window(200, 160, window=label6)

    Activitytype1 = tk.Entry (root2)
    canvas2.create_window(300, 190, window=Activitytype1)
    label7 = tk.Label(root2, text='Activitytype:')
    label7.config(font=('helvetica', 10))
    canvas2.create_window(200, 190, window=label7)


    Activity1 = tk.Entry (root2)
    canvas2.create_window(500, 10, window=Activity1)
    label8 = tk.Label(root2, text='Activity:')
    label8.config(font=('helvetica', 10))
    canvas2.create_window(400, 10, window=label8)

    Extra1 = tk.Entry (root2)
    canvas2.create_window(500, 40, window=Extra1)
    label9 = tk.Label(root2, text='Extra:')
    label9.config(font=('helvetica', 10))
    canvas2.create_window(400, 40, window=label9)

    button6 = tk.Button(root2,text='get',command=Search)
    canvas2.create_window(400, 250, window=button6)

    button5 = tk.Button(root2,text='Update',command=Update)
    canvas2.create_window(350, 250, window=button5)

# defining the canvas

root= tk.Tk()
root.title("Class4c")
canvas1 = tk.Canvas(root, width = 900, height = 300)
canvas1.pack()



# Defining the fields and labels and validating

Name = tk.Entry (root)
canvas1.create_window(300, 10, window=Name)
label1 = tk.Label(root, text='Name:')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 10, window=label1)


Age = tk.Entry (root)
canvas1.create_window(300, 40, window=Age)
label2 = tk.Label(root, text='Age:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 40, window=label2)



label3 = tk.Label(root, text='Gender:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 70, window=label3)


M = IntVar()
G1 = Checkbutton(
    root, text="M", variable=M,
    onvalue=1, offvalue=0)

F = IntVar()
G2 = Checkbutton(
    root, text="F", variable=F,
    onvalue=1, offvalue=0)

canvas1.create_window(350, 70, window=G1)
canvas1.create_window(250, 70, window=G2)


Height = tk.Entry (root)
canvas1.create_window(300, 100, window=Height)
label4 = tk.Label(root, text='height in cm:')
label4.config(font=('helvetica', 10))
canvas1.create_window(195, 100, window=label4)

Weight = tk.Entry (root)
canvas1.create_window(300, 130, window=Weight)
label5 = tk.Label(root, text='weight in kg:')
label5.config(font=('helvetica', 10))
canvas1.create_window(195, 130, window=label5)

StudentId = tk.Entry (root)
canvas1.create_window(300, 160, window=StudentId)
label6 = tk.Label(root, text='StudentId:')
label6.config(font=('helvetica', 10))
canvas1.create_window(200, 160, window=label6)

Activitytype = tk.Entry (root)
canvas1.create_window(300, 190, window=Activitytype)
label7 = tk.Label(root, text='Activitytype:')
label7.config(font=('helvetica', 10))
canvas1.create_window(200, 190, window=label7)


Activity = tk.Entry (root)
canvas1.create_window(500, 10, window=Activity)
label8 = tk.Label(root, text='Activity:')
label8.config(font=('helvetica', 10))
canvas1.create_window(400, 10, window=label8)

Extra = tk.Entry (root)
canvas1.create_window(500, 40, window=Extra)
label9 = tk.Label(root, text='Extra:')
label9.config(font=('helvetica', 10))
canvas1.create_window(400, 40, window=label9)





# Defining the buttons

Save_Button = tk.Button(text='Save',command = Save)
canvas1.create_window(500, 250, window=Save_Button)

Search_Button = tk.Button(text='Search',command=Search)
canvas1.create_window(400, 250, window=Search_Button)

Delete_Button = tk.Button(text='Delete',command=Delete)
canvas1.create_window(450, 250, window=Delete_Button)

Show_All_Records = tk.Button(text='Get all records',command=getallrecords)
canvas1.create_window(330, 250, window=Show_All_Records)

Update_Button = tk.Button(text='Update',command=create_new_window)
canvas1.create_window(260, 250, window=Update_Button)

# Defining the tree

tree=ttk.Treeview(root)
tree["columns"]=("one","two","three","four","five","six")
tree.column("#0", width=130, minwidth=270, stretch=tk.NO)
tree.column("one", width=100, minwidth=150, stretch=tk.NO)
tree.column("two", width=100, minwidth=100)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.column("three", width=100, minwidth=50, stretch=tk.NO)
tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Age",anchor=tk.W)
tree.heading("two", text="Gender",anchor=tk.W)
tree.heading("three", text="Height",anchor=tk.W)
tree.heading("four", text="Weight",anchor=tk.W)
tree.heading("five", text="StudentId",anchor=tk.W)
tree.heading("six", text="Activity",anchor=tk.W)
tree.pack()



root.mainloop()
