import pandas

data = pandas.read_csv("eglenfonetik.csv")

phonetic_dictionary = {row.Harf:row.Kelime for (index,row) in data.iterrows()}

user_word = input("Yeni Türkiye Yüzyılı Fonetik kodlaması için kelime girin: ").upper()
output_list = [phonetic_dictionary[letter] for letter in user_word]

print(output_list)