# Instafollower
Automation script for “farming” Likes, Comments and Followers on Instagram



# Installation

    pip install -r requirements.txt


# Usage

## Run follow, like, comment script:

    export instagram_username='my_username'
    export instagram_password='my_super_strong_password'

    python main.py run_follower --tag ig_europe --count 500 --no-gui

## Run unfollow:

    python main.py run_unfollower --count 100
