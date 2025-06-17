try:
  file = open("myfile.txt","r")
except IOError:
  print("Error: Unable to read the file!")
finally:
  file.close()
