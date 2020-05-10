from simulation.builder.well.slots import Slots

class Agregator:
    def __init__(self):
        self._lst = []

    def add_one(self, one, pre='', suf=''):
        self._lst.append(Slots.one(self._prefix(pre,self._suffix(one,suf))))

    def add_two(self, one, two, pre='', suf=''):
        self._lst.append(Slots.two(self._prefix(pre,one), self._suffix(two,suf)))

    def add_three(self, one, two, three, pre='', suf=''):
        self._lst.append(Slots.three(self._prefix(pre,one), two, self._suffix(three,suf)))

    def add_four(self, one, two, three, four, pre='', suf=''):
        self._lst.append(Slots.four(self._prefix(pre,one), two, three, self._suffix(four,suf)))

    def add_five(self, one, two, three, four, five, pre='', suf=''):
        self._lst.append(Slots.five(self._prefix(pre,one), two, three, four, self._suffix(five,suf)))

    def add_six(self, one, two, three, four, five, six, pre='', suf=''):
        self._lst.append(Slots.six(self._prefix(pre,one), two, three, four, five, self._suffix(six,suf)))

    def add_seven(self, one, two, three, four, five, six, seven, pre='', suf=''):
        self._lst.append(Slots.seven(self._prefix(pre,one), two, three, four, five, six, self._suffix(seven,suf)))

    def add_eight(self, one, two, three, four, five, six, seven, eight, pre='', suf=''):
        self._lst.append(Slots.eight(self._prefix(pre,one), two, three, four, five, six, seven, self._suffix(eight,suf)))

    def add_nine(self, one, two, three, four, five, six, seven, eight, nine, pre='', suf=''):
        self._lst.append(Slots.nine(self._prefix(pre,one), two, three, four, five, six, seven, eight, self._suffix(nine,suf)))

    def _prefix(self, pre, stg):
        return '{}{}'.format(pre,stg)

    def _suffix(self, stg, suf):
        return '{}{}'.format(stg,suf)

    def to_string(self):
        return '\n'.join(self._lst)

    def __repr__(self):
        return self.to_string()