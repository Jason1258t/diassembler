from command_parser import CommandParser
from packet import Packet


class Disassembler:
    def parse(self, formated_string: str):
        self._parse_packets(formated_string)
        total_commands = []
        for p in self.packets:
            a = self._parse_commands_from_packet(p)
            total_commands += a

        return total_commands

    def _parse_packets(self, formated_string: str):
        self.packets = []
        for i in formated_string.split('\n'):
            self.packets.append(Packet(i[1:]))

    def _parse_commands_from_packet(self, packet: Packet):
        commands = []
        data_bytes = packet.get_data_binary()
        address = int(packet.start_address, 16)
        while len(data_bytes) != 0:
            c, out = self._find_and_format_command(data_bytes, address)
            commands.append(out)
            bytes_len = len(c.mask.split()) // 2
            address += bytes_len
            data_bytes = data_bytes[len(c.mask.split()):]

        return commands

    def _find_and_format_command(self, data_bytes, address):
        c, words = self._extract_first_command(data_bytes)
        p = CommandParser.extract_parameters(c, ' '.join(words))
        result_parameters = CommandParser.get_result_parameters(c, p)
        return c, self._format_command_out(address, words, c, result_parameters)

    @staticmethod
    def _extract_first_command(data_bytes):
        words = data_bytes[:4]
        c = CommandParser.find_command(' '.join(words))
        if c is None:
            words = data_bytes[:8]
            c = CommandParser.find_command(' '.join(words))
        if c is None:
            print('Not found command with mask ', ' '.join(words))

        return c, words

    @staticmethod
    def _format_command_out(address, words, comm, parameters):
        address = hex(address)[2:].zfill(2)
        orig_bytes = Packet.get_original_bytes_from_words(words)
        command_out = comm.write_with_parameters(parameters)
        return address + ': ' + orig_bytes + ' ' + command_out
