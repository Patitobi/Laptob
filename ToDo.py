import json
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
        self.termin_list=quary_termine_tag(monat=self.monat, tag=self.stelle)
            
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
        self.button_list=list()
        self.total_frame=None
        self.button_creat_bool=False
        
        self.display_lode()
        
    def display_lode(self):
        
        for monat in range(12):
            if len(self.frame_list)<12:
                self.frame_list.append(None)
   
            if self.total_frame == None:
                self.total_frame=tk.Frame(root)
            elif self.total_frame!=None and monat==0:
                self.total_frame=None
                self.total_frame=tk.Frame(root)
            frame = tk.LabelFrame(self.total_frame)
            top_frame=tk.Frame(frame, relief="solid", borderwidth=2)
            
            monats_name=tk.Label(top_frame, text=quary_json_data(liste_monate=(monat, "name")), width=20, height=2)
            monats_num=tk.Label(top_frame, text=f"{monat+1}",width=3, height=2)
            
            anz_termine=tk.Label(frame, text="Anzahl Termine:")
            anz_termine_num=tk.Label(frame, text=ref_jahr.give_monat_ref(monat).give_anz_termine())
            
            termine_monat=quary_termine_monat(monat_int=monat)
            z=0
            for x in range(2, 11):
                termine_show=tk.Label(frame, text=termine_monat[z].name)
                termine_show_num=tk.Label(frame, text=f"{termine_monat[z].tag}.")
                
                self.termine_list.append((termine_show, termine_show_num))
                
                termine_show.grid(column=0, row=x)
                termine_show_num.grid(column=1, row=x)
                z+=1

            self.button_creat(monat, frame)
            
            
            monats_name.grid(column=0, row=0)
            monats_num.grid(column=1, row=0)
            
            top_frame.grid(column=0 , row=0, columnspan=2)
            
            anz_termine.grid(column=0, row=1)
            anz_termine_num.grid(column=1, row=1)
            
            self.frame_list[monat]=frame
            self.button_list[monat].grid(column=0, row=15, columnspan=2)  
            
        x=1
        y=0
        for frame in self.frame_list:
            frame.grid(column=x, row=y, padx=20, pady=20)
            if x%4==0 and x!=1:
                y+=1
                x=0
                
            x+=1
                  
            
        
    def button_creat(self, monat, frame):
        if len(self.button_list)==0 or self.button_list[11]==None:
            if not self.button_creat_bool:
                for x in range(12):
                    self.button_list.append(None)
            self.button_creat_bool=True
            if monat==0:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=0)]
                )
            elif monat==1:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=1)]
                )
            elif monat==2:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=2)]
                )
            elif monat==3:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=3)]
                )
            elif monat==4:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=4)]
                )
            elif monat==5:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=5)]
                )
            elif monat==6:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=6)]
                )
            elif monat==7:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=7)]
                )
            elif monat==8:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=8)]
                )
            elif monat==9:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=9)]
                )
            elif monat==10:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=10)]
                )
            elif monat==11:
                self.button_list[monat]=tk.Button(
                    frame,
                    text="Ansehen",
                    command=lambda:[self.display_none(), tag_display.display_active(monat=11)]
                )
        
    def dislpay_active(self):
        #bewegt sich nicht mit und macht probleme wenn die rechte seite verändert wird
        #self.total_frame.grid(row=0, column=0, padx=400, pady=50)
        self.total_frame.pack()

    def display_none(self):
        self.total_frame.pack_forget()
    ######################## 
    # Hier gehts weiter!!! # 
    ######################## 
class display_tag:
    
    def __init__(self):
        self.frame_list=list()
        self.active_display=int()
        
        self.display_lode()
        
        
    def display_lode(self): 
        for monat in range(12):
                if len(self.frame_list)<12:
                    self.frame_list.append(None)
                monat_frame=tk.Frame(root)
                
                wochentag=quary_json_data(liste_monate=(monat, "anfangs_tag"))
                
                tag_x=0
                tag_y=0
                
                for loop_tag in range(quary_json_data(liste_monate=(monat, "anz_days"))):
                    
                    tag_frame=tk.Frame(monat_frame, border=2, relief="groove")
                    
                    name=tk.Label(tag_frame, text=quary_json_data(liste_tag_namen=wochentag))
                    datum=tk.Label(tag_frame, text=loop_tag+1)
                    
                    name.grid(column=0, row=0)
                    datum.grid(column=2, row=0)
                    
                    x=1
                    if len(quary_termine_tag(monat=monat, tag=loop_tag))>0:
                        
                        for termin in quary_termine_tag(monat=monat, tag=loop_tag):
                            
                            termin_name=tk.Label(tag_frame, text=termin.name)
                            termin_von=tk.Label(tag_frame, text=termin.von_bis[0])
                            termin_bis=tk.Label(tag_frame, text=termin.von_bis[1])
                            
                            termin_name.grid(column=0, row=x)
                            termin_von.grid(column=1, row=x)
                            termin_bis.grid(column=2, row=x)

                            x+=1
                    tag_frame.grid(column=tag_y, row=tag_x, pady=15, padx=20)
                    
                    wochentag+=1
                    if wochentag>7:
                        wochentag=1
                    tag_y+=1
                    if tag_y>6:
                        tag_y=0
                        tag_x+=1
                        
                self.frame_list[monat]=monat_frame
                
                back=tk.Button(monat_frame,text="Zurück", command=lambda:[self.display_none(), monat_display.dislpay_active()])
                back.grid(row=10, column=0)
                termin_but=tk.Button(monat_frame, text="Neuer Termin", command=lambda:[self.display_none(), termin_new.display_active()])
                termin_but.grid(row=10, column=1)
                
    def display_active(self, monat=None):
        if monat==None:
            self.frame_list[self.active_display].pack()
        else:
            self.active_display=int(monat)
            self.frame_list[monat].pack()
    
    def display_none(self): 
        self.frame_list[self.active_display].pack_forget()
        
