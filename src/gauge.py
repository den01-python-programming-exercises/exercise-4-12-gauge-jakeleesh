class Gauge:
    def __init__(self):
        self.gauge_value = 0
    
    def increase(self):
        if (self.gauge_value < 5):
            self.gauge_value += 1

    def decrease(self):
        if (self.gauge_value > 0):
            self.gauge_value -= 1

    def value(self):
        return self.gauge_value

    def full(self):
        if (self.gauge_value == 5):
            return True
        else:
            return False 