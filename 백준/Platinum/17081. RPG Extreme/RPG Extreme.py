walls = set()
traps = set()
treasures = {}
monsters = {}
boss_pos = (0, 0)
monster_amount = 0
treasure_amount = 0
player = {
    "x": 0, "y": 0, "hp": 20, "max_hp": 20,
    "atk": 2, "def": 2, "exp": 0, "level": 1,
    "weapon": 0, "armor": 0, "accessory": set()
}
start_pos = (0, 0)

n, m = map(int, input().split())
for i in range(n):
    line = input()
    for j, x in enumerate(line):
        if x == "#":
            walls.add((i, j))
        if x == "^":
            traps.add((i, j))
        if x == "@":
            start_pos = (i, j)
            player["x"], player["y"] = j, i
        if x == "M":
            boss_pos = (i, j)
            monster_amount += 1
        if x == "&":
            monster_amount += 1
        if x == "B":
            treasure_amount += 1

player_input = input()

for _ in range(monster_amount):
    r, c, s, w, a, h, e = input().split()
    r, c = int(r) - 1, int(c) - 1
    data = {
        "name": s, "atk": int(w), "def": int(a),
        "hp": int(h), "max_hp": int(h), "exp": int(e)
    }
    monsters[(r, c)] = data

for _ in range(treasure_amount):
    r, c, t, s = input().split()
    treasures[(int(r) - 1, int(c) - 1)] = {"type": t, "value": s}

turn = 0
state = None
for move in player_input:
    turn += 1
    dx, dy = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}[move]
    nx, ny = player["x"] + dx, player["y"] + dy
    if 0 <= nx < m and 0 <= ny < n and (ny, nx) not in walls:
        player["x"], player["y"] = nx, ny
        if (ny, nx) in treasures:
            treasure = treasures[(ny, nx)]
            if treasure["type"] == "W":
                player["weapon"] = int(treasure["value"])
            if treasure["type"] == "A":
                player["armor"] = int(treasure["value"])
            if treasure["type"] == "O" and len(player["accessory"]) < 4:
                player["accessory"].add(treasure["value"])
            del treasures[(ny, nx)]
        if (ny, nx) in monsters:
            monster = monsters[(ny, nx)]
            p_atk = player["atk"] + player["weapon"]
            m_atk = max(1, monster["atk"] - player["def"] - player["armor"])
            is_boss = (ny, nx) == boss_pos
            if is_boss and "HU" in player["accessory"]:
                player["hp"] = player["max_hp"]
            first_turn = True
            win = True
            while True:
                atk = p_atk
                if first_turn and "CO" in player["accessory"]:
                    atk = p_atk * (3 if "DX" in player["accessory"] else 2)
                monster["hp"] -= max(1, atk - monster["def"])
                if monster["hp"] <= 0:
                    break
                if not first_turn or "HU" not in player["accessory"] or not is_boss:
                    player["hp"] -= m_atk
                if player["hp"] <= 0:
                    win = False
                    break
                first_turn = False
            if win:
                exp = monster["exp"]
                if "EX" in player["accessory"]:
                    exp = exp * 6 // 5
                player["exp"] += exp
                if "HR" in player["accessory"]:
                    player["hp"] = min(player["max_hp"], player["hp"] + 3)
                if player["exp"] >= player["level"] * 5:
                    player["level"] += 1
                    player["exp"] = 0
                    player["hp"] = player["max_hp"] = player["max_hp"] + 5
                    player["atk"] += 2
                    player["def"] += 2
                if is_boss:
                    state = ""
                    break
                del monsters[(ny, nx)]
            elif "RE" not in player["accessory"]:
                player["hp"] = 0
                state = monster["name"]
                break
            else:
                player["accessory"].remove("RE")
                player["y"], player["x"] = start_pos
                player["hp"] = player["max_hp"]
                monster["hp"] = monster["max_hp"]
    else:
        nx, ny = player["x"], player["y"]
    if (ny, nx) in traps:
        player["hp"] -= 1 if "DX" in player["accessory"] else 5
        if player["hp"] <= 0:
            if "RE" not in player["accessory"]:
                player["hp"] = 0
                state = "SPIKE TRAP"
                break
            player["accessory"].remove("RE")
            player["y"], player["x"] = start_pos
            player["hp"] = player["max_hp"]

for i in range(n):
    for j in range(m):
        if not state and (i, j) == (player["y"], player["x"]):
            print("@", end="")
            continue
        if (i, j) in walls:
            print("#", end="")
            continue
        if (i, j) in monsters:
            print("M" if (i, j) == boss_pos else "&", end="")
            continue
        if (i, j) in treasures:
            print("B", end="")
            continue
        if (i, j) in traps:
            print("^", end="")
            continue
        print(".", end="")
    print()
print(f"Passed Turns : {turn}\n"
      f"LV : {player['level']}\n"
      f"HP : {player['hp']}/{player['max_hp']}\n"
      f"ATT : {player['atk']}+{player['weapon']}\n"
      f"DEF : {player['def']}+{player['armor']}\n"
      f"EXP : {player['exp']}/{player['level'] * 5}")
if state:
    print(f"YOU HAVE BEEN KILLED BY {state}..")
elif state == "":
    print("YOU WIN!")
else:
    print("Press any key to continue.")
