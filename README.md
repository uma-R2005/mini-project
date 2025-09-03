# Password Training Quest

This mini-project helps users evaluate the strength of their passwords and test their memory recall after a short delay.  
It is a simple and educational way to improve password habits while learning about entropy, strength scoring, and secure practices.

---

## Features

- Password scoring (0–10) based on length, uppercase, lowercase, digits, special characters, and avoiding common dictionary words  
- Entropy calculation (measures unpredictability of the password in bits)  
- Strength labels (Weak / Medium / Strong)  
- Memory training (wait 2 minutes, then recall your password)  
- Logging (saves activity in `trainer.log`)  
- Result storage (saves outcomes in `trainer_results.csv`)  

---

## How It Works

1. The user enters a password (input is hidden).  
2. The program calculates score, entropy, strength, and explanations.  
3. The user is asked to remember their password for 2 minutes.  
4. After 2 minutes, the user must re-enter the password.  
5. The result is logged and stored in `trainer_results.csv`.  

---

## Files

- `password_trainer.py` → Main script  
- `test_password_trainer.py` → Test cases  
- `trainer.log` → Logs function calls and activity  
- `trainer_results.csv` → Stores password test results  

