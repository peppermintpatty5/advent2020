# Leaderboard Calculator

A simple leaderboard calculator written in Python.

The built-in leaderboard on the website shows cumulative rankings, so I was curious what the non-cumulative rankings would look like.

## Installation

Installation of required packages

```shell
python3 -m pip install -r requirements.txt
```

## Usage

Given a JSON input file such as `stats.json`, the command to summarize day 1 would be

```shell
python3 leaderboard.py 1 < stats.json
```
