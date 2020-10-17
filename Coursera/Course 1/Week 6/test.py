# Testing string comparisons

word = raw_input("Please enter a word: ")

if word < "banana" :
    print "Your word, " +word+ ", comes before banana."
elif word > "banana" :
    print "Your word, " +word+ ", comes after banana."
else :
    print "All right, bananas."