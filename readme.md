Another reddit project 
---------------------------

Background

Since we're all redditors here, let's make something dealing with reddit. If you go to a user's profile and add .json to the end of it, you can get the all sorts of Json data about the user (think of Json as a giant dictionary of smaller dictionaries and lists). For example, if I go to my own profile and view it's Json data, it would look like this. At first it might look intimidating, but if you break it down, you can see it's just one giant dictionary with all sorts of information about my latest posts.

Goal

Create a program that gets information about two different users, and then sees whose most recent post received the most karma. The program should then print out which user received more karma, and what the difference was. This is a pretty open project, so I encourage you to take it further by adding more features if you find it interesting.

Remember - Elements in a list are referenced by their index numbers while entries in a dictionary are referenced by their keys.

Subgoals

    Allow the user to put in the name of two different users when the program first begins.

    If one of the names of the users does not exist (because of a spelling error), print out a message saying so.

    Allow the user to keep comparing other users until the program is closed.

    Display the amount of upvotes and downvotes each user received for their posts.

Not sure how to turn json data into usable python data? Check this out.

