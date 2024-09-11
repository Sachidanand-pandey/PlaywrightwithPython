# Python Project with Playwright

This project uses Python with Playwright for end-to-end testing.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python **: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

Follow these steps to set up the project environment:

1. **Clone the Repository**
   git clone https://github.com/Sachidanand-pandey/PlaywrightwithPython.git
   cd PlaywrightwithPython


2. Open the Project in PyCharm 

3. Configure Python Interpreter


4. **Install Required Packages**
   pip install playwright  
   playwright install
   pip install pyee
   pip install pytest-playwright 
   pip install allure-pytest pip install request
   pip install pytest-asyncio           

5. **Running the Tests**
   pytest -v -s --alluredir=report --slowmo 2000 ./automationdemo/test


6. **Generating Allure Report**
   allure serve report
