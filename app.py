import random
from flask import Flask, render_template, request, redirect
from game import player, shop, weapons, armor, quest, monsters, monsters_data, quests

app = Flask(__name__)

player1 = player()
player1.name = "Герой"

current_monster = None
monster_health = None
attack_result = None
battle_finished = False
current_quest = None

@app.route("/")
@app.route("/")
def index():
    return render_template(
        "index.html",
        player=player1,
        shop=shop,
        weapons=weapons,
        current_monster=current_monster,
        monsters_data=monsters_data,
        monster_health=monster_health,
        attack_result=attack_result,
        battle_finished=battle_finished,
        current_quest=current_quest,
    )


@app.route("/sell", methods=["POST"])
def sell():
    item = request.form.get("item")

    if item:
        player1.sell_item(item, shop)

    return render_template(
        "index.html",
        player=player1,
        shop=shop,
        weapons=weapons,
        current_monster=current_monster,
        monsters_data=monsters_data,
        monster_health=monster_health,
        attack_result=attack_result,
        battle_finished=battle_finished
    )


@app.route("/use", methods=["POST"])
def use():
    item = request.form.get("item")

    if item:
        player1.use_item(item, weapons, armor)

    return render_template(
        "index.html",
        player=player1,
        shop=shop,
        weapons=weapons,
        current_monster=current_monster,
        monsters_data=monsters_data,
        monster_health=monster_health,
        attack_result=attack_result,
        battle_finished=battle_finished
    )

@app.route("/blacksmith", methods=["POST"])
def blacksmith_route():
    global attack_result

    if player1.weapon is None:
        attack_result = "У вас нет экипированного оружия."
        return redirect("/")

    weapon = player1.weapon

    durability = weapons[weapon]["durability"]

    if durability >= 100:
        attack_result = "Оружие уже полностью исправно."
        return redirect("/")

    repair_price = round((100 - durability) * 0.3)

    if player1.gold < repair_price:
        attack_result = (
            f"Недостаточно золота! "
            f"Ремонт стоит {repair_price} золота."
        )
        return redirect("/")

    player1.gold -= repair_price
    weapons[weapon]["durability"] = 100

    attack_result = (
        f"Оружие {weapon} отремонтировано! "
        f"Потрачено золота: {repair_price}."
    )

    return redirect("/")

@app.route("/quest", methods=["POST"])
def quest_route():
    global current_quest
    global current_monster
    global monster_health
    global battle_finished
    global attack_result

    current_quest = random.choice(quests[player1.level])

    current_monster = random.choice(current_quest["monster"])
    monster_health = monsters_data[current_monster]["health"]

    battle_finished = False
    attack_result = None

    return redirect("/")


@app.route("/attack", methods=["POST"])
def attack():
    global monster_health
    global attack_result
    global battle_finished

    if monster_health is None:
        return redirect("/")

    if battle_finished:
        return redirect("/")

    # Проверяем, не сломано ли оружие
    if player1.weapon is not None:
        if weapons[player1.weapon]["durability"] <= 0:
            attack_result = (
                f"Оружие {player1.weapon} сломано! "
                f"Отнесите его к кузнецу на ремонт."
            )
            return redirect("/")

    # Атака игрока
    if player1.weapon is None:
        damage = 5
        monster_health -= damage

        attack_result = (
            f"Вы нанесли {damage} урона!"
        )

    else:
        miss_chance = weapons[player1.weapon]["miss_chance"]

        # Проверяем промах игрока
        if random.randint(1, 100) <= miss_chance:
            damage = 0

            attack_result = "Промах!"

        else:
            damage = weapons[player1.weapon]["damage"]

            # Проверяем критический удар игрока
            critical_hit_chance = weapons[player1.weapon]["critical_hit_chance"]

            if random.randint(1, 100) <= critical_hit_chance:
                damage *= 2

                attack_result = (
                    f"Критический удар! "
                    f"Вы нанесли {damage} урона!"
                )

            else:
                attack_result = (
                    f"Вы нанесли {damage} урона!"
                )

            monster_health -= damage

            # Уменьшаем прочность оружия от 1 до 5
            durability_loss = random.randint(1, 5)

            weapons[player1.weapon]["durability"] = max(
                0,
                weapons[player1.weapon]["durability"] - durability_loss
            )

            attack_result += (
                f" Прочность оружия уменьшилась на "
                f"{durability_loss}."
            )

    # Проверяем, убит ли монстр
    if monster_health <= 0:
        monster_health = 0

        monster_gold = monsters_data[current_monster]["gold"]
        monster_xp = monsters_data[current_monster]["xp"]

        player1.add_gold(monster_gold)
        player1.add_xp(monster_xp)

        attack_result = (
            f"{attack_result} "
            f"Вы победили монстра! "
            f"Получено золота: {monster_gold}. "
            f"Получено опыта: {monster_xp}."
        )

        battle_finished = True

        return redirect("/")

    # Атака монстра
    monster_miss_chance = monsters_data[current_monster]["miss_chance"]

    # Проверяем промах монстра
    if random.randint(1, 100) <= monster_miss_chance:

        attack_result = (
            f"{attack_result} "
            f"{current_monster.capitalize()} промахнулся!"
        )

    else:
        monster_damage = monsters_data[current_monster]["damage"]

        # Проверяем критический удар монстра
        critical_hit_chance_m = (
            monsters_data[current_monster]["critical_hit_chance_m"]
        )

        if random.randint(1, 100) <= critical_hit_chance_m:
            monster_damage *= 2

            attack_result = (
                f"{attack_result} "
                f"Критический удар! "
                f"{current_monster.capitalize()} "
                f"нанес вам {monster_damage} урона!"
            )

        else:
            attack_result = (
                f"{attack_result} "
                f"{current_monster.capitalize()} "
                f"нанес вам {monster_damage} урона!"
            )

        # Уменьшаем здоровье игрока
        player1.health = max(
            0,
            player1.health - monster_damage
        )

        # Проверяем, погиб ли игрок
        if player1.health <= 0:
            attack_result = "💀 Вы погибли!"
            battle_finished = True

    return redirect("/")
@app.route("/buy", methods=["POST"])
def buy():
    item = request.form.get("item")

    if item:
        player1.buy_item(item, shop)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)