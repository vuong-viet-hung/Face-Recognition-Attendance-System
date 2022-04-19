import csv
import datetime
import logging
import re
from typing import Match, Tuple
import serial


USB_PORT = "/dev/ttyUSB0"


def info(found_id_match: Match[str]) -> Tuple[str]:
    time = str(datetime.datetime.now())
    found_id = found_id_match.group(1)
    confidence = found_id_match.group(2)
    return (time, found_id, confidence)


def main() -> None:

    found_id_regex = re.compile(r"Found ID #(\d*) with confidence of (\d*)")

    with serial.Serial(USB_PORT, baudrate=9600) as serial_port, open(
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
            # Write match finger id info
            csv_writer.writerow(info(found_id_match))


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    main()
