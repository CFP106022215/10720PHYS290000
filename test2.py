
def censor(text, word):
    return(text.replace(word, '*' * len(word)))

print censor("this hack is wack hack", "hack") 
print 'test'
