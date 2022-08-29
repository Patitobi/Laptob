import json
#import termine.py as T

class class_jahr:
    def __init__(self, name):
        self.name=name
        self.ref_monate=list()
        i=0
        while i < 12:
            self.ref_monate.append(
            class_monat(
                    name=quary_json_data(list_monate=(i, "name")),
                    stelle=i,
                    tagesraum=quary_json_data(list_monate=(i, "tageszeitraum")),
                    anz_tage=quary_json_data(list_monate=(i, "anz_days")),
                    ref_jahr=self
                )
            )
            i+=1
             
class class_monat:
    def __init__(self, name=str(), stelle=int(), tagesraum=list(), anz_tage=int(), ref_jahr=object()):
        self.ref_jahr=ref_jahr
        self.name=name
        self.stelle=stelle
        self.anz_tage=anz_tage
        self.tagesraum=tagesraum
        self.ref_tage=list()
        
        i=0
        while i < self.anz_tage:
            if i == 0:
                tag_name=int(quary_json_data(list_monate=(i, "anfangs_tag")))
            else:
                tag_name+=1
                if tag_name>7:
                    tag_name=1
            self.ref_tage.append(
                class_tag(
                    stelle=i,
                    name=quary_json_data(liste_tag_namen=tag_name),
                    jahrestag=self.tagesraum[0] + i,
                )
            )
            i+=1
        
class class_tag:
    def __init__(self, stelle=int(), name=str(), jahrestag=int()):
        self.stelle = stelle
        self.name=name
        self.jahrestag=jahrestag
        self.termin_anzahl=None
        
        

class class_termin:
    def __init__(self):
        pass
    
def quary_termine():
    try:
        with open("JSON/kalender_data.json", "r") as data_file:
            data = json.load(data_file)
            for monat in range(12): 
                for_monat = data.get(monat)
                for tag in range(quary_json_data(list_monate=(monat, "anz_days"))):
                    for_monat.get(tag)
    except:
        pass
    finally:
        pass
    
    
    
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
        print("ToDO\JSON\termine_data.json kommte nicht geöfnet werden")
    finally:
        if ero != None:
            print(ero)

if __name__=="__main__":
    ref_jahr = class_jahr(name=quary_json_data(jahr="name"))
    #T.append_termin(3, 8, "Termin", von="0800", bis="1600", text="Das ist ein Termin")
    
    quary_termine()