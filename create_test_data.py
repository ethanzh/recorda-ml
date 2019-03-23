import pandas as pd
import csv
import random
# this script will use the places, things, and sentence structures to generate structured test data to train the entity extraction model

# make everything lower case to start with, there will be some randomization with case to account for potential inconsistencies in the speech to text recognition

def sentence_from_pattern(pattern, thing, place, rating):
    string = pattern.replace("THING", thing).replace("PLACE", place).replace("RATING", rating)
    return ' '.join(string.split())

things = list(pd.read_csv("things.csv")["things"])
places = list(pd.read_csv("places.csv")["places"])

# not going to worry about these now, Google NLP will handle sentiment
ratings = [
        "bad",
        "good",
        "tasty",
        "delicious",
        "terrible",
        "decent",
        "okay",
        "acceptable",
        "not that bad",
        "not that good",
        "could have been better",
        "sucked",
        "was bomb"]

patterns = [
        "the THING I had at PLACE was RATING",
        "PLACE THING RATING",
        "THING PLACE RATING",
        "RATING THING PLACE",
        "my THING at PLACE was RATING",
        "I thought the THING at PLACE was RATING",
        "the THING at PLACE is RATING",
        "PLACE's THING is RATING"
        ]
with open("train_data.csv", mode='w') as csv_file:
    field_names = ["phrase", "thing", "t_s", "t_e", "place", "p_s", "p_e", "rating"]
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for i in range(5000):
        pa = str(random.choice(patterns))
        t = str(random.choice(things))
        pl = str(random.choice(places))
        r = str(random.choice(ratings))
        phrase = str(sentence_from_pattern(pa, t, pl, r))
        # general form, use 'find' to get start index, add len+1 for end
        t_s = phrase.find(t)
        t_e = t_s + len(t) + 1
        p_s = phrase.find(pl)
        p_e = p_s + len(pl) + 1
        writer.writerow({
            "phrase": phrase,
            "thing": t,
            "t_s": t_s,
            "t_e": t_e, 
            "place": pl,
            "p_s": p_s,
            "p_e": p_e,
            "rating": r 
            })
