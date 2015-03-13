from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/', methods = ['POST','GET'])
def hello_world():

    # variables for template page (templates/index.html)
    author = "Kyle"
    readval = 10

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        # if we press the turn on button
        if request.form['submit'] == 'Turn On': 
            print 'TURN ON'
            
        # if we press the turn off button
        elif request.form['submit'] == 'Turn Off': 
            print 'TURN OFF'

        else:
            pass
    
    # the default page to display will be our template with our template variables
    return render_template('index.html', author=author, value=100*(readval/1023.))


if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')
