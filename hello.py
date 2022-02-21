from flask import Flask, render_template


#create a Flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')
#def index():
#    return "<h1>mbolo'ani!</h1>"
def index():
    mori_name="wzw"
    gbo="°ky"
    chop=["nyembwe","odika","mayarra"]
    ink=["ink nh.h.","ink nb pt","ink nd r d_r""ink nt_r °3",
        "ink pth_","ink nt_r w°","w°","ink nb nh.h.","ink nh.h."]
    return render_template("index.html",
        mori_name=mori_name,
        gbo=gbo,
        chop=chop,
        ink=ink)
    
#localhost:5000/user/name    
@app.route('/user/<name>')    
def user(name):
    return render_template("user.html",name=name)
    
#Create error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404
#Create internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500