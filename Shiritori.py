# Viktigt! länkarna till csv filer funkar inte eftersom det ligger i en ny fil, filerna finns men är inte länkade till.
import csv
from random import randrange
global used_words
used_words = []
global words_to_csv
words_to_csv = []
global last_played
last_played = ""
global still_play
still_play = 0
global abc_array
abc_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def reader(place):#Funktion som tar in en integer och returnar strängen som står på det inputets indexet i en csv fil.
    with open("C:/Users/isami.okamotogustaf/Documents/Tillämpad Programeing/Shiritori/list.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        hold = rows[place]
        output = hold[0]
        output = output.lower()
    return(output)

def rows(): #Räknar antalet rader i en csv fil och returnar antalet rader.
    file = open("C:/Users/isami.okamotogustaf/Documents/Tillämpad Programeing/Shiritori/list.csv")
    numline = len(file.readlines())
    global nbr_rows
    nbr_rows = numline
    return(numline)
global nbr_rows
nbr_rows = rows()

def recount(): #En funktion som kollar när första bokstven ändras i en lista soterad efter första bokstaven och skickar tillbaka en array med indexarna där första bokstaven ändras. Funktionen funkar inte om det bara finns ett ord på en bokstav.
    i = 0
    n = 0
    outwrite = []
    with open("C:/Users/isami.okamotogustaf/Documents/Tillämpad Programeing/Shiritori/list.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row = list(csv_reader)
        while i < 26:
            if n == 0:
                outwrite.append(n)
            else:
                outwrite.append(n - 1)
            if len(outwrite) == 26:
                return outwrite
            first_hold = row[n]
            hold = first_hold[0].lower()
            j = 0
            while j < 1:
                compare_one = row[n]
                compare = compare_one[0].lower()
                if hold[0] != compare[0]:
                    j += 1
                n += 1
            i += 1

def rewrite_row(arr): #Tar in en array som input och skriver över det som finns i en csv fil med arrayen.
    with open("C:/Users/isami.okamotogustaf/Documents/Tillämpad Programeing/Shiritori/alphabet_count.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(arr)

def add_to_csv(word): #Frågar om ordet ska läggas till i en csv fil, returnar en bolean beroende på input från användaren. Ps lägger inte till ordet utan sparar ordet om svaret är jag i en array.
    print ("The word does not exist in our libaray but would you like to add it to the library? If yes just type yes, otherwise type anything else.")
    question = input("Answer: ")
    if question.lower() == "yes":
        words_to_csv.append(word)
        return True
    return False

def is_used(word): #Kollar om inputen finns i en array, returnar en boolean där false är om inputen finns i arrayen och true om den inte finns.
    i = 0
    while i < len(used_words):
        if used_words[i] == word:
            n = str(i + 1)
            print ("The word is already used, it was used on turn " + n)
            return False
        i += 1
    return True

def is_used_ai(word): #Kollar om inputen finns i en array, returnar en boolean där false är om inputen finns i arrayen och true om den inte finns.
    i = 0
    while i < len(used_words):
        if used_words[i] == word:
            return False
        i += 1
    return True

def last_word(input): #Tar en sträng som input och kollar om index noll på inputen är samma som sista indexet på en annan sträng. Returnar en boolean där true är om det stämmer annars false.
    if input[0] == last_played[len(last_played) - 1]:
        return True
    return False

def which_letter_index(letter): #Tar in en bokstav som input och kollar på vilket index bokstaven finns på i en array som går a till z och returnar indexet.
    i = 0
    while i < len(abc_array):
        if letter == abc_array[i]:
            return i
        i += 1

def where_letter_start(i): #Tar in en integer som input och returnar det som finns på indexet i en array. Kan inte ta in en input som är större än 25.
    with open("C:/Users/isami.okamotogustaf/Documents/Tillämpad Programeing/Shiritori/alphabet_count.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        arr = rows[0]
        output = arr[i]
        output = int(output)
        return output

def where_letter_end(i): #Tar in en integer som input och skickar tillbaka det som finns på indexet ett över inputen, om inputen är 25 så skickar den istället tillbaka det sista indexet på en annan lista. Kan inte ta in en input som är större än 25.
    with open("C:/Users/isami.okamotogustaf/Documents/Tillämpad Programeing/Shiritori/alphabet_count.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        arr = rows[0]
        if i == 25:
            output = nbr_rows
            output = int(output)
            output -= 1
            return output
        output = arr[i + 1]
        output = int(output)
        output -= 1
        return output

def ai_lose(a): #Tar in en sträng och kollar om antalet strängar som börjar på den bokstaven är samma antal som har andvänts (antal som finns i arrayen used_words som sparar alla använda ord) om antalet ord som har använts på bokstaven är lika många som antal ord på den bokstaven i csv returnar funktionen false, annars true.
    a1 = which_letter_index(a)
    i1 = where_letter_start(a1)
    i2 = where_letter_end(a1)
    hold = i2 - i1
    i = 0
    n = 0
    while i < len(used_words):
        if used_words[i][0] == a:
            n += 1
        if n == hold:
            global still_play
            still_play = 2
            return False
        i += 1
    return True

def word_exists(input): #Tar in en sträng som input som den sedan kollar om den finns i en viss del av en csv fil. Den delen av csv filen som den kollar på får den genom att genom en funktion som tar in första bokstaven i ordet och returnar en siffra beroende på ordet som den sedan skickar in i två funktioner som returnar var sitt index som funktion sedan kollar mellan efter en sträng som är lika dan som inputet, om funktionen hittar en sträng som matchar returnar den true. Annars går den in i en if sats med en funktion som statement och om funktionen returnar true returnar funktionen också true annars returnar funktionen false. 
    a = which_letter_index(input[0])
    i1 = where_letter_start(a)
    i2 = where_letter_end(a)
    with open("C:/Users/isami.okamotogustaf/Documents/Tillämpad Programeing/Shiritori/list.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        while i1 < i2:
            if input == rows[i1][0].lower():
                return True
            i1 += 1
        if add_to_csv(input):
            return True
        return False

def valied_word(input): #En funktion som tar in en sträng som input och skickar in strängen i tre funktioner som  returnar en boolean och om alla tre är true returnar funktionen true annars returnar den false.
    if last_word(input): 
        if is_used(input):
            if word_exists(input):
                used_words.append(input)
                print ("Valied word")
                print ("")
                global last_played
                last_played = input
                return True
    else:
        print ("First letter does not match the last one")
    global still_play
    still_play = 1
    return False

def valied_word_ai(input): #Tar in en sträng som input och skickar in den i två funktioner som returnar en boolean och om båda skickar tillbaks true skickar funktionen också tillbaka true, annars skickar funktionen tillbaka false. 
    if is_used_ai(input) & last_word(input):
        used_words.append(input)
        global last_played
        last_played = input
        return True
    return False

def ai_select_word(): #Börjar med att spara den sista bokstaven från en sträng som en variabel och går in i en if stats med en funktion som statement som returnar en boolean och tar variablen som input. Om funktionen returnar true skickar in variablen i en funktion returnar en siffra beroende på bokstaven. Med siffran skickar funktionen sedan in den i två funktioner som returnar index platser i en csv fil. Sedan går det in i en while loop där en siffra slumpas mellan de två indexn från tidigare hjälpfunktioner som skickas in i en hjälpfunktion som returnar en sträng på de index som blev framslumpad. Strängen skickas in i en funktion som returnar en boolean och loopen tar slut om hjälpfunktionen returnar true och funktionen returnar strängen. Om funtktionen returnar false returnar funktionen en tom sträng.
    a = last_played[len(last_played) - 1]
    if ai_lose(a):
        n = which_letter_index(a)
        i1 = where_letter_start(n)
        i2 = where_letter_end(n)
        i = 0
        while i < 1:
            word = reader(randrange(i1, i2))
            if valied_word_ai(word):
                i += 1
        return word
    else:
        return ""

def user_word(): #Frågar efter ett input från user och skickar in det efter lowercase in i en hjälpfunktion som är en statement till en if sats, funktionen returnar en boolean. Om hjälpfunktionen returnar true returnar funktionen user inputen.lower(), annars returnar funktionen false.
    word = input("Your word: ")
    word = word.lower()
    if valied_word(word):
        return word
    return False

def main(): #Main funktionen. Funktionen börjar med att välja en bokstav mellan a - z genom att slumpa en siffra som sedan blir indexet för en bokstav i en array. Sedan börjar spelet med spelaren som för börja. Spelet går ut på att svara med ett engelskt substantiv som börjar med den bokstav som det senaste ordet slutade på. I spelet spelar man mot en dator som slumpvis väljer ett giltigt ord. Efter att spelaren har kört en runda går funktionen in i en while loop som håller på tills spelaren svarar fel eller datorn får slut på ord genom att ändra variablen som är vilkåret för loopen. Skriver sedan ut om spelaren förlorade eller van och sedan ut en array om arrayen inte är tom. 
    rewrite_row(recount())
    a = randrange(0, 25)
    global last_played
    last_played = abc_array[a]
    print("The first letter is: " + abc_array[a])
    global still_play
    still_play = 0
    user_word()
    while still_play == 0:
        played = ai_select_word()
        print("Word from computer: " + played)
        if still_play == 0:
            user_word()
    if still_play == 1:
        print("You lose")
    elif still_play == 2:
        print ("You win")
    if len(words_to_csv) != 0:
        print("The words that should be added to the csv file 'list.csv' ", words_to_csv)

main() #Finns vissa saker som skulle kunna optimeras eftersom vissa delar av koden var gjorda för att jobba mer med csv fil men jag hann inte få med allt så vissa saker skulle varit mer efektiva.