from flask import Flask
from person.models import Person, Address, session

app = Flask(__name__)

@app.route("/")
def hello():
    return "I will show my model here"

@app.route("/new")
def new_person():
    # Insert a Person in the person table
    new_person = Person(name='new person')
    session.add(new_person)
    session.commit()

    # Insert an Address in the address table
    new_address = Address(post_code='00000', person=new_person)
    session.add(new_address)
    session.commit()

    return "They are saved"

@app.route("/person")
def show_person():
    person = session.query(Person).first()
    print(person)
    return str(person)


if __name__ == "__main__":
    app.run(debug=True)
