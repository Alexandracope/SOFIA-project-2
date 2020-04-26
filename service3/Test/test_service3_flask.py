import pytest
from application import routes
 
def test_medium():
    assert routes.medium() == 'Pencil' or routes.medium() == 'Acrylic Paint' or routes.medium() == 'Watercolour Paint' or routes.medium() == 'Crayons' or routes.medium() ==  'Coloured Pencils' or routes.colour() == 'Newspaper'
    