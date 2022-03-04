from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret" 
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()

@app.route("/")
def show_home_page():
    """ Homepage Listing Pets """

    pets  = Pet.query.all()
    return render_template("/home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """ Add a pet and Handle form submission for new pets """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        # reshow form for editing
        return render_template("/add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    " Display and Edit info about specfic pet "

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect("/")
    
    else:
        return render_template("/edit_pet.html", pet=pet, form=form)