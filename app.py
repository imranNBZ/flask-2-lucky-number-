from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# sample data for number facts
NUMBER_FACTS = {
    "trivia": "Did you know? This is a trivia fact about your lucky number!",
    "math": "Your lucky number has some fascinating mathematical properties.",
    "year": "Did you know? This number has a historical significance in its year.",
}



@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route('/api/get-lucky-num', methods=['POST'])
def get_lucky_num():
    # Parse the json body
    data = request.get_json()

    # Validation
    errors = {}

    name = data.get('name')
    email = data.get('email')
    year = data.get('year')
    color = data.get('color')


    # Validate name
    if not name:
        errors['name'] = "Name is required."

    # validate email
    if not email:
        errors['email'] = "Email is required."
    
    # Validate year
    if not isinstance(year, int) or year < 1900 or year > 2000:
        errors['year'] = "Year must be an integer between 1900 and 2000."


    # validate color
    if color not in ["red", "green", "orange", "blue"]:
        errors['color'] = "Color must be one of: red, green, orange, blue."

    # Return errors if any
    if errors:
        return jsonify({"errors": errors}), 400
    
    # generate lucky number and facts
    lucky_number = random.randint(1,100)
    number_facts = {
        "trivia": NUMBER_FACTS["trivia"],
        "math": NUMBER_FACTS["math"],
        "year": NUMBER_FACTS["year"],
    }

    #successful response
    return jsonify({
        "name": name,
        "lucky_number": lucky_number,
        "number_facts": number_facts,
    })
    