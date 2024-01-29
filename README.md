# Text-based-Adventure-Game-Enge-CDOF5

A text based adventure where the player's decisions define the outcome of the story !

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install Python:
If you don't have Python installed, you can download it from the official website: [Python Downloads](https://www.python.org/downloads/)


## Run the Code


1. Open a terminal command prompt

2. Clone the repository

3. Navigate to the directory where you saved the Python file 

4. If you are using Python3 run python3 text_adventure.py, if you are using python run python text_adventure.py


### Break down into end to end tests

These test cases are designed to cover different scenarios, such as initially providing an invalid input and then entering a valid one, to ensure the robustness of the make_choice function in handling user decisions.

For exemple in the second test of the test_text_adventure_game.py function : 

The side_effect parameter of the patch decorator is set to ['3', '2']. This simulates the user inputting '3' for the first choice, which is not a valid option, and then '2' for the second choice, which is a valid option.

The make_choice function is expected to handle the invalid input ('3') and prompt the user again until they provide a valid input ('2'). The test checks whether the function returns the expected result (2) after the valid input is provided.


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **engenouadje** 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details