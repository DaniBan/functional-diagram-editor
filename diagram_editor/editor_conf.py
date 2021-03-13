LISTBOX_MIMETYPE = "application/x-item"

OP_CODE_INPUT_1 = 1
OP_CODE_INPUT_2 = 2
OP_CODE_INPUT_3 = 3
OP_CODE_OUTPUT_1 = 4
OP_CODE_WASHER = 5
OP_CODE_PEELING = 6
OP_CODE_INPUT_4 = 7
OP_CODE_PASTEURIZER = 8
OP_CODE_EVAPORATOR = 9
OP_CODE_REFINER = 10
OP_CODE_MIXER = 11
OP_CODE_HEATER = 12


NODES = {
}


class ConfException(Exception): pass
class InvalidNodeRegistration(ConfException): pass
class OpCodeNotRegistered(ConfException): pass


def register_node_now(op_code, class_reference):
    if op_code in NODES:
        raise InvalidNodeRegistration("Duplicate node registration of '%s'. There is already %s" %(
            op_code, NODES[op_code]
        ))
    NODES[op_code] = class_reference


def register_node(op_code):
    def decorator(original_class):
        register_node_now(op_code, original_class)
        return original_class
    return decorator

def get_class_from_opcode(op_code):
    if op_code not in NODES: raise OpCodeNotRegistered("OpCode '%d' is not registered" % op_code)
    return NODES[op_code]