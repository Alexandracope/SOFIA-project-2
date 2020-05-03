import pytest
from application import routes

def test_generator():
    # colour = 'Red'
    for medium in ['Watercolour Paint']:
        for shades in range(2,20):
            for colour in ['Red']:
                assert routes.generator() == (str(shades) + " shades only using the medium " + medium + " and your Subject is a " + colour + " Obj1") \
                    or routes.generator() == (str(shades) + " shades only using the medium " + medium + " and your Subject is a " + colour + " Obj2") \
                        or routes.generator() == (str(shades) + " shades only using the medium " + medium + " and your Subject is a " + colour + " Obj3") \
                            or routes.generator() == (str(shades) + " shades only using the medium " + medium + " and your Subject is a " + colour + " Obj4") \
                                or routes.generator() == (str(shades) + " shades only using the medium " + medium + " and your Subject is a " + colour + " Obj5")