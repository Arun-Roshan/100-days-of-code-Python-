# treasure hunt game

print('''
     **     *******   **     ** ****     **   *******     *******    ******** **      **     **     ****     **
    ****   /**////** /**    /**/**/**   /**  /**////**   **/////**  **////// /**     /**    ****   /**/**   /**
   **//**  /**   /** /**    /**/**//**  /**  /**   /**  **     //**/**       /**     /**   **//**  /**//**  /**
  **  //** /*******  /**    /**/** //** /**  /*******  /**      /**/*********/**********  **  //** /** //** /**
 **********/**///**  /**    /**/**  //**/**  /**///**  /**      /**////////**/**//////** **********/**  //**/**
/**//////**/**  //** /**    /**/**   //****  /**  //** //**     **        /**/**     /**/**//////**/**   //****
/**     /**/**   //**//******* /**    //***  /**   //** //*******   ******** /**     /**/**     /**/**    //***
//      // //     //  ///////  //      ///   //     //   ///////   ////////  //      // //      // //      /// 
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
choice1 = input("you\'re at a crossroad, where do you want to go? Type left or right :- ").lower()
if choice1 == "left":
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. Type 'wait' for wait for "
                    "the boat or "
                    "Type 'swim' to swim across.")
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. there is a house with 3 doors 'red, yellow and blue' "
                        "which one do u choose?\n")
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        if choice3 == "yellow":
            print("You found the treasure. You win!")
            print('''
              .-=========-.
               |'-=======|
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\
            ''')
        if choice3 == "red":
            print("It's a room full of lion. Game Over.")
    else:
        print("You got attacked by angry trout. Game Over.")
elif choice1 == "right":
    print("You fell into a hole. Game Over.")
    
