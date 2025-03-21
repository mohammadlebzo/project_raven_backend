import csv
import pathlib

from server.models.item import Item
from server.config.database import get_db

def mysql_import():
    """ Imports a csv file at path csv_name to a mysql colection
    returns: count of the documants in the new collection
    """
    print(f"--- Seeding Data >> Started ---")
    db = next(get_db())

    if db.query(Item).first() == None:
        csv_path = pathlib.Path.cwd() / "app\\SampleData\\items.csv"

        dict_list = list()
        with csv_path.open(mode="r") as csv_reader:
            csv_reader = csv.reader(csv_reader)
            for rows in csv_reader:
                dict_list.append({'id':rows[0], 'title':rows[1], 'description':rows[2], 'price':rows[3], 'location':rows[4]})


        for item in dict_list[1:]:
            db_user = Item(
                id= int(item['id']),
                title= item['title'],
                description= item['description'],
                price= float(item['price']),
                location= item['location']
            )
            db.add(db_user)
        db.commit()
        print("--- Seeding Data >> Finished ---")
    else:
        print("--- Seeding Data >> Abort [Items are already available] ---")
    
    return True
    