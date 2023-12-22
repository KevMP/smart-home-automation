from class_aircondtioner import *
import time

def database_airconditioner_scanner(scan_interval=0.5):  # Scan every half second
    ac = Airconditioner()
    try:
        while True:
            command = ac.get_command_from_ai()
            if command:
                ac.write_command_to_ac()
                print(f"COMMAND: {command} WRITTEN TO THE AIRCONDITIONER TABLE")
            time.sleep(scan_interval)  # Wait for half a second before the next scan
    except KeyboardInterrupt:
        # Here you can handle the manual stop if needed.
        pass
    finally:
        ac.close_connection()
        # Here you can handle the closure of database connection if needed.

if __name__ == "__main__":
    database_airconditioner_scanner()
