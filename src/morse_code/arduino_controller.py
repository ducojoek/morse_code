import pyvisa

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()


def list_resources():
    """returns the available ports

    Returns:
        list: list of available ports
    """
    return ports


class ArduinoVISADevice:
    """Controling the arduino"""

    def __init__(self, ports):
        """defines self

        Args:
            ports (str): port of arduino
        """

        self.device = rm.open_resource(
            ports, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        """returns id of arduino

        Returns:
            ID arduino
        """

        identification = self.device.query("*IDN?")
        return identification

    def set_output_value(self, value):
        """set output value

        Args:
            value (_type_): set output value on channel 0
        """
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        """return output value

        Returns:
            output value of CH 0 in bit
        """
        return self.device.query("OUT:CH0?")

    def get_input_value(self, channel):
        """returns voltage of channel "channel" in bit

        Args:
            channel: channel of arduino

        Returns:
            voltage in bit
        """

        u1 = self.device.query(f"MEAS:CH{channel}?")

        return u1

    def get_input_voltage(self, channel):
        """measures input voltage of a channel of the arduino

        Args:
            channel (int): witch channel on the arduino

        Returns:
            voltage: calculates the voltage at the bit and returns that
        """

        u1 = self.device.query(f"MEAS:CH{channel}?")
        vol = 3.3 / 1023 * int(u1)
        return vol
