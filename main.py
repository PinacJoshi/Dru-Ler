from stem import Signal
from stem.control import Controller

controller = Controller.from_port(port=9051)
controller.authenticate(password="yourpass")
print(controller.get_info("status/circuit-established"))