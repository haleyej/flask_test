from app import app 

# view functions mapped to 1+ URLS
# Flask knows what to execute when the client requests a URL


# A decorator modifies the function that follows it 
# Creates an association between the URLS and the function
@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'