import pymongo
import os
from dotenv import load_dotenv
from pdfText import pdfExtractor

load_dotenv()

client = pymongo.MongoClient('mongodb+srv://' + os.getenv('MONGODBIDENTIFICATION') + '.vtqujxr.mongodb.net/TurnerFentonDECA?retryWrites=true&w=majority')
db = client['TurnerFentonDECA']
collection = db[('marketingquestions'.lower())]

pdfReader = pdfExtractor("./2011.pdf")

print("starting ...")

for i in range(100):
    print(i)
    pdfReader.questions[i] = pdfReader.questions[i].replace("\n", "")
    document = {
        "Question" : pdfReader.questions[i],
        "OptionOne": pdfReader.optionOnes[i],
        "OptionTwo": pdfReader.optionTwos[i],
        "OptionThree": pdfReader.optionThrees[i],
        "OptionFour": pdfReader.optionFours[i],
        "Answer": pdfReader.answers[i]
        }

    query = {"Question": pdfReader.questions[i]}
    result = collection.find_one(query)
    if not result:
        collection.insert_one(document)

print("done")
