class AVRParameter:
    def __init__(self, name, constraints='none', options='none'):
        self.name = name
        self.constraints = constraints
        self.options = options

    def name_for_find(self):
        if self.name[0] == 'R': return self.name[1:]
        return self.name

    def get_value(self, string):
        value: int
        add_symbols = ''
        if self.options == 'address':
            value = self._get_address_value(string)
        elif self.options == 'signed':
            add_symbols = '-' if string[0] == '1' else '+'
            value = self._get_signed_number_value(string)
        else:
            value = int(string, 2)

        value += self._get_constraints_adding()

        return self._format_value(value, add_symbols)

    def _format_value(self, value, add_symbols):
        if self.name[0] == 'R':
            return 'r' + str(value)
        return add_symbols + (hex(value) if value > 9 and self.options != 'signed' else str(value))

    def _get_constraints_adding(self):
        if self.constraints == 'none': return 0
        return int(self.constraints.split('<')[0])

    @staticmethod
    def _get_address_value(string):
        string += '0'
        return int(string, 2)

    def _get_signed_number_value(self, string):
        n = 0
        if string[0] == '1':
            string = self._invert_string(string)
            n += 1
        n += int(string, 2)
        n *= 2
        return n

    @staticmethod
    def _invert_string(string):
        string = list(string)
        for i in range(len(string)):
            if string[i] == '1':
                string[i] = '0'
            else:
                string[i] = '1'

        return ''.join(string)
