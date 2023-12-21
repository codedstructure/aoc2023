from dataclasses import dataclass

@dataclass
class XmasPart:
    x: int
    m: int
    a: int
    s: int

    @classmethod
    def parse(cls, line):
        a = {}
        for attr in line[1:-1].split(','):
            k, v = attr.split('=')
            a[k] = int(v)
        return XmasPart(**a)

    def rating(self):
        return self.x + self.m + self.a + self.s

class Range:
    def __init__(self, low=1, high=4000):
        self.low = low
        self.high = high

    def count(self):
        if self.valid():
            return self.high - self.low + 1
        else:
            return 0

    def valid(self):
        self.high >= self.low

    def apply_lt(self, lt):
        self.high = lt - 1

    def apply_gt(self, gt):
        self.low = gt + 1

class Workflow:
    def __init__(self, line):
        self.conditions = []
        self.name, conds = line.split('{')
        conds = conds[:-1]
        for cond in conds.split(','):
            self.conditions.append(cond)

    def run(self, ranges):
        for cond in self.conditions:
            if ':' not in cond:
                # this is a direct target, possibly 'R' or 'A'
                return cond
            check, target = cond.split(':')
            if '>' in check:
                attr, gtval = check.split('>')
                gtval = int(gtval)
                if getattr(part, attr) > gtval:
                    return target
            if '<' in check:
                attr, ltval = check.split('<')
                ltval = int(ltval)
                if getattr(part, attr) < ltval:
                    return target

def main():
    with open('test.txt') as f:
        workflows = []
        for line in f:
            line = line.strip()
            if not line:
                # we don't care about parts for step2.
                break
            workflows.append(line)

    flows = {}
    for wf in workflows:
        w = Workflow(wf)
        flows[w.name] = w

    ranges = {'x': Range(), 'm': Range(), 'a': Range(), 's': Range()}

    total = 0


    flow_name = 'in'
    while flow_name not in ('A', 'R'):
        flow = flows[flow_name]
        flow_name = flow.run(part)
    if flow_name == 'A':
        total += part.rating()
    print(total)


if __name__ == '__main__':
    main()
