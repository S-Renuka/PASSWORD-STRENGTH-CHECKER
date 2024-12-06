import re
def password_strength(password):
    if len(password) < 8:
        return "Weak: Password is too short."
                    
    if not re.search("[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter."
                    
    if not re.search("[A-Z]", password):
        return "Weak: Password should contain at least one uppercase letter."
                    
    if not re.search("[0-9]", password):
        return "Weak: Password should contain at least one digit."
                    
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not special_characters.search(password):
        return "Medium: Password should contain at least one special character for stronger strength."
                    
    return "Strong: Your password is strong."

if name == "main":
    user_password = input("Enter your password: ")
    print(password_strength(user_password))