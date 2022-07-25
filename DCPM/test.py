# import tkinter 
# from tkinter import *

# root = Tk() 
# root.title("PARÁMETROS MORFOMÉTRICOS DE LA CUENCA") 
# root.geometry("450x360")
 
# NC_label = Label(root, text = "Número de curva:") 
# NC_label.grid(row = 1, column = 1) 
# NC_Int = IntVar() 
# NC_entry = Entry(root, textvariable = NC_Int) 
# NC_entry.grid(row = 1, column = 2) 
# numcur=NC_Int.get()
 
# ok = Button(root, text = "OK",  command = root.destroy) 
# ok.grid(row = 2, column = 2) 
# def mostrar():
#     numcur= NC_Int.get()
#     print(numcur)
 
# ok.config(command=mostrar) 
# root.mainloop()

# import tkinter

# root = tkinter.Tk()
# root.title("Bookings")
# root.geometry("700x500")

# frame_title = tkinter.Frame(root)
# frame_fields = tkinter.Frame(root)
# frame_scan = tkinter.Frame(root)
# frame_credentials = tkinter.Frame(root)
# frame_site = tkinter.Frame(root)
# frame_change = tkinter.Frame(root)


# def passx():
#     pass

# frame_title.grid(row=0, column=0, padx=(50, 0))
# title = tkinter.Label(frame_title, text="Bookings Scan", font=("Helvetica", 24))
# title.grid(pady=(27, 10))
# frame_fields.grid(row=1, column=0, padx=(30, 0), pady=(10, 0))
# start_date_lbl = tkinter.Label(frame_fields, text="Enter the start date: ", font=("Helvetica", 16))
# start_date_lbl.grid(column=0, row=0, pady=15)
# start_date_unp = tkinter.Entry(frame_fields, width=11, font=("Helvetica", 16))
# start_date_unp.grid(column=1, row=0)
# start_date = start_date_unp.get()
# end_date_lbl = tkinter.Label(frame_fields, text="Enter the end date: ", font=("Helvetica", 16))
# end_date_lbl.grid(column=0, row=1)
# end_date_unp = tkinter.Entry(frame_fields, width=11, font=("Helvetica", 16))
# end_date_unp.grid(column=1, row=1)
# end_date = end_date_unp.get()
# frame_scan.grid(row=1, column=1, padx=(45, 0))
# scan_btn = tkinter.Button(frame_scan, text="Scan", command=passx, height=2, width=8, font=("Helvetica", 16))
# scan_btn.grid(row=0, column=0, pady=(10, 0))
# frame_credentials.grid(row=2, column=0)
# credential = tkinter.IntVar(value=0)
# tkinter.Radiobutton(frame_credentials, text="Username", variable=credential, value=1, font=("Helvetica", 16)).grid(column=1, row=4, sticky="W", pady=(43, 50))
# tkinter.Radiobutton(frame_credentials, text="Password", variable=credential, value=2, font=("Helvetica", 16)).grid(column=1, row=5, sticky="W")
# frame_site.grid(row=2, column=1, pady=(40, 0))
# site = tkinter.IntVar(value=0)
# tkinter.Radiobutton(frame_site, text="PearsonVUE", variable=site, value=1, font=("Helvetica", 16)).grid(column=0, row=0, sticky="W", pady=8)
# tkinter.Radiobutton(frame_site, text="Kryterion", variable=site, value=2, font=("Helvetica", 16)).grid(column=0, row=1, sticky="W")
# tkinter.Radiobutton(frame_site, text="PSI PAN", variable=site, value=3, font=("Helvetica", 16)).grid(column=0, row=2, sticky="W", pady=8)
# tkinter.Radiobutton(frame_site, text="Scantron", variable=site, value=4, font=("Helvetica", 16)).grid(column=0, row=3, sticky="W")
# tkinter.Radiobutton(frame_site, text="PSI Atlas", variable=site, value=5, font=("Helvetica", 16)).grid(column=0, row=4, sticky="W", pady=8)
# frame_change.grid(row=2, column=2, padx=25, pady=(20, 0))
# change_btn = tkinter.Button(frame_change, text="Change", command=passx, height=2, width=8, font=("Helvetica", 16))
# change_btn.grid(column=3, row=3)
# root.mainloop()



