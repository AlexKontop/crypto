# Συνάρτηση για κρυπτογράφηση κειμένου με χρήση του αλγορίθμου Affine Cipher
def encrypt(text, a, b):
    encrypted = ""  # Αρχικοποίηση κενής συμβολοσειράς για το κρυπτογραφημένο κείμενο
    for char in text:  # Για κάθε χαρακτήρα στο κείμενο που δόθηκε
        if char.isalpha():  # Έλεγχος αν ο χαρακτήρας είναι γράμμα (αλφαβητικός)
            # Υπολογισμός της "μετατόπισης" ανάλογα με το αν ο χαρακτήρας είναι κεφαλαίος ή πεζός
            shift = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            # Προσθήκη του κρυπτογραφημένου χαρακτήρα στην κρυπτογραφημένη συμβολοσειρά
            encrypted += chr((a * shift + b) % 26 + ord('A')) if char.isupper() else chr((a * shift + b) % 26 + ord('a'))
        else:
            encrypted += char  # Αν δεν είναι γράμμα, προσθέτουμε τον αρχικό χαρακτήρα όπως είναι
    return encrypted  # Επιστρέφουμε το κρυπτογραφημένο κείμενο

# Συνάρτηση για αποκρυπτογράφηση κειμένου με χρήση του αλγορίθμου Affine Cipher
def decrypt(text, a, b):
    decrypted = ""  # Αρχικοποίηση κενής συμβολοσειράς για το αποκρυπτογραφημένο κείμενο
    a_inv = pow(a, -1, 26)  # Υπολογισμός της αντίστροφης του a στο πεδίο mod 26
    for char in text:  # Για κάθε χαρακτήρα στο κείμενο που δόθηκε
        if char.isalpha():  # Έλεγχος αν ο χαρακτήρας είναι γράμμα
            # Υπολογισμός της "μετατόπισης" ανάλογα με το αν ο χαρακτήρας είναι κεφαλαίος ή πεζός
            shift = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')
            # Προσθήκη του αποκρυπτογραφημένου χαρακτήρα στην αποκρυπτογραφημένη συμβολοσειρά
            decrypted += chr((a_inv * (shift - b)) % 26 + ord('A')) if char.isupper() else chr((a_inv * (shift - b)) % 26 + ord('a'))
        else:
            decrypted += char  # Αν δεν είναι γράμμα, προσθέτουμε τον αρχικό χαρακτήρα όπως είναι
    return decrypted  # Επιστρέφουμε το αποκρυπτογραφημένο κείμενο

# Ζητάμε από τον χρήστη να επιλέξει αν θέλει κρυπτογράφηση ή αποκρυπτογράφηση
choice = input("Do you want to encrypt or decrypt? ").strip().lower()
# Ζητάμε το κείμενο από τον χρήστη
text = input("Enter the text: ")
# Ζητάμε τις παραμέτρους a και b από τον χρήστη
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Ανάλογα με την επιλογή του χρήστη, καλούμε την αντίστοιχη συνάρτηση
if choice == 'encrypt':
    result = encrypt(text, a, b)  # Κλήση της συνάρτησης κρυπτογράφησης
    print("Encrypted text:", result)  # Εμφάνιση του κρυπτογραφημένου κειμένου
elif choice == 'decrypt':
    result = decrypt(text, a, b)  # Κλήση της συνάρτησης αποκρυπτογράφησης
    print("Decrypted text:", result)  # Εμφάνιση του αποκρυπτογραφημένου κειμένου
else:
    print("Invalid choice")  # Αν η επιλογή δεν είναι σωστή, εμφάνιση μηνύματος λάθους