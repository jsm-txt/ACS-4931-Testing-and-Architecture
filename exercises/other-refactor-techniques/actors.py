# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

# def send_hiring_email(email):
#     print("email sent to: ", email)
    
# for i, value in enumerate(emails):
#     if birth_year[i] > 1985:
#         print(first_names[i], last_names[i])
#         print('Movies Played: ', end='')
#         for m in movies[i]:
#             print(m, end=', ')
#         print()
#         send_hiring_email(value)

class Actor:
    def __init__(self, first_name, last_name,birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def send_hiring_email(self, email):
        print("email sent to: ", email)
    
for i, value in enumerate( emails):
    if birth_year[i] > 1985:
        print(first_names[i], last_names[i])
        print('Movies Played: ', end='')
        for m in movies[i]:
            print(m, end=', ')
        print()
        Actor(first_names[i], last_names[i], birth_year[i]).send_hiring_email(value)