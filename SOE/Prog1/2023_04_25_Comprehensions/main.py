names = input("Give me names with comma separated: ")
names = [ name.strip().title() for name in names.split(',') ]

names_starting_with_vowel = [ name for name in names if name[0] in 'EUIOA' ]
print(names_starting_with_vowel)

#names_starting_with_vowel = []
#for name in names:
#    if name[0] in 'EUIOA':
#        names_starting_with_vowel.append(names)



