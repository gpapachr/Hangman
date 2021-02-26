import random                       #βιβλιοθήκη της Python

def emfanisi(x):
    for i in x:
        print(i, ' ', end="")
    print()

lexiko = ['ΚΡΕΜΑΛΑ','ΑΝΑΚΩΧΗ', 'ΑΝΑΤΟΛΗ', 'ΒΑΡΟΣ', 'ΒΗΧΑΣ', 'ΓΥΝΑΙΚΑ', 'ΓΕΛΙΟ', 'ΔΑΧΤΥΛΙΔΙ', 'ΔΕΝΤΡΟ', 'ΕΠΙΛΟΓΗ', 'ΕΠΙΔΕΣΜΟΣ', 'ΖΑΛΑΔΑ', 'ΖΩΓΡΑΦΙΑ', 'ΗΛΙΟΣ',\
          'ΗΜΙΘΕΟΣ', 'ΘΕΑΤΡΟ', 'ΘΡΗΣΚΕΙΑ', 'ΙΣΟΤΗΤΑ', 'ΙΣΟΠΛΕΥΡΟ','ΚΑΡΕΚΛΑ', 'ΛΑΜΠΡΟΤΗΤΑ', 'ΛΕΟΠΑΡΔΑΛΗ', 'ΜΕΓΑΛΕΙΟ', 'ΜΟΝΟΠΩΛΙΟ', 'ΝΑΥΤΙΑ', 'ΝΟΣΟΚΟΜΕΙΟ', \
          'ΞΙΦΙΑΣ', 'ΞΗΡΑΣΙΑ', 'ΟΡΟΦΟΣ', 'ΟΡΑΣΗ', 'ΠΑΠΟΥΤΣΙ', 'ΠΕΤΡΩΜΑ', 'ΡΑΔΙΟΦΩΝΟ', 'ΡΕΑΛΙΣΜΟΣ', 'ΣΥΚΟΦΑΝΤΙΑ', 'ΣΤΑΧΤΗ', 'ΤΗΛΕΦΩΝΟ', 'ΤΑΧΥΤΗΤΑ', 'ΥΨΩΜΑ', \
          'ΥΠΑΡΞΗ', 'ΦΡΑΓΜΑ', 'ΦΙΛΑΝΘΡΩΠΙΑ', 'ΧΕΛΙΔΟΝΙ', 'ΧΑΜΟΓΕΛΟ', 'ΨΥΓΕΙΟ', 'ΨΑΡΕΜΑ', 'ΩΔΕΙΟ', 'ΩΚΕΑΝΟΣ']

rematch = 1

