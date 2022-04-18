import csv
import datetime
import logging
import re
from typing import List
import serial.tools.list_ports


USB_PORT = "/dev/ttyUSB0"
BAUNDRATE = 9600


def info(packet: str) -> List[str]:
    return [datetime.datetime.now()] + re.findall(r"\d+", packet)


def main() -> None:

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    found_id_regex = re.compile(r"Found ID #(\d)*")

    with serial.Serial(USB_PORT, BAUNDRATE) as serial_port, open(
        "matches.csv", "a"
    ) as matches:

        csv_writer = csv.writer(matches)

        while True:
            # Read packet from serial port
            try:
                packet = serial_port.readline().decode("utf-8")
            except serial.serialutil.SerialException:
                continue
            logging.info(packet.strip())
            # Filter match finger id
            found_id_match = found_id_regex.search(packet)
            if found_id_match is None:
                continue
            # Save match finger id info
            csv_writer.writerow(info(packet))


if __name__ == "__main__":
    main()
