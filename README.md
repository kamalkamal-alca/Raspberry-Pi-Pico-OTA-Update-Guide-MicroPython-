Controlling GPIO LEDs (4 LEDs) on my Raspberry Pi using CircusOfThings with Python.

- Install the following libraries: requests, json, and W1ThermSensor.

- Create a circusofthings.com account.

- In https://circusofthings.com/workshop, create a new signal and name it control_led1, control_led2, control_led3, and control_led4.
- Key: 28440 for LED1 (example).
- Key: 28441 for LED2 (example).
- Key: 28442 for LED3 (example).

- Key: 28443 for LED4 (example).

- Go to https://circusofthings.com/dashboard.

- Click on View: Add a view to monitor the value of an existing signal.

- Select control_led1, ..., and use a button.

- Run the code to control LED1, LED2, ..., using the dashboard buttons.
