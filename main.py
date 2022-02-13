import pandas
df=pandas.read_csv("nato_phonetic_alphabet.csv")
dict={row.letter:row.code for (index, row) in df.iterrows()}
print(dict)
word=input("enter a word").upper()
op=[dict[letter] for letter in word]
print(op)