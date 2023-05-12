from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "kevin"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_form():
    """Create form for the prompts"""
    
    prompts = story.prompts
    return render_template('home.html', prompts = prompts)


@app.route('/madlib')
def create_story():
    """Generate story on page"""
    
    text = story.generate(request.args)
    return render_template('madlib.html', text = text)