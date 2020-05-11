from pymongo import MongoClient

client = MongoClient("mongodb://localhost/unanuevanormalidad")
db = client.get_database()


def query(zipcode):
    q = list((db["data"].find({"$and": [{"CP": zipcode[:2]}, {"Excepcion": False}]})))

    # Provinces without exceptions
    if len(q) > 0:
        fase = q[0]["Fase"]
        territory = q[0]["Provincia"]
        return fase, territory

    # Provinces with exceptions
    else:
        q2 = list((db["data"].find({"$and": [{"CP": zipcode[:2]}, {"Excepcion": {"$ne": False}}]},
                                {"Excepcion":1, "_id":0})))

        if q2[0]["Excepcion"].get(zipcode) != None:
                fase = q2[0]["Excepcion"][zipcode]["Fase"]
                territory = q2[0]["Excepcion"][zipcode]["Territorio"]
                return fase, territory
        else:
            q3 = list((db["data"].find({"CP": zipcode[:2]})))
            fase = "0"
            territory = q3[0]["Provincia"]
            return fase, territory
    