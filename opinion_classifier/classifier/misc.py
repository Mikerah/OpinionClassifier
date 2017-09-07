import pandas
import json
import pymongo

def create_data():
    """
    Creates the dataset from the news_and_opinion.json file
    Returns a pandas dataframe
    """
    
    # Load data from json file to pandas.DataFrame
    json_list =[]
    with open('news_and_opinion.json', encoding='utf8') as file:
        for line in file:
            #line = line.replace("\\","")
            json_list.append(json.loads(line))
    dataframe = pandas.io.json.json_normalize(json_list)
    
    # Remove both id fields
    del dataframe['_id.$oid']
    del dataframe['id']
    return dataframe
    
if __name__ == '__main__':
    print(create_data())
    