from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template('home.html', title='Welcome to da spy place "Cue James Bond Music"')

@app.route('/gadgets')
def gadgets():  
    gadgets = ["hidden camera", "night vision scope", "binoculars"]
    return render_template('gadgets.html', title='Gadgets', subtitle="Bring them to da mission", gadgets=gadgets)

@app.route('/missions')
def missions():  
    missions = ["Mission in Russia", "Mission in North Korea"]
    return render_template('missions.html', title='Missions', subtitle="Choose one of da missions", missions=missions)

if __name__ == '__main__':
    app.run(debug=True)