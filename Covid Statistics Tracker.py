from tkinter import *
from tkinter.font import Font 
import urllib.request # pip install requests 
from datetime import datetime # when did the user seach for any country using our app
from matplotlib.pyplot import figure, ylabel,xlabel,show # pip install matplotlib(numpy)
from seaborn import despine, barplot # pip install seaborn
from numpy import array # pip install numpy
from pandas import DataFrame # pip install pandas 
from covid import Covid # pip install covid

root = Tk()
root.title("CF Covid Tracker")
root.geometry("600x450+500+150")

blue = '#081D54'
root['bg'] = bluee 

big_font = Font(family='Helvetica',size=40,weight='bold')
mid_font = Font(family='Helvetica',size=17,weight='bold')
small_font = Font(family='Helvetica',size=10,weight='bold')
textarea_font =  Font(family='rockwell',size=20,weight='bold')

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

test = connect()
connection = Label(bg=bluee,fg='white',pady=2)
connection.config(text=f'\nConnected: {test}',font=small_font)
connection.pack(fill=X)

heading = Label(text='CF Covid Tracker',font=big_font,bd=8,bg=bluee,fg='white',pady=1)
heading.pack(fill=X)

enter_country_name_label = Label(text='Enter country name ',fg='white',bg=bluee,bd=8,pady=1)
enter_country_name_label.pack(fill=BOTH)

enter_country_name = Entry(root,font=textarea_font,justify='center')
enter_country_name.pack(pady=1)
enter_country_name.focus()

country = label(root,bg=bluee,fg='white',font=mid_font)
country.pack()

confirm = label(root,bg=bluee,fg='white',font=mid_font)
confirm .pack()

active = label(root,bg=bluee,fg='white',font=mid_font)
active.pack()

death = label(root,bg=bluee,fg='white',font=mid_font)
death.pack()

recovered = label(root,bg=bluee,fg='white',font=mid_font)
recovered.pack()

last_updated = Label(root)


def plotGraph(dfn):
    ndf = dfn[['confirmed','active','death','recovered']]
    ndf = ndf.T # distribute each column particulary
    figure(figsize=(5.5,5))
    for col in ndf.columns:
        pass
    plot = barplot(x=ndf.index,y=col,data=ndf)
    despine() # remove border
    for p in plot.patches:
        plot.annotate(format(p.get_height(),'1f',
                             p.get_x,p.get_width()/2.,p.get_height()),
                             ha='center',va='center',
                             xytext = (0,9),
                             textcoords="offset points")

    xlabel = ('DATA')
    ylabel = ("COUNT")
    show()


def getData(country_name,country):
    if test: # test is true/passed/connected
        data = Covid()
        data = data.get_data()
        df = DataFrame(data)
        country_name = country_name.get()
        dfn = df[country_name==df['country'].str.lower()]
        df = array(dfn)
        country_ = df[0][1]
        confirm_ = df[0][2]
        active_ = df[0][3]
        death_ = df[0][4]
        recovered_ = df[0][5]
        time_ = df[0][8]/1000
        last_update_ = datetime.fromtimestamp(time_).strftime('%d-%m-%Y %H:%M:%S')
        print(last_update_)

    country.configure(text=f"Country: {country_}")
    confirm.configure(text=f"Country: {confirm_}")
    active.configure(text=f"Country: {active_}")
    death.configure(text=f"Country: {death_}")
    recovered.configure(text=f"Country: {recovered_}")
    plotGraph(dfn)


root.bind('<Return>',(lambda x: getData(enter_country_name,country)))

root.mainloop()



