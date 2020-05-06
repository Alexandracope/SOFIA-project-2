import pytest
from application import routes
 
def test_colour():
    assert routes.colour() == 'Red' or routes.colour() == 'Yellow' or routes.colour() == 'Pink' or routes.colour() == 'Blue' or routes.colour() ==  'Orange' or routes.colour() == 'Purple' or routes.colour() == 'Green'