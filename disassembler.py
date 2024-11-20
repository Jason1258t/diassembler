from command_parser import CommandParser
from packet import Packet


class Disassembler:
    def parse(self, formated_string: str):
        self._parse_packets(formated_string)
        self._next_packet_offset = 0
        total_commands = []
        for i in range(len(self.packets)):
            p = self.packets[i]
            np = self.packets[i + 1] if i < len(self.packets) - 1 else None
            a = self._parse_commands_from_packet(p, np)
            total_commands += a

        return total_commands

    def _parse_packets(self, formated_string: str):
        self.packets = []
        for i in formated_string.split('\n'):
            self.packets.append(Packet(i[1:]))

    def _parse_commands_from_packet(self, packet: Packet, next_packet: Packet | None):
        commands = []
        data_bytes = packet.get_data_binary()[self._next_packet_offset:]
        if self._next_packet_offset != 0: self._next_packet_offset = 0
        address = int(packet.start_address, 16)
        while len(data_bytes) != 0:
            try:
                c, out = self._find_and_format_command(data_bytes, address)
            except ValueError as e:
                if len(data_bytes) < 8:
                    data_bytes += next_packet.get_data_binary()[:4]
                    c, out = self._find_and_format_command(data_bytes, address)
                    self._next_packet_offset = 4
                else:
                    print(e)
                    raise ValueError('cant find a command')
            commands.append(out)
            bytes_len = len(c.mask.split()) // 2
            address += bytes_len
            data_bytes = data_bytes[len(c.mask.split()):]

        return commands

    def _find_and_format_command(self, data_bytes, address):
        c, words = self._extract_first_command(data_bytes)
        p = CommandParser.extract_parameters(c, ' '.join(words))
        try:
            result_parameters = CommandParser.get_result_parameters(c, p)
        except:
            print(c.name, p)
        return c, self._format_command_out(address, words, c, result_parameters)

    @staticmethod
    def _extract_first_command(data_bytes):
        words = data_bytes[:4]
        c = CommandParser.find_command(' '.join(words))
        if c is None:
            words = data_bytes[:8]
            c = CommandParser.find_command(' '.join(words))

        if c is None:
            raise ValueError('Not found command with mask ',
                             ' '.join(words) + '; remains packet data: {0}'.format(data_bytes))

        return c, words

    @staticmethod
    def _format_command_out(address, words, comm, parameters):
        address = hex(address)[2:].zfill(2)
        orig_bytes = Packet.get_original_bytes_from_words(words)
        command_out = comm.write_with_parameters(parameters)
        return address + ': ' + orig_bytes + ' ' + command_out
