def vigenere_encrypt(plaintext, key):
    # Δημιουργούμε μια λίστα για να αποθηκεύσουμε το κρυπτογραφημένο κείμενο.
    ciphertext = []
    # Υπολογίζουμε το μήκος του κλειδιού.
    key_length = len(key)
    # Αρχικοποιούμε τον δείκτη του κλειδιού στη θέση 0.
    key_index = 0

    # Για κάθε χαρακτήρα στο αρχικό κείμενο (plaintext):
    for char in plaintext:
        # Ελέγχουμε αν ο χαρακτήρας είναι γράμμα (αποφεύγουμε τους αριθμούς και σύμβολα).
        if char.isalpha():
            # Υπολογίζουμε τη μετατόπιση (shift) για τον αντίστοιχο χαρακτήρα του κλειδιού.
            shift = ord(key[key_index].lower()) - ord('a')
            # Αν ο χαρακτήρας είναι πεζός (lowercase):
            if char.islower():
                # Προσθέτουμε τον κρυπτογραφημένο πεζό χαρακτήρα στη λίστα ciphertext.
                ciphertext.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                # Προσθέτουμε τον κρυπτογραφημένο κεφαλαίο χαρακτήρα στη λίστα ciphertext.
                ciphertext.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            # Αλλάζουμε τον δείκτη του κλειδιού (key_index) ώστε να δείχνει στον επόμενο χαρακτήρα του κλειδιού.
            key_index = (key_index + 1) % key_length
        else:
            # Αν ο χαρακτήρας δεν είναι γράμμα, τον προσθέτουμε κατευθείαν στο ciphertext χωρίς αλλαγή.
            ciphertext.append(char)

    # Επιστρέφουμε το κρυπτογραφημένο κείμενο ως ενιαία συμβολοσειρά.
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    # Δημιουργούμε μια λίστα για να αποθηκεύσουμε το αποκρυπτογραφημένο κείμενο.
    plaintext = []
    # Υπολογίζουμε το μήκος του κλειδιού.
    key_length = len(key)
    # Αρχικοποιούμε τον δείκτη του κλειδιού στη θέση 0.
    key_index = 0

    # Για κάθε χαρακτήρα στο κρυπτογραφημένο κείμενο (ciphertext):
    for char in ciphertext:
        # Ελέγχουμε αν ο χαρακτήρας είναι γράμμα.
        if char.isalpha():
            # Υπολογίζουμε τη μετατόπιση (shift) για τον αντίστοιχο χαρακτήρα του κλειδιού.
            shift = ord(key[key_index].lower()) - ord('a')
            # Αν ο χαρακτήρας είναι πεζός (lowercase):
            if char.islower():
                # Προσθέτουμε τον αποκρυπτογραφημένο πεζό χαρακτήρα στη λίστα plaintext.
                plaintext.append(chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a')))
            else:
                # Προσθέτουμε τον αποκρυπτογραφημένο κεφαλαίο χαρακτήρα στη λίστα plaintext.
                plaintext.append(chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A')))
            # Αλλάζουμε τον δείκτη του κλειδιού για τον επόμενο χαρακτήρα.
            key_index = (key_index + 1) % key_length
        else:
            # Αν ο χαρακτήρας δεν είναι γράμμα, τον προσθέτουμε κατευθείαν στο plaintext χωρίς αλλαγή.
            plaintext.append(char)

    # Επιστρέφουμε το αποκρυπτογραφημένο κείμενο ως ενιαία συμβολοσειρά.
    return ''.join(plaintext)

# Ζητάμε από τον χρήστη να επιλέξει αν θέλει να κρυπτογραφήσει ή να αποκρυπτογραφήσει.
choice = input("Type encrypt or decrypt: ").strip().lower()
# Λαμβάνουμε το κείμενο που θα χρησιμοποιηθεί.
text = input("Enter your text: ")
# Λαμβάνουμε το κλειδί που θα χρησιμοποιηθεί για την κρυπτογράφηση ή αποκρυπτογράφηση.
key = input("Enter your key: ")

# Αν η επιλογή είναι "encrypt", κρυπτογραφούμε το κείμενο.
if choice == 'encrypt':
    result = vigenere_encrypt(text, key)
    print("Encrypted text:", result)
# Αν η επιλογή είναι "decrypt", αποκρυπτογραφούμε το κείμενο.
elif choice == 'decrypt':
    result = vigenere_decrypt(text, key)
    print("Decrypted text:", result)
# Αν η επιλογή δεν είναι καμία από τις δύο, εμφανίζουμε μήνυμα λάθους.
else:
    print("Invalid choice.")