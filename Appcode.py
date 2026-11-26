from tkinter import *
from tkinter import ttk
import requests
def data_get():
    city= city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cc73d5a355440e5059c9bd210115e5ec").json()
    climate_Label1.config(text=data["weather"][0]["main"])
    D_Label2.config(text=data["weather"][0]["description"])
    Temp_Label3.config(text=str(int(data["main"]["temp"]-272.15)))
    Tempmin_Label4.config(text=str(int(data["main"]["temp_min"]-272.15)))
    Tempmax_Label5.config(text=str(int(data["main"]["temp_max"]-272.15)))
win = Tk()
win.title("Weather App")
win.config(bg="light blue")
win.geometry("600x600")


name_Label = Label(win, text="Mausam Wibhag App",
                   font=("Times New Roman", 25, "bold"),
                   fg="black", bg="light blue")
name_Label.place(x=25, y=50, height=50, width=550)


list_name= (
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi",
    "Jammu and Kashmir",
    "Ladakh",
    "Lakshadweep",
    "Puducherry"
)
city_name=StringVar()
box= ttk.Combobox(win, text="Mausam Wibhag App",values=list_name,
                  font= ("arial",20,"bold"),textvariable= city_name)
box.place(x=75,y=130,height=50,width=450)

button = Button(win, text="Check",font= ("arial",20,"bold"),command=data_get)
button.place(x=250,y=200,height=50,width=100)


climate_Label = Label(win, text="Weather Climate: ",
                      font= ("time new roman",15),
                      bg="light blue")
climate_Label.place(x=20,y=260,height=40,width=210)

climate_Label1 = Label(win, text=" ", font= ("time new roman",15),bg="sky blue")
climate_Label1.place(x=235,y=260,height=40,width=150)

D_Label = Label(win, text="Weather Description: ", font= ("time new roman",15),bg="light blue")
D_Label.place(x=20,y=310,height=40,width=210)


D_Label2 = Label(win, text=" ", font= ("time new roman",15),bg="sky blue")
D_Label2.place(x=235,y=310,height=40,width=150)


Temp_Label = Label(win, text="Temp:", font= ("time new roman",15),bg="light blue")
Temp_Label.place(x=20,y=360,height=40,width=210)

Temp_Label3 = Label(win, text=" ", font= ("time new roman",15),bg="sky blue")
Temp_Label3.place(x=235,y=360,height=40,width=150)


Tempmin_Label = Label(win, text="Temp min:", font= ("time new roman",15),bg="light blue")
Tempmin_Label.place(x=20,y=410,height=40,width=210)

Tempmin_Label4 = Label(win, text=" ", font= ("time new roman",15),bg="sky blue")
Tempmin_Label4.place(x=235,y=410,height=40,width=150)

Tempmax_Label = Label(win, text="Temp Max: ", font= ("time new roman",15),bg="light blue")
Tempmax_Label.place(x=20,y=460,height=40,width=210)

Tempmax_Label5 = Label(win, text=" ", font= ("time new roman",15),bg="sky blue")
Tempmax_Label5.place(x=235,y=460,height=40,width=150)

win.mainloop()











