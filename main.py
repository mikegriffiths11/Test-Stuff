# import pymongo

# print(bool("Hello"))
# print(bool(15))

# current_year = 1985
# current_year_message = "hello"

# print(f'{current_year_message}{current_year}')

# print("this %s that %s" % (current_year_message, current_year))

# print(current_year_message,str(current_year))

# last_name = "Griffiths"
# first_name = "Michael"

# print (last_name+first_name)

# varOne = "Greetings,"

# varTwo = "Camel Case is the coolest"

# varThree = 1000

# # This next code will do 

# varFour = 2000

# print(varOne, varTwo)
# print("1st number:", varThree, "2nd number:", varFour)

# varOne = varTwo + "."

# varTwo = "Wow a Variable to change a variable!"

# varThree = varThree + varFour

# varFour = varThree - varFour
# print()
# print(varOne, varTwo)
# print("1st number:", varThree, "2nd number:", varFour)
# # print("hello ",2," yes")
# # print("hello"+1)


# # test_string = "hello class"

# # second=test_string.capitalize()

# # print (second)








# mystring = "hello    "
# you = "You"
# print (mystring, you)


# # my_upper_string = (mystring.upper())

# # print (my_upper_string, "you")

# my_stripped_string = mystring.strip()

# print(my_stripped_string,you)




# # print (my_upper_and_stripped_string, "you")

# my_csv_row = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,z,y,z"

# my_list = my_csv_row.split(",")

# print (my_list)

# another_list = [1,2,True,"Dog's"]








# print (another_list[3])

# x = 2





# print (another_list[x])

# y = 0

# another_list[y] = "Now!"

# # print (another_list)







# # mylist3 = [1,2,3,4,True]

# var1 = 2

# mylist3[var1] = "great"

# print (mylist3)

# mylist3[1] = ["a","b","c"]

# print (mylist3)

# print (mylist3[1][2])
# var2 = 3
# var3 = 4


# if var2 = 1:
#   var5=7
#   var6=var2+var3
# else:
#   var5=50



# if var2=1:
#   var5=99

# mikeobey=20
# honorsparents = False

# if mikeobey > 10:
#   honorsparents = True

# # This is how to test a boolean

# if honorsparents:
#   yearsinland=120

# mystring1 = 1
# mystring2 = 2

# if mystring1 == mystring2:
#   print("Yes")
# elif mystring1 > 4:
#   var5=6
# else:
#   print ("No")


import time
#allows for the pause later, see line 14

days = 7
hours = 0
minutes = 0
#setting time. can edit days to make shorter or longer

while days >= 0:
  while hours >= 0:
    while minutes >= 0:
      print(days,":",hours,":",minutes)
      #prints current timer
      time.sleep(0.01)
      #lengthen this to 1 for an accurate clock time
      minutes -= 1
      if minutes == -1:
        minutes = 59
        #rolls minutes back around
        hours -= 1
        if hours == -1:
          hours = 23
          #rolls hours back around
          days -= 1
          if days == -1:
            break
    if days == -1:
      break
  if days == -1:
    break
    #these if-days roll back the days in case they get wonky
print("Done!")
#completion marker




















































amifromengland = False








