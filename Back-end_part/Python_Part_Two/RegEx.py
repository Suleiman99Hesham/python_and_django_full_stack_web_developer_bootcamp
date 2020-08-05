
# this file has a punch of examples on RegEx which i wrote,
#  i seperate them by '=' sign 
# so run every example individually, simply uncomment it and run 


import re
#===========================================================
# patterns = ['term1', 'term2']

# text = 'This is a string with term1, not not the other!'

# for pattern in patterns:
#     print("I'm searching for: "+pattern)

#     if re.search(pattern, text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")

# match = re.search('term1',text)

# print(type(match))

# print(match.start())

#============================================================

# split_term = '@'

# email = 'suleimanhesham99@gmail.com'

# print(re.split(split_term,email))

#============================================================

# print(re.findall('match', 'test phrase match in match middle'))

#============================================================

# def multi_re_find(patterns,phrase):
#     '''
#     find all occurencs of every pattern in some phrase 
#     and print them 
#     '''
#     for pat in patterns:
#         print("searching for pattern {}: ".format(pat))
#         print(re.findall(pat, phrase))
#         print('\n')
    
# use one of them (test_phrase,test_patterns) , not all in one time

# test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
# test_patterns = ['sd', 'sd*', 'sd+', 's[sd]+', 'sd{3}', 'sd{1,3}']

# test_phrase = 'This is a string! But is has punctuation. How can we remove it?'
# test_patterns = ['[^!.?]+', '[a-z]+', '[A-Z]+']

# test_phrase = 'This is a string with numbers 12312 and a symbol #hashing'
# test_patterns = [r'\w+', r'\W+', r'\d+', r'\D+', r'\s+', r'\S+']

# multi_re_find(test_patterns,test_phrase)