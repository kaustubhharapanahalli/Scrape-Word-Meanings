import csv
import json
import random

all_words = []

with open("All_words.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        all_words.extend(row)
print(len(all_words))

with open("data_corrected.json", "r") as outfile:
    dict_words = json.load(outfile)

for group, _ in dict_words.items():
    for word, _ in dict_words[group].items():
        gre_syns = []
        for syn_word in dict_words[group][word]["synonyms"]:
            if syn_word in all_words:
                dict_words[group][word]["synonyms"].remove(syn_word)
                gre_syns.append(syn_word)
        dict_words[group][word]["gre_synonyms"] = gre_syns
        try:
            for example_sen in dict_words[group][word]["example_sentences"]:
                sample_size = (
                    3
                    if len(dict_words[group][word]["example_sentences"]) > 3
                    else len(dict_words[group][word]["example_sentences"])
                )

                dict_words[group][word]["example_sentences"] = random.sample(
                    dict_words[group][word]["example_sentences"], sample_size
                )
        except Exception:
            pass


with open("data_corrected_with_gre_syns.json", "w") as outfile:
    json.dump(dict_words, outfile)
