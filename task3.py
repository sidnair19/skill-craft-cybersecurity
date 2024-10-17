import re

def assess_password_strength(password):
    strength_criteria = {
        'length': len(password) >= 8,
        'uppercase': any(char.isupper() for char in password),
        'lowercase': any(char.islower() for char in password),
        'digit': any(char.isdigit() for char in password),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    # Calculate score based on criteria met
    score = sum(strength_criteria.values())
    
    # Feedback messages
    feedback = []
    if not strength_criteria['length']:
        feedback.append("Password should be at least 8 characters long.")
    if not strength_criteria['uppercase']:
        feedback.append("Password should include at least one uppercase letter.")
    if not strength_criteria['lowercase']:
        feedback.append("Password should include at least one lowercase letter.")
    if not strength_criteria['digit']:
        feedback.append("Password should include at least one digit.")
    if not strength_criteria['special']:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*).")

    # Provide strength assessment
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength, score, feedback

# User input
password = input("Enter your password: ")

# Assess password strength
strength, score, feedback = assess_password_strength(password)

# Output results
print(f"\nPassword Strength: {strength}")
print(f"Score: {score}/5")

if feedback:
    print("\nSuggestions to improve your password:")
    for suggestion in feedback:
        print(f"- {suggestion}")