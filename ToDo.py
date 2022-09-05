import json
import termine as T
import tkinter as tk

class class_jahr:
    def __init__(self, name):
        self.name=name
        self.ref_monate=list()
        i=0
        while i < 12:
            self.ref_monate.append(
            class_monat(
                    name=quary_json_data(liste_monate=(i, "name")),
                    stelle=i,
                    tagesraum=quary_json_data(liste_monate=(i, "tageszeitraum")),
                    anz_tage=quary_json_data(liste_monate=(i, "anz_days")),
                    ref_jahr=self
                )
            )
            i+=1
        
    def give_monat_ref(self, monat=int()):
        return self.ref_monate[monat]
             
class class_monat:
    def __init__(self, name=str(), stelle=int(), tagesraum=list(), anz_tage=int(), ref_jahr=object()):
        self.ref_jahr=ref_jahr
        self.name=name
        self.stelle=stelle
        self.anz_tage=anz_tage
        self.tagesraum=tagesraum
        self.ref_tage=list()
        self.anz_termine=anz_termine_monat(self.stelle)
        
        i=0
        while i < self.anz_tage:
            if i == 0:
                tag_name=int(quary_json_data(liste_monate=(i, "anfangs_tag")))
            else:
                tag_name+=1
                if tag_name>7:
                    tag_name=1
            self.ref_tage.append(
                class_tag(
                    monat=self.stelle,
                    stelle=i,
                    name=quary_json_data(liste_tag_namen=tag_name),
                    jahrestag=self.tagesraum[0] + i,
                )
            )
            i+=1
            
    def give_anz_termine(self):
        return self.anz_termine
        
class class_tag:
    def __init__(self, stelle=int(), name=str(), jahrestag=int(), monat=int()):
        self.stelle = stelle
        self.name=name
        self.jahrestag=jahrestag
        self.termin_anzahl=None
        self.monat=monat
        self.termin_list=quary_termine(monat=self.monat, tag=self.stelle)
            
        

class class_termin:
    def __init__(self, name, id, von, bis, text, fabe, tag, monat):
        self.name = name
        self.id = id
        self.von_bis = [von, bis]
        self.text = text
        self.fabe =fabe
        self.tag=tag
        self.monat=monat
        
class display_monate:
    def __init__(self):
        self.frame_list=list()
        self.termine_list=list()
        self.total_frame=tk.Frame(root)
        
        for monat in range(12):
            frame = tk.LabelFrame(self.total_frame)
            top_frame=tk.Frame(frame, relief="solid", borderwidth=2)
            
            monats_name=tk.Label(top_frame, text=quary_json_data(liste_monate=(monat, "name")), width=20, height=2)
            monats_num=tk.Label(top_frame, text=f"{monat+1}",width=3, height=2)
            
            anz_termine=tk.Label(frame, text="Anzahl Termine:")
            anz_termine_num=tk.Label(frame, text=ref_jahr.give_monat_ref(monat).give_anz_termine())
            
            for x in range(2, 11):
                termine_show=tk.Label(frame, text="xxx")
                termine_show_num=tk.Label(frame, text=f"{x-1}.")
                
                self.termine_list.append((termine_show, termine_show_num))
                
                termine_show.grid(column=0, row=x)
                termine_show_num.grid(column=1, row=x)
            
            ########################
            # Hier gehts weiter!!! #
            ########################
            
            ansehen=tk.Button(frame, text="Ansehen", command=None)

            monats_name.grid(column=0, row=0)
            monats_num.grid(column=1, row=0)
            
            top_frame.grid(column=0 , row=0, columnspan=2)
            
            anz_termine.grid(column=0, row=1)
            anz_termine_num.grid(column=1, row=1)
            
            self.frame_list.append(frame)

            x=1
            y=0
            for frame in self.frame_list:
                frame.grid(column=x, row=y, padx=20, pady=20)
                if x%4==0 and x!=1:
                    y+=1
                    x=0
                x+=1
                
            ansehen.grid(column=0, row=11, columnspan=2)
                
            
        
    def dislpay(self):
        #bewegt sich nicht mit und macht probleme wenn die rechte seite verändert wird
        #self.total_frame.grid(row=0, column=0, padx=400, pady=50)
        self.total_frame.pack()
        
class display_tag:
    def __ini__(self):
        self.frame_list=list()
        
        for monat in range(12):
            monat_frame=tk.Frame(root)
            self.frame_list.append(monat_frame)
            for tag in range(quary_json_data(liste_monate=(monat, "anz_days"))):
                pass
                
            
    
def anz_termine_monat(monat=int()):
    anz_termine=0
    with open("JSON/termine_data.json", "r") as data_file:
        data = json.load(data_file)
        data_monat = data.get("data")
        if data_monat.get(str(monat)) > 0:
            anz_termine=data_monat.get(str(monat))
    return anz_termine 
    
    
        
# such nach terminen an einem tag und gib diese in einem objeckt wieder
def quary_termine(monat,tag):
    termine_list=list()
    try:
        with open("JSON/termine_data.json", "r") as data_file:
            data = json.load(data_file)
            tag = data.get(str(monat)).get(str(tag))
            if len(tag.keys()) < 1:
                pass
            else:
                for key in tag.keys():
                    termine=tag.get(key)
                    termine_list.append(class_termin(
                        name=termine.get("name"),
                        id=termine.get("id"),
                        von=termine.get("von"),
                        bis=termine.get("bis"),
                        text=termine.get("text"),
                        fabe=termine.get("fabe"),
                        tag=int(key),
                        monat=monat
                        ))
    except:
        print("datei eror: termine_data.json")
    finally:
        return termine_list
    
    
# sucht nach daten zum kalender
#jahr für infos zum ganzen jahr#
#liste_tag_namen macht aus 1-7 namen wie Montag
#liste_monate git infos über ein bestimten monat
#wird in tupel angegeben (monat in int, name von para)
def quary_json_data(jahr=None, liste_tag_namen=None, liste_monate=None):
    try:
        ero = None
        with open("JSON/kalender_data.json", "r") as data_file:
                data = json.load(data_file)
                if jahr!=None:
                    result_1 = data.get(jahr)
                    if result_1 == None:
                        print(jahr, "nicht in dict")
                    else:    
                        return result_1
                if liste_tag_namen!=None:
                    if type(liste_tag_namen) != int:
                        ero=f"{liste_tag_namen} inst kein int"
                        raise TypeError(liste_tag_namen + "inst kein int")
                    result_2 = data.get("liste_tag_namen").get(str(liste_tag_namen))
                    if result_2 == None:
                        print(liste_tag_namen, "nicht in dict")
                    else:
                        return result_2
                if liste_monate != None:
                    if type(liste_monate) != tuple:
                        ero=f"{liste_monate} inst kein tupel"
                        raise TypeError(liste_monate + "inst kein tupel")
                    result_3 = data.get("list_monate")[liste_monate[0]].get(liste_monate[1])
                    if result_3 == None:
                        print(liste_monate[1],"nicht in dict")
                    else:
                        return result_3
    except:
        print("ToDO\JSON\Termine_data.json kommte nicht geöfnet werden")
    finally:
        if ero != None:
            print(ero)

if __name__=="__main__":
    ref_jahr = class_jahr(name=quary_json_data(jahr="name"))
    gui=True
    if gui:
        root = tk.Tk()
        root.title("Kalender 2022")
        root.geometry("1920x1080")
        
        monat_display=display_monate()
        monat_display.dislpay()
        
        tag_display=display_tag()
        
        root.mainloop()