class new_termin:
    
    def __init__(self):
        self.monat=None
        self.frame=None
        
        self.display_lode()
    
    def display_lode(self):
        self.frame=tk.Frame(root)
        
        tag_text=tk.Label(self.frame, text="Tag:")
        self.tag_entry=tk.Entry(self.frame)
        tag_text.grid(row=1, column=0)
        self.tag_entry.grid(row=1, column=1)
        
        name_text=tk.Label(self.frame, text="Name:")
        self.name_entry=tk.Entry(self.frame)
        name_text.grid(row=2, column=0)
        self.name_entry.grid(row=2, column=1)
        
        von_text=tk.Label(self.frame, text="Von:")
        self.von_entry=tk.Entry(self.frame)
        von_text.grid(row=3, column=0)
        self.von_entry.grid(row=3, column=1)
        
        bis_text=tk.Label(self.frame, text="Bis:")
        self.bis_entry=tk.Entry(self.frame)
        bis_text.grid(row=4, column=0)
        self.bis_entry.grid(row=4, column=1)
        
        info_text=tk.Label(self.frame, text="Info")
        self.info_entry=tk.Entry(self.frame)
        info_text.grid(row=5, column=0)
        self.info_entry.grid(row=5, column=1)
        
        save=tk.Button(self.frame, text="Speichern", command=lambda:self.creat_termin())
        save.grid(row=6, column=1)
        
        back=tk.Button(self.frame, text="Zurück", command=lambda:[self.display_none(), tag_display.display_active(monat=None)])
        back.grid(row=6, column=0)
    
    
    def display_active(self):
        self.frame.pack()
    
    def display_none(self):
        self.frame.pack_forget()
    
    def creat_termin(self):
        
        append_termin(
            monat=tag_display.active_display,
            tag=self.tag_entry.get(),
            name=self.name_entry.get(),
            von=self.von_entry.get(),
            bis=self.bis_entry.get(),
            text=self.info_entry.get(),
            fabe=None
        )
        
        monat_display.display_lode()
        tag_display.display_lode()
        
        self.display_none()
        tag_display.display_active(monat=None)

def anz_termine_monat(monat=int()):
    anz_termine=0
    with open("JSON/termine_data.json", "r") as data_file:
        data = json.load(data_file)
        data_monat = data.get("data")
        if data_monat.get(str(monat)) > 0:
            anz_termine=data_monat.get(str(monat))
    return anz_termine   
        
        
# such nach terminen an einem tag und gib diese in einem objeckt wieder
def quary_termine_tag(monat=int(), tag=int()):
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
        print("quary_termine_tag")
    finally:
        return termine_list
      
def quary_termine_monat(monat_int=int()):
    return_list=list()
    try:
        with open("JSON/termine_data.json", "r") as data_file:
            data = json.load(data_file)
            monat=data.get(str(monat_int))
            for key_mon in monat.keys():
                
                if len(monat.get(key_mon).keys())>0:
                    
                    for key_tag in monat.get(key_mon).keys():
                        termine=monat.get(key_mon).get(key_tag)
                        return_list.append(
                            class_termin(
                                name=termine.get("name"),
                                id=termine.get("id"),
                                von=termine.get("von"),
                                bis=termine.get("bis"),
                                text=termine.get("text"),
                                fabe=termine.get("fabe"),
                                tag=int(key_mon),
                                monat=monat_int
                            )
                        )
            z=1
            while len(return_list)<9:
                return_list.append(
                    class_termin(
                        name="xxx",
                        id=None,
                        von=None,
                        bis=None,
                        text=None,
                        fabe=None,
                        tag=z,
                        monat=None
                    )
                )
                z+=1
    except:
        print("quary_termine_monat")
    finally:
        return return_list
                    
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
        print("quary_json_data")
    finally:
        if ero != None:
            print(ero)

############################# RESETET ALLES ###############################################
def reset():
    with open("ToDO\JSON\kalender_data.json", "r") as data_file:
        main={}
        data = json.load(data_file)
        tage_monat=list()
        for x in range(12):
            tage_monat.append(int(data.get("list_monate")[x].get("anz_days")))
    
    with open("ToDO\JSON\Termine_data.json", "w") as data_file:
        for monate in range(12):
            main.update({str(monate):{}})
            for tage in range(tage_monat[monate]):
                main.get(str(monate)).update({str(tage):{}})
        json.dump(main, data_file, indent=4)

def append_termin(monat=int(), tag=int(), name=str(), von=None, bis=None, text=None, fabe=None, id=None):
    with open("JSON\Termine_data.json", "r") as data_file:
        data = json.load(data_file)
        if id == None:
            id = data.get("data").get("id") + 1
            data.get("data").pop("id")
            data.get("data").update({"id":id})
        data.get(str(monat)).get(str(tag)).update(
                    {f"{id}":{
                    "name":name,
                    "von":von,
                    "bis":bis,
                    "text":text,
                    "fabe":fabe,
                    "id":id
                    }}
                )
    with open("JSON\Termine_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

if __name__=="__main__":
    ref_jahr = class_jahr(name=quary_json_data(jahr="name"))
    gui=True
    if gui:
        root = tk.Tk()
        root.title("Kalender 2022")
        root.geometry("1920x1080")
        
        tag_display = display_tag()
        monat_display=display_monate()
        termin_new=new_termin()
        
        monat_display.dislpay_active()
        
        root.mainloop()
