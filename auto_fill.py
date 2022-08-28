import json

main={}

for x in range(12):
    main.update({str(x):{
                        ""
                        }
                 }
                )

with open("ToDO\JSON\termine_data.json", "w") as data_file:
    pass