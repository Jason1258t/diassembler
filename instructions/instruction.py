from instructions.parameter import AVRParameter


class AVRInstruction:
    def __init__(self, name, mask, parameters: list[AVRParameter]):
        self.name = name
        self.mask = mask
        self.parameters = parameters

    def write_with_parameters(self, parameters: dict):
        name = ' '.join(self.name.split()[1:])
        for p, v in parameters.items():
            name = name.replace(p, v)
        return self.name.split()[0] + ' ' + name
