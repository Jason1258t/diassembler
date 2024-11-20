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

        if hex(value) in self.special_registers.keys() and self.name in 'qwertyuiopasdfghjzxcvbnm'.upper():
            return self.special_registers[hex(value)]

        return self._format_value(value, add_symbols)

    special_registers = {
        '0x3': 'PINB',
        '0x4': 'DDRB',
        '0x5': 'PORTC',
        '0x6': 'PINC',
        '0x7': 'DDRC',
        '0x8': 'PORTC',
        '0x9': 'PIND',
        '0xa': 'DDRD',
        '0xc': 'PORTD',
        '0x2c': 'SPCR',
        '0x3d': 'SPL',
        '0x3e': 'SPH',
        '0x3f': 'SREG'
    }

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
