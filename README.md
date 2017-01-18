# Apollo

Apollo is the great tool to get a fast waether forecast for your city.

## Introduction

With Apollo, you can get many weather details for your city. For example:

* wind
* weather condition
* humidity

Apollo is written in Python, an easy and powerful language for powerful tools.

## Get Started

Follow this step for use Apollo correctly:

* Run `setup.py` to install all dependencies
* Open `config.json` and add your name and surname. Also, you need to add a default city value. E.g.:

        {
          "City": "New York",
          "Api_Key": "1fad2670e91546ebd6f280e185b23732",
          "Name": "John",
          "Surname": "Smith"
        }

* Run `Apollo.py` and add next city name
* Run `Apollo.py help` to print all the available commands

### Dependencies

The project is dependent on third-party modules:

* [pyowm](https://pypi.python.org/pypi/pyowm) for OWM Api
* [simplejson](https://pypi.python.org/pypi/simplejson) for load and modify config.json

## Development

Do you want to contribute? Great!

* Fork Apollo: click the Fork button in the header of the repository.
* You’ve successfully forked the Apollo repository, but so far, you will need to clone it to your computer:

  ```sh
  git clone git@github.com:<your_username>/Apollo.git
  ```

* When you’re ready to propose changes to the main project, make a pull request.

## Contributors

* Dellaquila Francesco Paolo
