from fnmatch import fnmatch

from instructions.generated_commands import instructions
from instructions.instruction import AVRInstruction


class CommandParser:
    @classmethod
    def find_command(cls, binary_words: str):
        for i in instructions:
            formated_mask = cls._get_clear_mask(i.mask)
            if fnmatch(binary_words, formated_mask):
                return i

    @staticmethod
    def _get_clear_mask(mask):
        for x in mask:
            if x not in '01 ':
                mask = mask.replace(x, '?')

        return mask

    @staticmethod
    def extract_parameters(command: AVRInstruction, string: str):
        parameters = {}
        for i in command.parameters:
            parameters[i.name] = ''

        for p in command.parameters:
            for i in range(len(command.mask)):
                if command.mask[i] == p.name_for_find():
                    parameters[p.name] += string[i]

        return parameters

    @staticmethod
    def get_parameters_values_and_annotations(command: AVRInstruction, parameters, command_address):
        annotations_list = []

        for p in command.parameters:
            parameters[p.name] = p.get_value(parameters[p.name])
            if p.options == 'signed':
                annotations_list.append(p.get_jump_annotation(command_address, parameters[p.name]))

        return parameters, annotations_list
