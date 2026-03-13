from bson.objectid import ObjectId
import pymongo

client = pymongo.MongoClient("localhost:27017")
db = client["BDC_bank_recon"]
list_collections = db.list_collections()



def get_collections_pb(): 
    list_collection = list(db.list_collection_names(0))
    final_list= {}
    account_list= [] 
    
    for x in list_collection:
        if "_pb_" in x:
            data = db[x].find_one()
            account = data.get("account_number","None")
            account_list.append(f'{account}')

    for account in account_list:
        final_list[account] = []

    for x in list_collection:
        if "_pb_" in x:
            final_list[account].append(x)

    for k,v in final_list.items():
        if v:
            for z in v:
                print(z,k)
    return(final_list)

def get_collections_gl(): 
    list_collection = list(db.list_collection_names(0))
    final_list= {}
    account_list= [] 
    
    for x in list_collection:
        if "_gl_" in x:
            data = db[x].find_one()
            account = data.get("account_number","None")
            account_list.append(f'{account}')

    for account in account_list:
        final_list[account] = []

    for x in list_collection:
        if "_pb_" in x:
            final_list[account].append(x)
    
    return(final_list)
get_collections_pb()
