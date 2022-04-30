from stem import Signal
from stem.control import Controller
import time

controller = Controller.from_port(port=9051)
controller.authenticate(password="yourpass")
print(controller.get_info("status/circuit-established"))
while(str(controller.get_info("status/circuit-established"))=="0"):
  time.sleep(0.5)

#begin
