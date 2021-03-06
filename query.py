"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.filter_by(id=8).first() #Returns an object

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all(); # Returns a list of objects

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all() #Returns a list of objects

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all() #Returns a list of objects

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like("Cor%")).all() #Returns a list of objects

# Get all brands with that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all() #Returns a list of objects

# Get all brands with that are either discontinued or founded before 1950.

Brand.query.filter(db.or_(Brand.discontinued != None, Brand.founded < 1950)).all() #Returns a list of objects

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').all() #Returns a list of objects

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand, Model.brand_name==Brand.name).filter(Model.year == year).all()
    
    for name, brand, headquarters in models:
    	print "Model: %s  Brand: %s  Headquarters: %s" % (name, brand, headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = db.session.query(Brand.name, Model.name).outerjoin(Model,Model.brand_name==Brand.name).order_by(Brand.name).all()
    
    for brand, model in brands:
		print "Brand name: %s  Model: %r" % (brand, model)


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    
    search = db.session.query(Brand).filter(Brand.name.like('%'+mystr'%')).all()

    return search


def get_models_between(start_year, end_year):

	models = db.session.query(Model).filter(
		((Model.year == start_year) | (Model.year > start_year)) &
		((Model.year == end_year) | (Model.year < end_year))
		).all()
	    
    return models

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
## This query returns a BaseQuery object rather than the list of objects that match that query.
## Without .all() at the end, the object that is returned is like a question "package" rather than the answer.
## This is returned: <flask_sqlalchemy.BaseQuery object at 0x103c84dd0>

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
## An association table manages tables that have a many-to-many relationship. 
## Since tables can only be related as one-to-many (or one-to-one in rare cases),
## the association table only holds the primary keys of the tables it is connecting as foreign keys.



