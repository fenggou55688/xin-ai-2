class SimpleAIPredictorV2:
    def __init__(self, history, window_size=7):
        self.history = history
        self.window_size = window_size

    def predict(self, recent):
        from collections import defaultdict
        if len(recent) < self.window_size:
            return "❌ 過去資料不足"

        weights = [i + 1 for i in range(self.window_size)]
        patterns = defaultdict(lambda: [0, 0])  # {'pattern': [B_count, P_count]}

        for i in range(len(self.history) - self.window_size):
            pattern = ''.join(self.history[i:i+self.window_size])
            next_char = self.history[i+self.window_size]
            if next_char in ['B', 'P']:
                idx = 0 if next_char == 'B' else 1
                for j in range(self.window_size):
                    w = weights[j]
                    patterns[pattern][idx] += w

        recent_pattern = ''.join(recent)
        prediction = patterns.get(recent_pattern, None)
        if prediction:
            total = sum(prediction)
            prob_b = round(prediction[0] / total * 100, 1)
            prob_p = round(prediction[1] / total * 100, 1)
            suggestion = "✅ 建議下注：" + ("莊(B)" if prob_b > prob_p else "閒(P)")
            return f"近期模式：{recent_pattern}\n莊(B) 機率：{prob_b}%\n閒(P) 機率：{prob_p}%\n{suggestion}"
        else:
            return "⚠️ 找不到匹配的過往模式"

