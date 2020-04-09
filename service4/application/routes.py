# import request & Response function from the flask module
from flask import request, Response
import random

# import the app object from the ./application/__init__.py
from application import app

# define routes for /medium , this function will be called when these are accessed
@app.route('/generator', methods = ['GET'])
def generator():
    color = request.get('http://Service2:5001/color')
    medium = request.get('http://service3:5002/medium')

array = ["Obj1" , "Obj2" , "Obj3" , "Obj4", "Obj5", "Obj6" , "Obj7", "Obj8" , "Obj9" , "Obj10", "Obj11" , "Obj12" , "Obj13" , "Obj14" , "Obj15" , "Obj16" , "Obj17" , "Obj18" , "Obj19", "Obj20" , "Obj21", "Obj22", "Obj23", "Obj24" , "Obj25" , "Obj26" , "Obj27" , "Obj28"]

if input1 == "water colour paint":
    shades = random.randint(2,9)
    if input2 == "Red":
        subject = array[random.randrange(0,4)]
    elif input2 == "Yellow":
        subject = array[random.randrange(5,8)]
    elif input2 == "Pink":
        subject = array[random.randrange(9,12)]
    elif input2 == "Blue":
        subject = array[random.randrange(13,16)]
    elif input2 == "Orange":
        subject = array[random.randrange(17,20)]
    elif input2 == "Purple":
        subject = array[random.randrange(21,24)]
    elif input2 == "Green":
        subject = array[random.randrange(25,28)]

if input1 == "Acrylic paint":
    shades = random.randint(2,17)
    if input2 == "Red":
        subject = array[random.randrange(0,4)]
    elif input2 == "Yellow":
        subject = array[random.randrange(5,8)]
    elif input2 == "Pink":
        subject = array[random.randrange(9,12)]
    elif input2 == "Blue":
        subject = array[random.randrange(13,16)]
    elif input2 == "Orange":
        subject = array[random.randrange(17,20)]
    elif input2 == "Purple":
        subject = array[random.randrange(21,24)]
    elif input2 == "Green":
        subject = array[random.randrange(25,28)]

if input1 == "Pencil":
    shades = random.randint(2,8)
    if input2 == "Red":
        subject = array[random.randrange(0,4)]
    elif input2 == "Yellow":
        subject = array[random.randrange(5,8)]
    elif input2 == "Pink":
        subject = array[random.randrange(9,12)]
    elif input2 == "Blue":
        subject = array[random.randrange(13,16)]
    elif input2 == "Orange":
        subject = array[random.randrange(17,20)]
    elif input2 == "Purple":
        subject = array[random.randrange(21,24)]
    elif input2 == "Green":
        subject = array[random.randrange(25,28)]

if input1 == "Crayons":
    shades = random.randint(2,10)
    if input2 == "Red":
        subject = array[random.randrange(0,4)]
    elif input2 == "Yellow":
        subject = array[random.randrange(5,8)]
    elif input2 == "Pink":
        subject = array[random.randrange(9,12)]
    elif input2 == "Blue":
        subject = array[random.randrange(13,16)]
    elif input2 == "Orange":
        subject = array[random.randrange(17,20)]
    elif input2 == "Purple":
        subject = array[random.randrange(21,24)]
    elif input2 == "Green":
        subject = array[random.randrange(25,28)]

if input1 == "Coloured Pencils":
    shades = random.randint(2,10)
    if input2 == "Red":
        subject = array[random.randrange(0,4)]
    elif input2 == "Yellow":
        subject = array[random.randrange(5,8)]
    elif input2 == "Pink":
        subject = array[random.randrange(9,12)]
    elif input2 == "Blue":
        subject = array[random.randrange(13,16)]
    elif input2 == "Orange":
        subject = array[random.randrange(17,20)]
    elif input2 == "Purple":
        subject = array[random.randrange(21,24)]
    elif input2 == "Green":
        subject = array[random.randrange(25,28)]

if input1 == "Newspaper":
    shades = random.randint(2,20)
    if input2 == "Red":
        subject = array[random.randrange(0,4)]
    elif input2 == "Yellow":
        subject = array[random.randrange(5,8)]
    elif input2 == "Pink":
        subject = array[random.randrange(9,12)]
    elif input2 == "Blue":
        subject = array[random.randrange(13,16)]
    elif input2 == "Orange":
        subject = array[random.randrange(17,20)]
    elif input2 == "Purple":
        subject = array[random.randrange(21,24)]
    elif input2 == "Green":
        subject = array[random.randrange(25,28)]

print (str(shades) + " " + "shades only" + " ,your Subject is " + input2 + " " +  subject)
    return Response(color, medium, mimetype='text/plain')

