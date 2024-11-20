class Packet:
    def __init__(self, string: str):
        self._formated_string = string
        self._initial_string = string
        self.start_address = self._get_start_address()
        self.bytes_length = self._get_bytes_length()
        self.data_type = self._get_data_type()
        self.string_data = self._get_string_data()
        self.control_sum = self._get_control_sum()

    def initial_string(self):
        return self._initial_string

    def get_data_binary(self):
        data = []
        for i in self.string_data:
            for j in i:
                data.append(bin(int(j, 16))[2:].zfill(4))
        return data

    def _get_bytes_length(self):
        length = hex(int(self._formated_string[:2], 16))
        return length

    def _get_start_address(self):
        address = hex(int(self._formated_string[2:6], 16))[2:].zfill(4)
        return address

    def _get_data_type(self):
        data_type = self._formated_string[6:8]
        return data_type

    def _get_control_sum(self):
        return hex(int(self._formated_string[-2:], 16))

    def _get_string_data(self):
        data = []
        for i in range(3 + 8, len(self._formated_string) - 2, 4):
            data.append(self._formated_string[i - 1:i + 1] + self._formated_string[i - 3:i - 1])

        return data

    def print_packet(self):
        print(self.bytes_length, self.start_address, self.data_type, *self.string_data, self.control_sum)

    def print_packet_data_binary(self):
        out_data = []
        for i in self.string_data:
            for j in i:
                out_data.append(bin(int(j, 16))[2:].zfill(4))

        print(*out_data)
