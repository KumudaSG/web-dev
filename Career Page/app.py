from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        'id':1,
        'title':'Data Analyst Intern',
        'location': 'Champaign, IL',
        'salary': '$16 / hour'
    },
    {
        'id': 2,
        'title':'Software Engineering Intern',
        'location': 'Champaign, IL',
        'salary': '$17 / hour'
    },
    {
        'id': 3,
        'title':'Front-End Engineer',
        'location': 'Champaign, IL',
        'salary': '$18 / hour'
    },
    {
        'id': 4,
        'title':'Software Engineer',
        'location': 'Champaign, IL',
    }
]


@app.route('/')
#passing in JOBS as an argument gives us access to it in the html
def start_of_everything():
    return render_template('home.html', jobs = JOBS)

'''When using the term 'API endpoint' or 'JSON endpoint' people mean this part, where we can access info,
not only through an html page, but also as a json output.'''

@app.route('/api/jobs')
def jobsssss():
    return jsonify(JOBS)

#setting host to this makes the website accessible to any IP address. 
if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)