while rematch == 1:
    players_number = int(input('Αριθμός Παικτών: '))

    players = []
    for i in range(players_number):
        p = input('Όνομα Παίκτη: ')
        players.append(p)
    print('')

    while len(players)>1:
    
        player = 0 #η θέση του ονόματος του τρέχοντος παίκτη στην λίστα players
        players_played = 0 # το πλήθος των παικτών που έχουν παίξει
        players_qualified = [] #λίστα παικτών που προκρίνονται
        new_words = [] # οι λέξεις που έχουν ειπωθεί στον τρέχοντα γύρο
        old_words = [] # οι λέξεις που έχουν ειπωθεί στον προηγούμενο γύρο
        end_this_game = False

    
        while players_played < len(players) and end_this_game == False:
            print('')
            print(players[player],',είναι η σειρά σου!')
            print('Δικαιούσε 5 λάθος επιλογές γραμμάτων. Με το 6o λάθος αποχωρείς από το παιχνίδι. Καλή επιτυχία!!')
            print('')
            print('Ας σκεφτούμε μια λέξη για σένα...')
    
            print('Είμαστε έτοιμοι, ας ξεκινήσουμε!!!')

            lexi = random.choice(lexiko)

          # while lexi in new_words or lexi in old_words:
           #     lexi = random.choice(lexiko) 

            new_words.append(lexi)

            grammata = list(lexi)
            theseis = ['_']*len(lexi)

            emfanisi(theseis)

            not_in_lexi = [] #λίστα με τα γράμματα που καταχωρήθηκαν αλλά δεν υπάρχουν μέσα στη λέξη
            life = 6         
            defeat = False
            win = False

            while defeat == False and win == False:
                gramma = input('Δώσε μου ένα κεφαλαιο ελληνικό γράμμα: ')

                while len(gramma)>1 or len(gramma)==0 or gramma not in 'ΑΒΓΔΕΖΗΘΗΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ' or gramma in not_in_lexi:
                    if len(gramma)>1: 
                        print('Δώσε μου το πολύ ένα κεφαλαίο ελληνικό γράμμα')
                
                    elif len(gramma)==0:
                        print('Δεν μου έδωσες κανένα γράμμα')
                    elif gramma not in 'ΑΒΓΔΕΖΗΘΗΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ':
                        print('Δώσε μου ένα κεφαλαίο ελληνικό γράμμα')
                    elif gramma in not_in_lexi:
                        print('Έχεις ήδη δοκιμάσει αυτό το γράμμα χωρίς επιτυχία...')
                    gramma = input('Προσπάθησε ξανά: ')
                    

        
                if gramma in lexi:
                    while gramma in grammata:
                        thesi = grammata.index(gramma)
                        grammata[thesi] = '_'
                        theseis[thesi] = gramma
                    if '_' not in theseis:
                        win = True
                else:
                    life -= 1
                    if gramma not in not_in_lexi:
                        not_in_lexi += [gramma]
                    if life == 5:
                        print('|---------|')
                        print('|         O')
                        print('|'          )
                        print('|'          )
                        print('|'          )
                        print('|'          )
                        print('|'          )
                    elif life == 4:
                        print('|---------|')
                        print('|         O')
                        print('|        /|\ ')
                        print('|'          )
                        print('|'          )
                        print('|'          )
                        print('|'          )
                    elif life == 3:
                        print('|---------|')
                        print('|         O')
                        print('|        /|\ ')
                        print('|         |')
                        print('|'          )
                        print('|'          )
                        print('|'          )
                    elif life == 2:
                        print('|---------|')
                        print('|         O')
                        print('|        /|\ ')
                        print('|         |')
                        print('|       _/ \_')
                        print('|'          )
                        print('|'          )
                    elif life == 1:
                        print('|---------|')
                        print('|         O')
                        print('|        /|\ ')
                        print('|         |')
                        print('|       _/ \_')
                        print('|      ### ###')
                        print('|'          )
                    elif life == 0:
                        print('|---------|')
                        print('|         O')
                        print('|        /|\ ')
                        print('|         |')
                        print('|       _/ \_')
                        print('|      ### ###')
                        print('         fire')
                    
                              
                    print('Δεν υπάρχει αυτό το γράμμα στην λέξη')
                    print('Έχεις ακόμα: ',life, 'ζωές')
                    print('Τα γράμματα που έχεις δοκιμάσει και δεν υπάρχουν στην λέξη είναι: ', not_in_lexi)
                    if life == 0:
                        defeat = True
        
                emfanisi(theseis)
        
            if defeat==True:
                print('Λυπάμαι, είσαι εκτός παιχνιδιού...Η λέξη που ψάχναμε ήταν:' ,lexi)
            else:
                print('Μπράβο! Η λέξη που ψάχναμε ήταν:',lexi)
                print('Πέρασες στον επόμενο γύρο!')
                players_qualified.append(players[player])
            players_played += 1
            player += 1

        if players_played == len(players):
            if len(players) == 1:
                print('Έχουμε νικητή!!! Συγχαρητήρια', players[0], '!!!')
                end_this_game = True
            elif len(players) == 0:
                print('Δυστυχώς δεν υπήρξε νικητής...καλή τύχη την επόμενη φορά')
                end_this_game = True
            players = players_qualified       
            players_qualified = []
            players_played = 0
            player = 0
            old_words = new_words
            new_words = []
    if len(players) == 1:
        print('Έχουμε νικητή!!! Συγχαρητήρια', players[0], '!!!')
        end_this_game = True
    elif len(players) == 0:
        print('Δυστυχώς δεν υπήρξε νικητής...καλή τύχη την επόμενη φορά')
        end_this_game = True        
    
            
    rematch = int(input('Θέλετε να ξαναπαίξετε;(πληκτρολογήστε 1 αν θέλετε να αρχίσετε νέο παιχνίδι ή 0 αν θέλετε να τερματιστεί η εφαρμογή): '))

print('')
print('^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^')
print('Ανίκητος είναι δύνασαι, εάν εις μηδένα αγώνα καταβαίνης, όν ουκ έστιν επί σοι νικήσαι.')
print('')
print('Τα λέμε την επόμενη φορά!!')


        


