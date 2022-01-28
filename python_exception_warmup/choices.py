# Import all the other modules
import jokes
import addition
import happy


class UserOption:
    def __init__(self, text, action):
        self.text = text
        self.action = action


option_one = UserOption("Tell me a joke", jokes.tell_joke)
option_two = UserOption("Let me add a couple numbers", addition.add_nums)
option_three = UserOption("Show me a happy face", happy.print_happy_face)
option_four = UserOption("Leave this place", exit)
# print(option_one.text)
# option_one.action


# Each element of the array is a dictionary
# Each dictionary contains a string that is show to the user and a function that is called if they pick it
# Cool thing here is you can add more options here and they will automatically show up the next time you run the program.
options = [
    option_one,
    option_two,
    option_three,
    option_four

    # {
    #     "string": "Tell me a joke",
    #     "function": jokes.tell_joke
    # },

    # {
    #     "string": "Let me add a couple numbers",
    #     "function": addition.add_nums
    # },

    # {
    #     "string": "Show me a happy face",
    #     "function": happy.print_happy_face
    # },

    # {
    #     "string": "Leave this place",
    #     "function": exit
    # }
]
