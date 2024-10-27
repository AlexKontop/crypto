def caesar_cipher(text, shift, mode):
    result = ""  # Αρχικοποίηση του αποτελέσματος ως κενή συμβολοσειρά.
    
    # Έλεγχος λειτουργίας κρυπτογράφησης ή αποκρυπτογράφησης.
    if mode == "encrypt":
        shift = shift % 26  # Αν είναι κρυπτογράφηση, ορίζουμε το shift με βάση το υπόλοιπο της διαίρεσης με το 26.
    elif mode == "decrypt":
        shift = -shift % 26  # Αν είναι αποκρυπτογράφηση, αντιστρέφουμε το shift και υπολογίζουμε το υπόλοιπο με το 26.

    # Επανάληψη για κάθε χαρακτήρα στο κείμενο.
    for char in text:
        if char.isalpha():  # Έλεγχος αν ο χαρακτήρας είναι γράμμα.
            # Ανάλογα με το αν ο χαρακτήρας είναι πεζός ή κεφαλαίος, ορίζουμε τη βάση.
            base = ord('a') if char.islower() else ord('A')
            # Μετατροπή του χαρακτήρα με βάση το shift και προσθήκη στο αποτέλεσμα.
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Αν ο χαρακτήρας δεν είναι γράμμα, τον προσθέτουμε στο αποτέλεσμα χωρίς αλλαγή.
            result += char

    return result  # Επιστροφή του τελικού αποτελέσματος.

# Λήψη του τρόπου λειτουργίας (κρυπτογράφηση ή αποκρυπτογράφηση) από το χρήστη.
mode = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
# Έλεγχος αν η λειτουργία είναι έγκυρη.
if mode not in ["encrypt", "decrypt"]:
    print("Please choose 'encrypt' or 'decrypt'.")  # Ενημέρωση χρήστη για μη έγκυρη επιλογή.
else:
    # Λήψη του κειμένου και του κλειδιού από τον χρήστη.
    text = input("Enter the message: ")
    shift = int(input("Enter the key as integer: "))
    # Κλήση της συνάρτησης caesar_cipher για κρυπτογράφηση ή αποκρυπτογράφηση.
    result = caesar_cipher(text, shift, mode)
    # Εκτύπωση του αποτελέσματος.
    print(f"The result is: {result}")