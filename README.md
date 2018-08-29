# Instafollower
Automation script for “farming” Likes, Comments and Followers on Instagram



# Installation

    pip install -r requirements.txt


# Configuration

## Before running script you have to export username and password environment variables

    export instagram_username='my_username'
    export instagram_password='my_super_strong_password'


# Usage

## Run follow, like, comment script:

    python main.py run_follower --tag ig_europe --count 500 --no-gui

## Run unfollow:

    python main.py run_unfollower --count 100
