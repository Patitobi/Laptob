import json


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
    with open("ToDO\JSON\Termine_data.json", "r") as data_file:
        data = json.load(data_file)
        if id == None:
            id = data.get("data").get("id") + 1
            data.get("data").pop("id")
            data.get("data").update({"id":id})
        data.get(str(monat)).get(str(tag)).update(
                    {{
                    "name":name,
                    "von":von,
                    "bis":bis,
                    "text":text,
                    "fabe":fabe,
                    "id":id
                    }}
                )
    with open("ToDO\JSON\Termine_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)


if __name__ == "__main__":
    append_termin(1, 8, "Termin", von="0800", bis="1600", text="Das ist ein Termin")
    append_termin(7, 9, "Termin", von="0800", bis="1600", text="Das ist ein Termin")
