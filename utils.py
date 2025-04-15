import random
from collections import Counter

def predict_next(history, window=7):
    recent = history[-window:]
    weights = [i+1 for i in range(len(recent))]
    counter = {'B': 0, 'P': 0}

    for i, result in enumerate(recent):
        if result in counter:
            counter[result] += weights[i]

    total = sum(counter.values()) or 1
    return {k: round(v / total * 100, 2) for k, v in counter.items()}

def update_roads(history):
    def build_road(data):
        road = []
        col = []
        last = None
        for val in data:
            if val == last:
                col.append(val)
            else:
                if col:
                    road.append(col)
                col = [val]
                last = val
        if col:
            road.append(col)
        return road

    big_road = build_road([h for h in history if h in ["B", "P"]])
    # 模擬大眼仔、小路、曱甴路
    eye_road = build_road([h for i, h in enumerate(history) if i % 2 == 0])
    small_road = build_road([h for i, h in enumerate(history) if i % 2 == 1])
    cockroach_road = build_road([random.choice(["B", "P"]) for _ in history])

    return {
        "big": big_road,
        "eye": eye_road,
        "small": small_road,
        "cockroach": cockroach_road,
    }

def analyze_patterns(history):
    patterns = {"單跳": False, "雙跳": False, "長龍": False}
    if len(history) < 4:
        return patterns

    last = history[-1]
    if history[-1] != history[-2] and history[-2] != history[-3]:
        patterns["單跳"] = True
    if history[-1] != history[-2] and history[-2] != history[-3] and history[-3] != history[-4]:
        patterns["雙跳"] = True
    if all(h == last for h in history[-4:]):
        patterns["長龍"] = True

    return patterns
