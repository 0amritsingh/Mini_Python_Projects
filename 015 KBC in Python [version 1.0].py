# KBC in Python [version 1.0] # With a Special Feature :D 

# Quesitons from index 0 to 9
questions = [
       "\nQuestion: Which of the following corresponds to ‘ek bataa do’?\n(1) Pura\n(2) Saw\n(3) Adha\n(4) Pauna",

       "\nQuestion: Which of the following gods is also known as ‘Gauri Nandan’?\n(5) Agni\n(6) Indra\n(7) Hanuman\n(8) Ganesha",

       "\nQuestion: In the game of ludo the discs or tokens are of how many colours?\n(9) One\n(10) Two\n(11) Three\n(12) Four",

       "\nQuestion: Which of these are names of national parks located in Madhya Pradesh?\n(13) Krishna and Kanhaiya\n(14) Kanha and Madhav\n(15) Ghanshyam and Murari\n(16) Girdhar and Gopal",

       "\nQuestion: Where was the BRICS summit held in 2014?\n(17) Brazil\n(18) India\n(19) Russia\n(20) China",

       "\nQuestion: Who wrote the introduction to the English translation of Rabindranath Tagore’s Gitanjali?\n(21) P.B. Shelley\n(22) Alfred Tennyson\n(23) W.B. Yeats\n(24) T.S. Elliot",

       "\nQuestion: Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving two girls from drowning?\n(25) Anandiben Patel\n(26) Vasundhara Raje Scindia\n(27) Uma Bharti\n(28) Mamata Banerjee",

       "\nQuestion: The wife of which of these famous sports persons was once captain of Indian volleyball team?\n(29) K.D.Jadav\n(30) Dhyan Chand\n(31) Prakash Padukone\n(32) Milkha Singh",

       "\nQuestion: Which of these sports requires you to shout out a word loudly during play?\n(33) Ludo\n(34) Kho-kho\n(35) Playing cards\n(36) Chess",

       "\nQuestion: Which of these terms can only be used for women?\n(37) Dirghaayu\n(38) Suhagan\n(39) Chiranjeevi\n(40) Sushil"
] 

# Answers from index 0 to 9
answers = [3,8,12,14,17,23,25,32,34,38,
           
1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

# Money form index 0 to 9
prize_money = ["$1" ,"$10" ,"$100" ,"$1K" ,"$10K", "$50K" ,"$100K" ,"$1M" ,"$5M" ,"$10M"]

print("\nWelcome to Kaun Banega Carorpati\nYou have to answer Ten Question by typing the correct option\nThe Prize Money is of 10 Million Dollors\nGood Luck!")
print("\nFirst Question is for", prize_money[0])

for i in range(0, 10):
       print(questions[i])
       
       user_input = str(input("\nChoose Option: "))
       
       if user_input == "showme": # The Cheat Code
              print(answers[0:10])
              continue
       
       if questions.index(questions[i]) == answers.index(int(user_input)):
              print("\nOption", user_input, "is a 'CORRECT ANSWER'\n\nNext Question for", prize_money[i+1])
              
       elif questions.index(questions[i]) != answers.index(int(user_input)):
              print("\nOption", user_input, "is a 'WRONG ANSWER'\nYou won", prize_money[i])
              break
              