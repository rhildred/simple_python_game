END = 0

def fix_or_help(player_input):
    storystate = END
    player_next = "fixing your flat is a good idea, you are soaked but on your way"
    if player_input == "HELP":
        storystate = help
        player_next = """When you get to the door of the house, it sounds like there is a party going on. 
        Your spidey sense is telling you this is a party that you don't want to be a part of. Do you go back and FIX your own flat or do you KNOCK on the door
        """
    return(player_next, storystate)

def help(player_input):
    storystate = END
    player_next = "you should have trusted your spidey sense, the party was terrible and there are some things you just can't unsee."
    if player_input == "FIX":
        player_next =  "fixing your flat was the right choice, you are really we and cold, but you get in the car and drive home with the heat on full blast."
    return(player_next, storystate)

# The Main Guard
if __name__ == "__main__":
    print("""
    It is a dark night. you are on a country road in the middle of nowhere. Bang! You hit a pothole and you have a flat. You pull over and it starts pouring.
    You try to call CAA but you don't have any bars. There is a farmhouse 500 meters away up a laneway. Do you FIX your own flat or go to the farmhouse for HELP?
    """)
    storystate = fix_or_help
    while storystate != END:
        player_input = input(": ")
        player_next, storystate = storystate(player_input)
        print(player_next)
