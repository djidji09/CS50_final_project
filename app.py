from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configure application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        return render_template("index1.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template('buy.html')
    else:
        symbol = request.form.get("symbol").upper()
    shares = request.form.get("shares")
    if not symbol:
        return apology("Enter stock symbol!", 400)
    if not shares.isdigit():
        return apology("you can't buy shares this way", 400)
    if int(shares) < 0:
        return apology("type a positive integer", 400)

    item = lookup(symbol)
    if not item:
        return apology("Enter a valid stock symbol!", 400)

    if not item:
        return apology("Invalid stock symbol!")

    cash = db.execute("SELECT cash FROM users")
    price = usd(item["price"])
    name = item["name"]
    symbol = item["symbol"]

    if (item["price"]) * int(shares) > cash[0]["cash"]:
        return apology("YOU'RE POOR")
    else:
        db.execute("UPDATE users SET cash = cash - :price WHERE id = :id",
                   price=(item["price"] * int(shares)), id=session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], symbol, shares, price)

    return redirect('/')


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        transactions = db.execute(
            "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY timestamp DESC", user_id=session["user_id"])
        return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash('login done')
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template('quote.html')
    else:
        symbol = request.form.get("symbol").upper()
    if not symbol:
        return apology("Enter stock symbol!", 400)

    item = lookup(symbol)

    if not item:
        return apology("Invalid stock symbol!")

    price = usd(item["price"])
    name = item["name"]
    symbol = item["symbol"]

    return render_template('quoted.html', price=price, name=name, symbol=symbol)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # ensure that he typed the password
        if not request.form.get("password"):
            return apology("must provide password", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("are you an idiot", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 0:
            return apology("usename already exists", 400)

        # add username and hash to the database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get(
            "username"), generate_password_hash(request.form.get("password")))

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP by symbol HAVING total_shares > 0", user_id=session["user_id"])
    if request.method == "POST":
        symbol = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = :user_id", user_id=session["user_id"])
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("you can't buy shares this way", 400)
        if not shares.isdigit():
            return apology("you can't buy shares this way", 400)
        if int(shares) <= 0:
            return apology("type a positive integer", 400)
        for stock in stocks:
            if stock["symbol"] == symbol:
                if stock["total_shares"] < int(shares):
                    return apology("not enough shares")
                else:
                    item = lookup(symbol)
                    if not item:
                        return apology("there is no stock with this name")
                    price = item["price"]
                    total_sell = int(shares) * price
                    shares = -int(shares)
                    db.execute("UPDATE users SET cash = cash + :total_sell WHERE id = :user_id",
                               user_id=session["user_id"], total_sell=total_sell)
                    db.execute("INSERT INTO transactions (user_id,symbol,shares,price) VALUES (?,?,?,?)",
                               session["user_id"], symbol, shares, price)
                    return redirect("/")
    if request.method == "GET":
        symbol = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = :user_id", user_id=session["user_id"])
        return render_template("sell.html", symbols=symbol)
