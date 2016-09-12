from flask import render_template

from app import app
from app.lib.teams import RandomGroups


@app.route("/")
@app.route("/index")
def index():
  
    groups = RandomGroups()

    return render_template("index.html", groups = groups.teamed_groups)





    



