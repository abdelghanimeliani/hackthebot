# Stingo Telegram Bot


<br />
<p align="center">
  <a href="https://github.com/abdelghanimeliani/hackthebot">
    <img src="images/bot.png" alt="stingo" width="280" height="280" >
  </a>

  <h3 align="center">Stingo Telegram Bot</h3>

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>

  </ol>
</details>

### TESTs
<p align="center">
  ![App UI](images/screen.jpg)

![Demo](images/vid.MP4)
  </a>

<!-- ABOUT THE PROJECT -->
## About The Project
Stigno is a free, open source e-commerce telegram bot made by Python . Stingo offers too much features. 

### Built With

* [Python](https://www.python.org/)
* [telegram bot payments api](https://core.telegram.org/bots/payments)
* [Python-telegram-bot](https://core.telegram.org/bots/)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Befor you begin you need to install python and configure A virtual environment if you are in **Windows** you can just use `Conda` 
* Python [Ubuntu]
  ```sh
  $ sudo apt-get install python3 python3-pip
  ```
* VirtualEnv 
  ```sh
  $ pip install virtualenv
  ```

### Installation

1. Clone the repo 

2. Create VirtualEnv & Activate environment
   ```sh
    $ virtualenv env 
    $ source env/bin/activate
   ```
3. Install Requirements
   ```sh
    $ pip install -r requirements
   ```

<!-- USAGE EXAMPLES -->
## Usage

1. First you have to create a discord application and get an Application token check out the [documentation](https://discord.com/developers/docs/intro)
2. Set your application token in the configuration files  
3. Running The bot
   ```sh
    $ python3 main.py
   ```



<!-- PROJECT STRUCTURE -->
## Project-Structure
The project is split into multiple categories `cogs` where each category will hold a set of commands here are the current structure :
Karma has a lot of features, with **5 main categories**:


*   👩‍💼 **General**: `serverinfo`, `ping`, `server` and **1** more! 
*   🤖 **Mod**: `announce` 
*   👻 **Fun**: `tweet`, `advice`
*   ✉️ **Help**: `help`
*   👑 **Owner**: `shutdown`, `say`, `embed`




