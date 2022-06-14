# Competitive Programming Scraper (CPS)

This is a web scraper I made for downloading DMOJ problem solutions. DMOJ is a platform for training in competitive programming, similar to Codeforces and Leetcode.

This project is my first written in python, and utilizes the [Requests](https://pypi.org/project/requests/) library to make HTTTP requests and persist user login.

Here's my [DMOJ profile](https://dmoj.ca/user/JY900)

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

To run the program, simply do

    python main.py

## Further Notes

Download times for each solution will vary. This is because the scraper looks for your best solution within the solution ranking pages of each problem.

For a low point problem such as [CCC '17 J1 - Quadrant Selection
](https://dmoj.ca/problem/ccc17j1), there will be thousands of solutions spread across multiple pages in the [ranking tab](https://dmoj.ca/problem/ccc17j1/rank/). Scraping and processing my solution for this problem (placed on the 23rd page) takes around one minute to complete.

In contrast, high point problems like [COCI '14 Contest 1 #6 Kamp](https://dmoj.ca/problem/coci14c1p6) have a relatively minimal number of solutions, so one's solution will have a higher chance of being placed on an earlier ranking page. Scraping and processing my solution for this problem (placed 3rd overall) takes around one second.

Therefore, the time taken to download one's problem solution generally depends on the ranking placement of said solution, and the number of people who have solved the problem.
