@app.route('/', methods=["GET", "POST"])
def index():
    # Use session cookie to store username for entire game duration
    if "username" in session:
        # User already picked a name, redirect them to the game
        return redirect("/riddles")
    with open("data/scores.json") as scores_file:
        # Load scores file to check username against and to render hiscores
        userscores = json.load(scores_file)
    if request.method == "GET":
        return render_template("index.html", hiscores=userscores)
    if request.method == "POST":
        # Homepage shows user form which sends POST request back to itself here
        username = request.form["username"]
        if not check_username(userscores, username):
            # Username was invalid
            return render_template(
                    "index.html", 
                    username=username, 
                    error=True, 
                    hiscores=userscores)
        else:
            '''
            Username was valid, add it to the json and then write file so
            nobody else can use it
            '''
            userscores[username] = 0
            with open("data/scores.json", "w") as write_file:
                json.dump(userscores, write_file)
            # Also store username in session cookie
            session["username"] = username
            return redirect("/riddles")
    # If neither GET or POST requests brought us here, use this as fallback
    return render_template("index.html", hiscores=userscores)