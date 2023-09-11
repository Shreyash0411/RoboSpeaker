import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 : made by Shreyash")
    engine = pyttsx3.init();
    while True:
        x = input("enter what you want me to pronounce : ")
        if x == "q":
            engine.say("bye bye friend");
            engine.runAndWait();
            break;

        engine.say(x);
        engine.runAndWait();