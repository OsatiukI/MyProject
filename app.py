from flask import Flask, render_template, request
from game import player, shop, weapons, armor, quest

app = Flask(__name__)

player1 = player()
player1.name = "Герой"


@app.route("/")
def index():
    return render_template("index.html", player=player1, shop=shop)


@app.route("/buy", methods=["POST"])
def buy():
    item = request.form.get("item")

    if item:
        player1.buy_item(item, shop)

    return render_template("index.html", player=player1, shop=shop)


@app.route("/sell", methods=["POST"])
def sell():
    item = request.form.get("item")

    if item:
        player1.sell_item(item, shop)

    return render_template("index.html", player=player1, shop=shop)


@app.route("/use", methods=["POST"])
def use():
    item = request.form.get("item")

    if item:
        player1.use_item(item, weapons, armor)

    return render_template("index.html", player=player1, shop=shop)


@app.route("/quest", methods=["POST"])
def quest_route():
    result = quest(player1)

    return render_template(
        "index.html",
        player=player1,
        shop=shop,
        quest_result=result
    )


if __name__ == "__main__":
    app.run(debug=True)