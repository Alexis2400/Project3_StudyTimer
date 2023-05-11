import time
import random
import subprocess

# List of study and break messages that the user will see
study_messages = ["Keep up the good work!", "Stay focused and determined!", "Believe in yourself and your abilities!",
                  "You're making progress, keep going!", "Take it one step at a time.", "Success is within your reach!",
                  "Stay committed and dedicated!", "You've got this!", "Believe in the power of your dreams.",
                  "Effort and perseverance will pay off!"]
break_messages = ["Take a few deep breaths and relax your mind.", "Stretch your body and take a short walk.",
                  "Get a healthy snack and rehydrate.", "Listen to your favorite song.", "Call a friend and catch up.",
                  "Take a power nap to recharge.", "Do a quick workout or yoga session.", "Meditate to clear your mind.",
                  "Take a moment to appreciate your progress.", "Visualize your success and stay motivated."]

def study_timer():
    #this is the Function to start the study timer for a given amount of time with the corresponding break time that the user inputs"""
    total_study_time = int(input("Enter total study time (in minutes): "))
    break_time = int(input("Enter break time (in minutes): "))
    study_message = random.choice(study_messages)
    break_message = random.choice(break_messages)
    start_time = time.time()
    # This turns the tudy time to seconds
    end_time = start_time + total_study_time * 60  
    study_count = 1
    while time.time() < end_time:
        print(f'Study session {study_count}: {study_message}')
        # waits for the study time
        time.sleep(total_study_time * 60)  
        print(f'Break {study_count}: {break_message}')
        # waits for the break time
        time.sleep(break_time * 60)  
        study_count += 1
        # randomizes a study message to the user
        study_message = random.choice(study_messages) 
        # randomizes a break message to the user
        break_message = random.choice(break_messages)  
    print('Great job, you finished your study session!')
     # uses the 'say' command to output an audio message when the timer is up
    subprocess.run(['say', 'Your study session has been completed!']) 

    # ask the user if they want to start another study session
    restart = input("Would you like to start another study session? (yes or no): ")
    if restart.lower() == "yes":
        study_timer()
    else:
        print("You did great in todays study session! Take care and until next time!")

study_timer()
