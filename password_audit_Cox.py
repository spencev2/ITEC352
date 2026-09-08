"""Password Strength Audit starter template.

Complete each TODO. Do not change the required function names or parameters.
"""


def get_password_count():
    """Prompt until the user enters a positive whole number; return that number."""
    #this function gets and validates the number of passwords to audit
    while True:
        try:
            count = int(input("How many passwords would you like to audit? "))

            if count > 0:
                return count
            else:
                print("Please enter a whole number greater than zero.")

        except ValueError:
            print("Please enter a whole number greater than zero.")


def evaluate_password(password):
    """Return Strong, Moderate, or Weak after examining one password."""
    #this function checks the password requirements and returns its rating
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    type_total = has_uppercase + has_lowercase + has_digit + has_special

    if len(password) >= 12 and type_total == 4:
        return "Strong"
    elif len(password) >= 8 and type_total >= 3:
        return "Moderate"
    else:
        return "Weak"


def display_summary(strong_count, moderate_count, weak_count):
    """Display the totals for each password-rating category."""
    #this function displays the final totals for each password rating
    print("\n--- Password Audit Summary ---")
    print("Strong passwords:  ", strong_count)
    print("Moderate passwords:", moderate_count)
    print("Weak passwords:    ", weak_count)


def main():
    """Coordinate the password audit."""
    #this function controls the password audit and keeps track of the totals
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    password_count = get_password_count()

    for password_number in range(1, password_count + 1):
        password = input(f"\nPassword {password_number}: ")
        rating = evaluate_password(password)
        print("Rating:", rating)

        if rating == "Strong":
            strong_count += 1
        elif rating == "Moderate":
            moderate_count += 1
        else:
            weak_count += 1

    display_summary(strong_count, moderate_count, weak_count)


if __name__ == "__main__":
    main()
