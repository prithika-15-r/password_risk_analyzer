import re
import math
def password_strength(password):
    score=0
    feedback=[]
    if len(password)>=12:
        score+=2
    elif len(password)>=8:
        score+=1
        feedback.append("Increase password length...")
    else:
        feedback.append("Password is too short")

    #checking of characters,numbers and special symbols
    if re.search(r"[A-Z]",password):
        score+=1
    else:
        feedback.append("missing uppercase letters, add uppercase letters")
    if re.search(r"[a-z]", password):
        score+=1
    else:
        feedback.append("Missing lowercase letters; Add Lowercase letters")
    if re.search(r"[0-9]",password):
        score+=1
    else:
        feedback.append("Add Numbers")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score+=1
    else:
        feedback.append("include special symbols such as '@','#")
    
    #checking repeated characters and patterns
    if re.search(r"(.)\1\1",password):
        score -=1
        feedback.append("avoid repetition of characters like 'aaa','bbb'")
    
    if re.search(r"123|abc|qwerty",password.lower()):
        score-=1
        feedback.append("avoid keyboard patterns")
    
    #entropy estimation
    charset=0
    if re.search(r"[a-z]",password):
        charset+=26
    if re.search(r"[A-Z]",password):
        charset+=26
    if re.search(r"[0-9]",password):
        charset+=10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset+=32
    
    entropy= round(len(password)* math.log2(charset)) if charset else 0

    #Brute force time estimation
    attempts_per_second= 1e9
    seconds= (2**entropy)/attempts_per_second if entropy else 0

    #final score
    if score<=2:
        strength = "WEAK"
    elif score<=4:
        strength="MEDIUM"
    else:
        strength="STRONG"
    return strength, entropy, int(seconds), feedback

password= input("Enter password to analyze:")
strength, entropy, time_to_crack, tips=password_strength(password)
print("\nPassword Strength:", strength)
print("Estimated Entropy:", entropy, "bits")
print("Estimated brute-force time (seconds):", time_to_crack)

if tips:
    print("\nSuggestions:")
    for tip in tips:
        print("-",tip)
else:
    print("\nGood job! your password is secure")

