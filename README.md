# Competitive Programming Scraper (CPS)

**This is fork of [JonathanYuan900's repo](https://github.com/JonathanYuan900/CPS) with some extra edits of my own.<br>All first-person references were made by the original author.**

This is a web scraper I made for downloading DMOJ problem solutions. DMOJ is a platform for training in competitive programming, similar to Codeforces and Leetcode.

Here's my [DMOJ profile](https://dmoj.ca/user/JY900)

This project is my first written in python, and utilizes the [Requests](https://pypi.org/project/requests/) library to make HTTP requests and persist user login.
It will only process user solutions in C, C++, Python, Java, or Text.

## Getting Started

First install the required libraries from the PyPI repository

    pip install bs4 requests python-dotenv

Then clone the project to your machine

    git clone https://github.com/JonathanYuan900/CPS.git
    cd CPS

Finally, you will need to create a file called `.env` defining the environment variables `DMOJ_USERNAME`, `DMOJ_PASSWORD` and `TARGET_DIRECTORY`

For example

    DMOJ_USERNAME=your_username
    DMOJ_PASSWORD=your_password
    TARGET_DIRECTORY=path_to_download_directory

## Usage

To run the program, simply execute

    python main.py

## Further Notes

Download times for each solution will now be virtually constant, as the scraper will only check 1 page with all of the user's correct submissions to that problem. 
Only the most recent one will be selected for download. 
However, the program also checks a text file to see if the problem's solution has already been downloaded.
The more problems that the user has solved, the longer it will take for the later downloads. 
