import random

data = [
    {"name": "Cristiano Ronaldo", "followers": 680, "description": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 518, "description": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 403, "description": "Singer and actress", "country": "United States"},
    {"name": "Kylie Jenner", "followers": 381, "description": "Businesswoman and media personality", "country": "United States"},
    {"name": "Dwayne Johnson", "followers": 381, "description": "Actor and wrestler", "country": "United States"},
    {"name": "Ariana Grande", "followers": 362, "description": "Singer and actress", "country": "United States"},
    {"name": "Kim Kardashian", "followers": 344, "description": "Media personality and entrepreneur", "country": "United States"},
    {"name": "Beyonce", "followers": 299, "description": "Singer and songwriter", "country": "United States"},
    {"name": "Khloe Kardashian", "followers": 291, "description": "Media personality", "country": "United States"},
    {"name": "Kendall Jenner", "followers": 284, "description": "Model", "country": "United States"},
    {"name": "Justin Bieber", "followers": 292, "description": "Singer", "country": "Canada"},
    {"name": "Taylor Swift", "followers": 281, "description": "Singer and songwriter", "country": "United States"},
    {"name": "Virat Kohli", "followers": 275, "description": "Cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "followers": 249, "description": "Singer and actress", "country": "United States"},
    {"name": "Neymar Jr", "followers": 231, "description": "Footballer", "country": "Brazil"},
    {"name": "Nicki Minaj", "followers": 225, "description": "Rapper", "country": "Trinidad and Tobago"},
    {"name": "Kourtney Kardashian", "followers": 220, "description": "Media personality", "country": "United States"},
    {"name": "Miley Cyrus", "followers": 212, "description": "Singer and actress", "country": "United States"},
    {"name": "Katy Perry", "followers": 203, "description": "Singer and songwriter", "country": "United States"},
    {"name": "Zendaya", "followers": 180, "description": "Actress and singer", "country": "United States"},
    {"name": "Kevin Hart", "followers": 178, "description": "Comedian and actor", "country": "United States"},
    {"name": "Cardi B", "followers": 164, "description": "Rapper", "country": "United States"},
    {"name": "LeBron James", "followers": 159, "description": "Basketball player", "country": "United States"},
    {"name": "Rihanna", "followers": 149, "description": "Singer and entrepreneur", "country": "Barbados"},
    {"name": "Drake", "followers": 140, "description": "Rapper and singer", "country": "Canada"},
    {"name": "Chris Brown", "followers": 139, "description": "Singer and dancer", "country": "United States"},
    {"name": "Eminem", "followers": 52, "description": "Rapper", "country": "United States"},
    {"name": "Billie Eilish", "followers": 125, "description": "Singer and songwriter", "country": "United States"},
    {"name": "Shakira", "followers": 95, "description": "Singer and songwriter", "country": "Colombia"},
    {"name": "David Beckham", "followers": 88, "description": "Former footballer", "country": "United Kingdom"},
    {"name": "Priyanka Chopra", "followers": 93, "description": "Actress and producer", "country": "India"},
    {"name": "Deepika Padukone", "followers": 80, "description": "Actress", "country": "India"},
    {"name": "Alia Bhatt", "followers": 86, "description": "Actress", "country": "India"},
    {"name": "Shraddha Kapoor", "followers": 94, "description": "Actress and singer", "country": "India"},
    {"name": "Katrina Kaif", "followers": 80, "description": "Actress and entrepreneur", "country": "India"},
    {"name": "Salman Khan", "followers": 70, "description": "Actor and producer", "country": "India"},
    {"name": "Shah Rukh Khan", "followers": 49, "description": "Actor and producer", "country": "India"},
    {"name": "Akshay Kumar", "followers": 68, "description": "Actor and producer", "country": "India"},
    {"name": "Anushka Sharma", "followers": 68, "description": "Actress and producer", "country": "India"},
    {"name": "Narendra Modi", "followers": 100, "description": "Politician", "country": "India"},
    {"name": "Rashmika Mandanna", "followers": 45, "description": "Actress", "country": "India"},
    {"name": "MS Dhoni", "followers": 50, "description": "Former cricketer", "country": "India"},
    {"name": "Rohit Sharma", "followers": 43, "description": "Cricketer", "country": "India"},
    {"name": "Hardik Pandya", "followers": 40, "description": "Cricketer", "country": "India"},
    {"name": "Jisoo", "followers": 79, "description": "Singer and actress", "country": "South Korea"},
    {"name": "Jennie", "followers": 87, "description": "Singer and rapper", "country": "South Korea"},
    {"name": "Lisa", "followers": 106, "description": "Singer and dancer", "country": "Thailand"},
    {"name": "Rosé", "followers": 80, "description": "Singer and songwriter", "country": "New Zealand"},
    {"name": "V", "followers": 68, "description": "Singer and BTS member", "country": "South Korea"},
    {"name": "Jungkook", "followers": 57, "description": "Singer and BTS member", "country": "South Korea"},
    {"name": "RM", "followers": 45, "description": "Rapper and songwriter", "country": "South Korea"},
    {"name": "IU", "followers": 33, "description": "Singer and actress", "country": "South Korea"},
    {"name": "Jackie Chan", "followers": 5, "description": "Actor and martial artist", "country": "Hong Kong"},
    {"name": "Zhao Lusi", "followers": 10, "description": "Actress", "country": "China"},
    {"name": "Dilraba Dilmurat", "followers": 10, "description": "Actress and model", "country": "China"},
    {"name": "Wang Yibo", "followers": 5, "description": "Actor and singer", "country": "China"},
    {"name": "Huda Kattan", "followers": 54, "description": "Beauty entrepreneur", "country": "United States"},
    {"name": "Nusret Gokce", "followers": 53, "description": "Chef and restaurateur", "country": "Turkey"},
    {"name": "Burak Ozdemir", "followers": 50, "description": "Chef and restaurateur", "country": "Turkey"},
    {"name": "Mohamed Salah", "followers": 66, "description": "Footballer", "country": "Egypt"},
    {"name": "Karim Benzema", "followers": 76, "description": "Footballer", "country": "France"},
    {"name": "Kylian Mbappe", "followers": 130, "description": "Footballer", "country": "France"},
    {"name": "Erling Haaland", "followers": 40, "description": "Footballer", "country": "Norway"},
    {"name": "Vinicius Junior", "followers": 55, "description": "Footballer", "country": "Brazil"},
    {"name": "Luka Modric", "followers": 38, "description": "Footballer", "country": "Croatia"},
    {"name": "Sergio Ramos", "followers": 66, "description": "Footballer", "country": "Spain"},
    {"name": "Gerard Pique", "followers": 23, "description": "Former footballer", "country": "Spain"},
    {"name": "Zlatan Ibrahimovic", "followers": 64, "description": "Former footballer", "country": "Sweden"},
    {"name": "Paul Pogba", "followers": 63, "description": "Footballer", "country": "France"},
    {"name": "Antoine Griezmann", "followers": 41, "description": "Footballer", "country": "France"},
    {"name": "David Warner", "followers": 11, "description": "Cricketer", "country": "Australia"},
    {"name": "Babar Azam", "followers": 6, "description": "Cricketer", "country": "Pakistan"},
    {"name": "Shaheen Afridi", "followers": 5, "description": "Cricketer", "country": "Pakistan"},
    {"name": "Fakhar Zaman", "followers": 3, "description": "Cricketer", "country": "Pakistan"},
    {"name": "Atif Aslam", "followers": 9, "description": "Singer", "country": "Pakistan"},
    {"name": "Mahira Khan", "followers": 11, "description": "Actress", "country": "Pakistan"},
    {"name": "Hania Aamir", "followers": 19, "description": "Actress", "country": "Pakistan"},
    {"name": "Ayeza Khan", "followers": 14, "description": "Actress and model", "country": "Pakistan"},
    {"name": "Sajal Aly", "followers": 10, "description": "Actress", "country": "Pakistan"},
    {"name": "Fahad Mustafa", "followers": 5, "description": "Actor and television host", "country": "Pakistan"},
    {"name": "Imran Khan", "followers": 10, "description": "Former cricketer and politician", "country": "Pakistan"},
    {"name": "Zach King", "followers": 30, "description": "Digital creator and filmmaker", "country": "United States"},
    {"name": "Charli D'Amelio", "followers": 42, "description": "Dancer and content creator", "country": "United States"},
    {"name": "Addison Rae", "followers": 35, "description": "Actress and content creator", "country": "United States"},
    {"name": "Khaby Lame", "followers": 80, "description": "Content creator", "country": "Italy"},
    {"name": "MrBeast", "followers": 70, "description": "YouTuber and entrepreneur", "country": "United States"},
    {"name": "Logan Paul", "followers": 27, "description": "Content creator and wrestler", "country": "United States"},
    {"name": "Jake Paul", "followers": 28, "description": "Content creator and boxer", "country": "United States"},
    {"name": "Emma Watson", "followers": 72, "description": "Actress and activist", "country": "United Kingdom"},
    {"name": "Tom Holland", "followers": 65, "description": "Actor", "country": "United Kingdom"},
    {"name": "Will Smith", "followers": 68, "description": "Actor and musician", "country": "United States"},
    {"name": "Robert Downey Jr", "followers": 58, "description": "Actor", "country": "United States"},
    {"name": "Millie Bobby Brown", "followers": 63, "description": "Actress and entrepreneur", "country": "United Kingdom"},
    {"name": "Gal Gadot", "followers": 108, "description": "Actress and model", "country": "Israel"},
    {"name": "Shawn Mendes", "followers": 73, "description": "Singer and songwriter", "country": "Canada"},
    {"name": "Camila Cabello", "followers": 65, "description": "Singer and songwriter", "country": "Cuba"},
    {"name": "Lalisa Manobal", "followers": 106, "description": "Singer and dancer", "country": "Thailand"},
    {"name": "Bad Bunny", "followers": 50, "description": "Rapper and singer", "country": "Puerto Rico"},
    {"name": "J Balvin", "followers": 51, "description": "Singer and rapper", "country": "Colombia"},
    {"name": "Maluma", "followers": 64, "description": "Singer and songwriter", "country": "Colombia"},
    {"name": "Anitta", "followers": 64, "description": "Singer and performer", "country": "Brazil"},
    {"name": "Lalisa Manobal", "followers": 106, "description": "Singer and dancer", "country": "Thailand"},
]

person_A = random.choice(data)
person_B = random.choice(data)

is_game_over = False
score = 0

while not is_game_over:
    print(f"Compare A: {person_A["name"]}, a {person_A["description"]}, from {person_A["country"]}")
    print(f"Against B: {person_B["name"]}, a {person_B["description"]}, from {person_B["country"]}")

    if person_A["followers"] > person_B["followers"]:
        answer = "a"
    elif person_B["followers"] > person_A["followers"]:
        answer = "b"

    if input("Who has more followers? Type 'A' or 'B': ").lower() == answer:
        score += 1
        print(f"You're right! Current score: {score}")
        if person_B["followers"] > person_A["followers"]:
            person_A = person_B
        person_B = random.choice(data)
    else:
        print("That's wrong! You Lose.")
        print(f"Final score: {score}")
        is_game_over = True