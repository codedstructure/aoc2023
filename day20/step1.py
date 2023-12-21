class Stats:
    low = 0
    high = 0

    def result(self):
        return self.low * self.high

class Clock:
    ready = []

    def cycle(self):
        actions, self.ready = self.ready, []
        for level, source, dest in actions:
            if level == 'low':
                stats.low += 1
            else:
                stats.high += 1
            print(f"{source} -{level}-> {dest.name}")
            dest.pulse(level, source, dest)

stats = Stats()
clock = Clock()

class Component:
    def __init__(self, name, dests):
        self.name = name
        self.dests = dests

    def pulse(self, level, source, dest):
        pass

class Broadcast(Component):
    def pulse(self, level, source, _):
        for d in self.dests:
            clock.ready.append((level, self.name, d))

class Flipflop(Component):
    def __init__(self, name, dests):
        super().__init__(name, dests)
        self.state = 'off'

    def pulse(self, level, source, _):
        if level == 'low':
            # toggle flipflop
            self.state = {'on': 'off', 'off': 'on'}[self.state]
            for d in self.dests:
                out = {'on': 'high', 'off': 'low'}[self.state]
                clock.ready.append((out, self.name, d))

class Conjunction(Component):
    def __init__(self, name, dests):
        super().__init__(name, dests)
        self.inputs = {}

    # Took me a long time to realise I need this; I was
    # previously just using a defaultdict...
    def add_input(self, name):
        self.inputs[name] = 'low'

    def pulse(self, level, source, _):
        self.inputs[source] = level
        out = 'low' if all(inp == 'high' for inp in self.inputs.values()) else 'high'
        for d in self.dests:
            clock.ready.append((out, self.name, d))

class Button(Component):
    def press(self):
        for d in self.dests:
            clock.ready.append(('low', self.name, d))

class Output(Component):
    pass

def main():
    components = {}
    with open('inputs.txt') as f:
        for line in f:
            tname, dests = line.strip().split(' -> ')
            dests = dests.split(', ')
            if tname == 'broadcaster':
                c = Broadcast(tname, dests)
            elif tname.startswith('&'):
                c = Conjunction(tname[1:], dests)
            elif tname.startswith('%'):
                c = Flipflop(tname[1:], dests)
            else:
                raise Exception("Invalid line")

            components[c.name] = c

        components['output'] = Output('output', [])
        # 'rx' appears in my input data..
        components['rx'] = Output('rx', [])

        for c in components.values():
            c.dests = [components[d] for d in c.dests]
        for c in components.values():
            for d in c.dests:
                if isinstance(d, Conjunction):
                    d.add_input(c.name)

        components['button'] = Button('button', [components['broadcaster']])
        for i in range(1000):
            components['button'].press()
            while clock.ready:
                clock.cycle()
            print()

        print(stats.result())

if __name__ == '__main__':
    main()

