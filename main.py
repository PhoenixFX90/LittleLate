answer = input("This is a short crime text-based game. In this game you are a play as rookie detective following leads on the hunt for a known serial killer.." 
               "Accompanied by your long time partner Det. Gray, you encounter strange people and places."
                "Would you like to play? (yes/no)")
if answer.lower().strip() == "yes":
    answer = input("You drive to a fork in the road. Do you go left, right or forward?").lower().strip()
    if answer == "left":
        answer = input("As you are driving down a poorly lit, paved road, and suddenly Det. Gray notices a person slumped over against an old fuel pump."
                       "He tells you to stop the car."
                       "Do you stop the car or keep driving?")
        
        if answer == "stop":
            answer = input("Your partner helps the man into the squad car. He victim states he was attacked by a tall husky man."
                           "He is bleeding from his eyebrow and covered in scratches."
                           "He asks you to drive him to a hospital. But you need more information from the victim."
                           "Do you drive him to the hospital or police station?")
            if answer == "hospital":
                print("The victim is very grateful and agrees to answer all your questions at the hospital.")
            
            elif answer:
                print("The victim takes a turn for the worst and dies on the way to the police station. Game Over.")
        else:
            print("You ignore your partner and suddenly the car gets a flat tire. Not prepared, you and your partner are stranded."
                  "Attacked by surprise, you are both brutually murdered in the sqaud car."
                  "The Killer has struck again!")
            
    if answer == "right":
        answer = input("It's very late and you guys have been driving for several hours. Your partner lets out a loud yawn."
                       "You see a sign for a hotel and coffee shop. Do you stop for the hotel or coffee?")
        if answer == "hotel":
            print("Det. Gray gets the two of you checked into the hotel room while you take the luggage from the car to the hotel room."
                  "As your partner settles in, you decide to look over the casefile before heading to the shower."
                  "Gray makes a comment about the drive into town."
                  "You decide to shower, as you are in the shower you put two and two together about what you just looked over and what Det. Gray said about the drive in.")
        else:
            print("You stop for coffee and continue the search, driving on into the night.")
    
    elif answer == "forward":
        answer = input("Driving forward you hear dispatch radio in, 'We have 10-31 half a mile out patrol 110-7'"
                       "You are on the right path to catching the serial killer. You hit the lights and step on the gas. The chase is on!")
else:
    print("GoodBye")
