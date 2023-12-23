from class_aircondtioner import *
import time

def database_airconditioner_scanner():
    ac = Airconditioner()
    while True:
        command = ac.get_command_from_ai()
        if command:
            ac.write_command_to_ac()
            print(f"COMMAND: {command} WRITTEN TO THE AIRCONDITIONER TABLE")

if __name__ == "__main__":
    database_airconditioner_scanner()
