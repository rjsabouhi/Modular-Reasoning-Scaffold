class MRS:
    def __init__(self, model, num_slots=4, max_depth=8):
        self.model = model
        self.slots = [None] * num_slots
        self.max_depth = max_depth
        self.depth = 0

    def update_slot(self, i, value):
        self.slots[i % len(self.slots)] = value

    def drift(self, text):
        return abs(hash(text)) % 1000 / 1000.0

    def run(self, prompt):
        x = prompt
        history = []

        while self.depth < self.max_depth:
            self.depth += 1
            o = self.model(x)
            Δ = self.drift(o)
            history.append((x, o, Δ))

            if Δ > 0.65:
                break

            self.update_slot(self.depth, o)
            x = o

        return {
            "history": history,
            "slots": self.slots,
            "final": history[-1][1]
        }
