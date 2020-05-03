# import request & Response function from the flask module
import random
import requests

# import the app object from the ./application/__init__.py
from application import app

# define routes for /medium , this function will be called when these are accessed
@app.route('/generator', methods = ['GET','POST'])
def generator():
    # colour_response = requests.get('http://service2:5001/colour')
    # medium_response = requests.get('http://service3:5002/medium')
    # colour = colour_response.text
    colour = 'Yellow'
    # medium = medium_response.text
    medium = 'Watercolour Paint'


    array = ["Obj1" , "Obj2" , "Obj3" , "Obj4", "Obj5", "Obj6" , "Obj7", "Obj8" , "Obj9" , "Obj10", "Obj11" , "Obj12" , "Obj13" , "Obj14" , "Obj15" , "Obj16" , "Obj17" , "Obj18" , "Obj19", "Obj20" , "Obj21", "Obj22", "Obj23", "Obj24" , "Obj25" , "Obj26" , "Obj27" , "Obj28"]
    shades = 0

    if medium == "Watercolour Paint":
        shades = random.randint(2,20)
        if colour == "Red":
            subject = array[random.randrange(0,4)]
        elif colour == "Yellow":
            subject = array[random.randrange(5,8)]
        elif colour == "Pink":
            subject = array[random.randrange(9,12)]
        elif colour == "Blue":
            subject = array[random.randrange(13,16)]
        elif colour == "Orange":
            subject = array[random.randrange(17,20)]
        elif colour == "Purple":
            subject = array[random.randrange(21,24)]
        elif colour == "Green":
            subject = array[random.randrange(25,28)]

    if medium == "Acrylic Paint":
        shades = random.randint(2,20)
        if colour == "Red":
            subject = array[random.randrange(0,4)]
        elif colour == "Yellow":
            subject = array[random.randrange(5,8)]
        elif colour == "Pink":
            subject = array[random.randrange(9,12)]
        elif colour == "Blue":
            subject = array[random.randrange(13,16)]
        elif colour == "Orange":
            subject = array[random.randrange(17,20)]
        elif colour == "Purple":
            subject = array[random.randrange(21,24)]
        elif colour == "Green":
            subject = array[random.randrange(25,28)]

    if medium == "Pencil":
        shades = random.randint(2,20)
        if colour == "Red":
            subject = array[random.randrange(0,4)]
        elif colour == "Yellow":
            subject = array[random.randrange(5,8)]
        elif colour == "Pink":
            subject = array[random.randrange(9,12)]
        elif colour == "Blue":
            subject = array[random.randrange(13,16)]
        elif colour == "Orange":
            subject = array[random.randrange(17,20)]
        elif colour == "Purple":
            subject = array[random.randrange(21,24)]
        elif colour == "Green":
            subject = array[random.randrange(25,28)]

    if medium == "Crayons":
        shades = random.randint(2,20)
        if colour == "Red":
            subject = array[random.randrange(0,4)]
        elif colour == "Yellow":
            subject = array[random.randrange(5,8)]
        elif colour == "Pink":
            subject = array[random.randrange(9,12)]
        elif colour == "Blue":
            subject = array[random.randrange(13,16)]
        elif colour == "Orange":
            subject = array[random.randrange(17,20)]
        elif colour == "Purple":
            subject = array[random.randrange(21,24)]
        elif colour == "Green":
            subject = array[random.randrange(25,28)]

    if medium == "Coloured Pencils":
        shades = random.randint(2,20)
        if colour == "Red":
            subject = array[random.randrange(0,4)]
        elif colour == "Yellow":
            subject = array[random.randrange(5,8)]
        elif colour == "Pink":
            subject = array[random.randrange(9,12)]
        elif colour == "Blue":
            subject = array[random.randrange(13,16)]
        elif colour == "Orange":
            subject = array[random.randrange(17,20)]
        elif colour == "Purple":
            subject = array[random.randrange(21,24)]
        elif colour == "Green":
            subject = array[random.randrange(25,28)]

    if medium == "Newspaper":
        shades = random.randint(2,20)
        if colour == "Red":
            subject = array[random.randrange(0,4)]
        elif colour == "Yellow":
            subject = array[random.randrange(5,8)]
        elif colour == "Pink":
            subject = array[random.randrange(9,12)]
        elif colour == "Blue":
            subject = array[random.randrange(13,16)]
        elif colour == "Orange":
            subject = array[random.randrange(17,20)]
        elif colour == "Purple":
            subject = array[random.randrange(21,24)]
        elif colour == "Green":
            subject = array[random.randrange(25,28)]

    return (str(shades) + " " + "shades only" + " using the medium " + medium + " and your Subject is a " + colour + " " +  subject)
    
