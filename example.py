# TO CORRECT SETUP INSTAPY SESSION READ THE DOCUMENTATIONS
from instapy import InstaPy
from instapy.util import smart_run
import schedule
import time
import random
insta_username = 'your_instagram_username'
insta_password = 'your_password'
session = InstaPy(username=insta_username,
                password=insta_password,
                headless_browser=False)
with smart_run(session):
    """ Activity flow """
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=1200,
                                    min_followers=45,
                                    max_following=1200,
                                    min_following=77)


    #
    #   CODE START HERE
    #
    import random
    def random_users(long_arr, num):
        return [ long_arr[random.randint(0, len(long_arr))] for x in range(0, num)]

    def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

    # HERE GOES THE RESULT OF THE SCRAPE
    followers_account1 = ['here your list']
    followers_account2 = ['here the other list and so on...']
    total_users = [followers_account1, followers_account2 ]
    unique_values = list(set(x for l in total_users for x in l))

    with open('users_explored.txt', 'r') as text_file:
        arleady_explored = text_file.read().split("\n")

    to_explore = diff(unique_values, arleady_explored)
    to_explore_now = random_users(to_explore, 100)
    arleady_explored_and_now = arleady_explored + to_explore_now

    session.set_do_follow(enabled=False, percentage=50)
    session.set_comments(["🔝🔝🔝", "👍"], media="Photo")
    session.set_do_comment(enabled=False, percentage=80)
    session.set_do_like(True, percentage=70)
    session.interact_by_users(to_explore_now, amount=3, randomize=True, media='Photo')



    with open('users_explored.txt', 'w') as f:
        for item in arleady_explored_and_now:
            if (item): 
                f.write("%s\n" % item)


    print('USERS TO EXPLORE: ', len(to_explore))
    print('users explored in total: ', len(arleady_explored_and_now))
    numebers_of_like_per_days = 200
    print('you have ', len(to_explore)/numebers_of_like_per_days, ' days untill you expire all contacts...')