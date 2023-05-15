# app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

# menu = [{"name": 'Downald', 'url': 'install'},
#         {'name': "Contact", "url": "contact"},
#         {'name': 'About me', 'url': 'about-me'}]
# @app.route("/")
# def about():
#     print(url_for("about"))
#     return render_template("about.html", title="About Flask", menu=menu)


# @app.route("/index/")
# def index ():
#     print(url_for("index"))
#     return render_template("index.html", title="About Flask", menu=menu)

# @app.route("/contact/", methods=["POST", "GET"])
# def contact():
#     if request.method == 'POST':
#         if len(request.form["username"]) > 2:
#             flash("Message was send", category="success")
#         else:
#             flash("Error in cause of  the send", category="error")
        
#     return render_template("contact.html", title="Contact", menu=menu)


# @app.route("/profile/<username>")
# def profile(username):
#     if "UserLogged" not in session or session["UserLogged"]!= username:
#         abort(401)
#     return f"Hello {username}"

# @app.route("/login", methods=["POST", 'GET'])
# def login():
#     if 'UserLogged' in session:
#         return redirect(url_for("profile", username=session["UserLogged"]))
#     elif request.method=="POST" and request.form["username"] == "selfedu" \
#         and request.form['psw'] == "123":
#         session['UserLogged'] = request.form["username"]
    
#     return render_template("login.html", title = "Autorization", menu=menu)



# @app.errorhandler(404)
# def page_not_fond(error):
#     return render_template("page404.html", title="Page not found", menu=menu)


# @app.route("/general")
# def ind():
#     return "<h1>Main Page</h1>"
#
#
# @app.route("/session")
# def sess():
#     if 'visits' in session:
#         session['visits'] = session.get('visits') + 1  # обновление данных сессии
#     else:
#         session['visits'] = 1  # запись данных в сессию
#
#     return f"<h1>Main Page</h1>Число просмотров: {session['visits']}"
#
#
# data = [1, 2, 3, 4]
#
#
# @app.route("/ses")
# def session_data():
#     if 'data' not in session:
#         session.permanent = True
#         session['data'] = data
#     else:
#         session['data'][1] += 1
#         session.modified = True
#
#     return f"session['data']: {session['data']}"
#
#
# @app.route("/login")
# def login():
#     log = ""
#     if request.cookies.get('logged'):
#         log = request.cookies.get('logged')
#
#     res = make_response(f"<h1>Форма авторизации</h1>logged: {log}")
#     res.set_cookie("logged", "yes", 30 * 24 * 3600)
#     return res
#
#
# @app.route("/logout")
# def logout():
#     res = make_response("Вы больше не авторизованы!</p>")
#     res.set_cookie("logged", "", 0)
#     return res