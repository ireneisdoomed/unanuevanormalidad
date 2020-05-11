from pymongo import MongoClient

client = MongoClient("mongodb://localhost/unanuevanormalidad")
db = client.get_database()

def query(zipcode):
    q = list((db["data"].find({"$and": [{"CP": zipcode[:2]}, {"Excepcion": False}]})))

    if len(q) > 0:
        result = q[0]["Fase"]
        print(result)
        return result
    else:
        q2 = list((db["data"].find({"$and": [{"CP": zipcode[:2]}, {"Excepcion": {"$ne": False}}]},
                            {"Excepcion":1, "_id":0})))
        if len(q2) == 0:
            result = "0"
            print(result)
            return result
        else:
            result = q2[0]["Excepcion"][zipcode]["Fase"]
            print(result)
            return result

