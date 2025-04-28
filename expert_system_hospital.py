# Simple Expert System for Medical Diagnosis

def ask_question(question):
    answer = input(question + " (yes/no): ").strip().lower()
    while answer not in ('yes', 'no'):
        print("Please answer with 'yes' or 'no'.")
        answer = input(question + " (yes/no): ").strip().lower()
    return answer == 'yes'

def medical_expert_system():
    print("Welcome to the Hospital Medical Expert System!")
    print("Please answer the following questions:")

    if ask_question("Do you have a fever?"):
        if ask_question("Do you have a cough?"):
            if ask_question("Are you experiencing difficulty breathing?"):
                print("\nDiagnosis: You might have COVID-19 or a respiratory infection.")
            else:
                print("\nDiagnosis: You may have a common flu.")
        else:
            if ask_question("Do you have a rash?"):
                print("\nDiagnosis: You might have Dengue Fever.")
            else:
                print("\nDiagnosis: You may have a viral infection.")
    else:
        if ask_question("Do you have body pain?"):
            if ask_question("Are you experiencing joint pain?"):
                print("\nDiagnosis: You may have Chikungunya.")
            else:
                print("\nDiagnosis: You may have a mild infection.")
        else:
            if ask_question("Do you have a headache?"):
                print("\nDiagnosis: You might have a Migraine.")
            else:
                print("\nDiagnosis: No serious symptoms detected. Stay hydrated and rest.")

    print("\nNote: This is a basic expert system and not a substitute for professional medical advice.")

# Run the expert system
medical_expert_system()
