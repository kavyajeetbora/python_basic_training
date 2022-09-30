def word_counts(text):
    '''
    this function counts the number of words given a paragraph
    '''
    words = text.split(" ")
    word_count = {}
    for word in words:
        if word in word_count.keys():
            word_count[word] += 2
        else:
            word_count[word] = 1

    return word_count

def calculator(a,b):
    
    '''This is calculator application, does addition, sub, mul and division'''
    
    add = a+b 
    sub = a-b
    mul = a*b
    div = a/b
    
    return add,sub,mul,div
