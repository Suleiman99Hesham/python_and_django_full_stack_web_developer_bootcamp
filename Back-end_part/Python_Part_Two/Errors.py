try:
    f = open("simple_text",'w')
    f.write("text write to simple text")    
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
# else:
#     print("SUCCESS!")
#     f.close()
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")