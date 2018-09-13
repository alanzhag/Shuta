import serial
import serial.tools.list_ports


def fetch_port(func):
    def assign_valid_port(*args):
        ports = map(lambda serial_port: serial_port.device, serial.tools.list_ports.comports())
        for port in ports:
            try:
                serial.Serial(port, 115200)
                return func(*args, port)
            except serial.SerialException:
                continue
        raise Exception("There's no board available.")

    return assign_valid_port


def encode(func):
    def command_encoder(first_arg, command):
        return func(first_arg, command.encode())

    return command_encoder


class ArduinoCommander:

    @fetch_port
    def __init__(self, port, rate=None):
        self.rate = rate or 115200
        self.board_serial = serial.Serial(port, self.rate)

    def send_command(self, command):
        self.board_serial.write(command.encode())
