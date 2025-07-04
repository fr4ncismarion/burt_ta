# create venv
python3 -m venv venv

# activate venv 
# mac os
source venv/bin/activate

# windows
source venv/Scripts/activate

# deactivate 
deactivate

# install the requirements
pip3 install -r requirements.txt


# run the full suite
pytest tests/calculator.py

# run per function
pytest test/calculator.py::test_calculate_operator
pytest test/calculator.py::test_calculate_invalid_input
pytest test/calculator.py::test_validate_buttons
pytest test/calculator.py::test_validate_hyperlinks