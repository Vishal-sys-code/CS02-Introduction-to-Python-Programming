def function_without_KW_arguments(first_name, last_name):
    print("Hello " + first_name + " " + last_name)

print(function_without_KW_arguments(first_name = "Jack", last_name = "Williams"))
# print(hello(first_name = "Opera", middle_name = "Henry", last_name = "Kushgoterava"))

#------------------------------------------------------------------------------------------------------------------#

"""
The following above code-snippet has given an error:
TypeError: hello() got an unexpected keyword argument 'middle_name'

So, this can be fixed throught the positional arguments, and this would be done by the kwargs.
kwargs are being packed in the dictionary.
"""

def  function_with_KW_arguments(**kwargs):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello ")
    for key,value in kwargs.items():
        print("Hola " + value)
function_with_KW_arguments(first_name = "Jack", last_name = "Williams")
function_with_KW_arguments(first_name = "Opera", middle_name = "Henry", last_name = "Kushgoterava")

#------------------------------------------------------------------------------------------------------------------#

"""
We can change the name of the *args to anything like your name too.
It can be *jack, *annie or anything.
"""

def  function_with_KW_arguments_name_changing(**annie):
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello ")
    for key,value in annie.items():
        print("Hola " + value)
function_with_KW_arguments_name_changing(first_name = "Jack", last_name = "Williams")
function_with_KW_arguments_name_changing(first_name = "Opera", middle_name = "Henry", last_name = "Kushgoterava")