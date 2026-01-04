"""
PROJECT: ONCOLOGICAL CLINICAL TRIAGE SYSTEM
VERSION: 1.0.0
AUTHOR: [Laurien Michel /GitHub Username:Laurien03]

DESCRIPTION:
This system is a Clinical Decision Support Tool designed to streamline oncology 
patient registration and triage. It utilizes an 8-level class inheritance 
structure to ensure data integrity across multiple clinical stages, including 
vital signs, symptom assessment, and emergency protocol detection.

KEY LOGIC:
- Multi-level Inheritance Architecture
- Real-time Clinical Scoring (0-10 Scale)
- Automated Emergency 'Red Flag' Triggers (Score >= 8)
- High-volume data processing (100-patient capacity)
"""
import sys

# Front Desk Coordinator


class Receptionnist:

    # >>The entire sequence from first contact to the patient sitting in the waiting room .. for more information BMI stands for Body Mass Index
    def __init__(self, name, age, sex, weight, height, BMI):
        self.age = age
        self.name = name
        self.sex = sex
        self.weight = weight
        self.height = height
        self.BMI = BMI

    def patient_registration_step1(self):
        # """Captures and validates basic identity and demographic data."""

        # --- Loop 1: Full Legal Name Validation ---
        while True:
            try:

                patient_name = self.name = input(
                    " Welecome to our clinic . Please provide your full legal name as it appears on your ID:").strip()
                # Ensure input is alphabetic and not empty
                if patient_name.replace(" ", "").isalpha() and len(patient_name) > 0:
                    print(
                        "✅Name recorded successfully. Proceeding to demographic verification")
                    break
                else:
                    print(
                        " ⛔️Invalid entry Please ensure you provide a full name using only alphabetic characters")

            except ValueError:
                print(



                    " ⛔️Invalid entry Please ensure you provide a full name using only alphabetic characters")

        # --- Loop 2: Age Validation (Numeric) ---
        while True:
            try:
                # Direct conversion to int handles type checking automatically
                patient_age = self.age = int(
                    input("Please enter your current age in years using numbers:"))
                if type(patient_age) == int:
                    print("✅Age verified. Eligibility criteria met for the next phase")
                    break
                else:
                    print(
                        " ⛔️Data entry error. Please enter a valid numerical age (e.g., 45)")

            except ValueError:
                print(

                    " ⛔️Data entry error. Please enter a valid numerical age (e.g., 45)")

        # --- Loop 3: Sex/Gender Documentation ---
        while True:
            try:

                patient_sex = self.sex = input(
                    "Please indicate your sex (M/F/Other): ").strip().lower()
                # Validate against accepted medical categories
                if patient_sex in ["m", "f", "other", "male", "female"]:
                    print(
                        "✅ Patient sex documented. Initializing physical metrics module")
                    break
                else:
                    print(
                        "⛔️ Selection not recognized. Please choose from M, F, or Other.")

            except Exception:
                print("⛔️ An unexpected error occurred.")

    def patient_registration_step2(self):
        # """Captures physical metrics required for clinical BMI and dosage calculations."""
        # --- Loop 1: Weight Input (Kilograms) ---
        while True:
            try:
                # Capturing weight as a float to allow for decimal precision
                patient_weight = self.weight = float(
                    input("Enter your current weight in kilograms (kg) for dosage precision: "))
                if type(patient_weight) == float:
                    print(
                        "✅Weight captured. Metric has been stored for clinical calculations")
                    break
                else:
                    print(
                        "⛔️input error. Please enter weight as a number or decimal (e.g., 70.5).")
            except ValueError:
                print(
                    "⛔️input error. Please enter weight as a number or decimal (e.g., 70.5).")
            # --- Loop 2: Height Input (Meters) ---
        while True:
            try:
                # Capturing height as a float (e.g., 1.75)
                self.height = float(
                    input("Enter your height in meters (m) to complete your physical profile: "))
                # Basic safety check to prevent height being 0 (which breaks BMI formula)
                if self.height > 0:
                    print("✅ Height captured. Finalizing biometric analysis.")
                    break
                else:
                    print("⛔️ Entry failed. Height must be greater than 0.")
            except ValueError:
                print(
                    "⛔️ Entry failed. Ensure height is entered in meters (e.g., 1.75).")

    def patient_registration_step3(self):
        # Calculates BMI and performs a final data accuracy confirmation.

        # Calculate BMI using the standard formula (Weight / Height^2)
        # We round to 1 decimal place for professional medical reporting
        if self.height > 0:
            self.BMI = self.weight / (self.height ** 2)
            print(
                f"Based on the information provided, your BMI is: {round(self.BMI, 1)}")

        # Final Verification Gate
        confirmation = input(
            "Is all the information provided correct? (Yes/No): ").strip().lower()

        if confirmation in ["yes", "y"]:
            print("Registration Finalized ✅. Your profile has been successfully updated.")
            # Signal that registration is complete
        else:
            # notifying the user about the failure
            print(
                "Validation Declined ⛔️. Basic registration incomplete. Please restart the process.")

            # we immediately trigger the retry of Step 2 -- # Recursive calls: redo Step 2, then redo Step 3 for a new confirmation
            self.patient_registration_step1()
            self.patient_registration_step2()
            self.patient_registration_step3()


class Oncology_Clinical(Receptionnist):
    def __init__(self, name, age, sex, weight, height, BMI):
        super().__init__(name, age, sex, weight, height, BMI)
        self.name = name

    def verify_consultation_type(self):
        # Dictionary mapping numeric codes to clinical visit types for easy updates
        visit_reason = {1: "New Diagnosis",
                        2: "Follow-up",
                        3: "Treatment sessions",
                        4: "Side Effects",
                        5: "Results Review"}
        # Standardized error message to maintain consistent UI/UX
        error_msg = "⛔️ Invalid entry. Please enter a number (1-5) from the menu"
        while True:
            try:
                print("\n--Reason for Visit---")
                # Loop through dictionary to display menu dynamically
                for key, value in visit_reason.items():
                    print(f"{key} {value}")
                self.patient_choice = int(input(
                    "To route your file correctly, please select your assigned department number from the list above.:"))
                # Validation check against dictionary keys
                if self.patient_choice in visit_reason:
                    # Accessing dictionary value using square brackets []
                    self.visit_reason_confirmation = visit_reason[self.patient_choice]
                    print(
                        f"✅ Entry verified. Your file has been updated with the following status :{self.visit_reason_confirmation}")
                    break
                else:
                    print(error_msg)
            except ValueError:
                # Catching non-integer inputs to prevent program crash
                print(error_msg)

    def Pathology_information(self):
        """
        Manages the collection of specific oncological data.
        This method captures both the cancer category and the clinical stage,
        ensuring both are validated before finalizing the patient profile.
        """
        # error message for diagnostic validation failures
        error = "⛔️ Validation failed. To ensure data integrity, please re-verify your Category and Stage starting from the menu above."

        pathology_type = {
            1: "Carcinoma (Covers Breast, Lung, Prostate, Colon",
            2: "Sarcoma (Bone and soft tissue)",
            3: "Lymphoma (Lymph system)",
            4: "Leukemia (Blood cancers)",
            5: "Melanoma (Skin cancer)",
            6: "Neuroendocrine (Nervous/Endocrine system)",
            7: "Other / Rare Tumor"
        }
        pathology_stages = {1: "Stage I", 2: "Stage II",
                            3: "Stage III", 4: "Stage IV"}
        # Primary control loop: Ensures the user cannot progress until data is validated

        while True:
            try:
                # --- SECTION 1: Category Selection ---
                print("\n--- Clinical Pathology Classification ---")
                for key, value in pathology_type.items():
                    print(f"{key} , {value}")
                self.pathology_type_selection = int(
                    input("Select the numeric code (1-7) corresponding to your primary diagnosis:"))
                self.review_and_confirmation = input(
                    "Is  the information provided correct? Please enter 'Y' for Yes or 'N' for No : ").strip().upper()
                # Validation Logic: Cross-references integer input against dictionary keys
                if self.pathology_type_selection in pathology_type and self.review_and_confirmation == "Y":
                    if self.pathology_type_selection == 7:
                        self.pathology_type_confirmation = input(
                            "You selected 'Other'. Please type the name of the pathology you are currently being treated for:")
                        print(
                            f"✅ Pathology synchronized. Recording category:{self.pathology_type_confirmation}")

                    else:
                        self.pathology_type_confirmation = pathology_type[self.pathology_type_selection]
                        print(
                            f"✅ Pathology synchronized. Recording category:{self.pathology_type_confirmation}")

                else:
                    print(error)
                    continue  # Restarts the loop if the Category is not confirmed
            except ValueError:
                print(error)
                continue  # Error Handling: Catches non-numeric input to prevent program termination

            try:
                print("--- Staging Verification ---")
                for key, value in pathology_stages.items():
                    print(f"{key} , {value}")
                self.pathology_stage_selection = int(
                    input("Please enter the number (1-4) representing your current clinical stage:"))
                self.stage_review_confirmation = input(
                    "Is the information provided correct? Please enter 'Y' for Yes or 'N' for No: ").strip().upper()
                # Final Data Synchronization: Pairs Category and Stage for the final profile
                if self.pathology_stage_selection in pathology_stages and self.stage_review_confirmation == "Y":
                    self.pathology_stage_confirmation = pathology_stages[self.pathology_stage_selection]
                    print(
                        f"✅ Staging confirmed. Recording:{self.pathology_stage_confirmation}")
                    # Final Summary: Integrates data from both sections into a final string output
                    print(
                        f"Dear {self.name} Your Clinical Profile Were Generated:{self.pathology_type_confirmation} - {self.pathology_stage_confirmation}")
                    print(
                        "All diagnostic data has been successfully validated. Task 2 complete")
                    break  # Final break: Exits the method only after both pieces of data are confirmed

                else:
                    print(error)

            except ValueError:
                print(error)


class Symptom_Severity_Assessment(Oncology_Clinical):
    def __init__(self, name, age, sex, weight, height, BMI):
        super().__init__(name, age, sex, weight, height, BMI)

    def assess_symptom(self):
        """
        Captures patient-reported symptom intensity using a 0-10 scale.
        Includes automated logic for critical value alerts (scores >= 8).
        """
        # Centralized error message for non-integer or out-of-range inputs
        error = "⛔️ Entry not recognized. To ensure your doctor receives accurate data, please provide a numeric digit."
        # Clinical variables list; can be modified to include specialty-specific symptoms
        patient_symptoms = ["Pain", "Fever", "Fatigue",
                            "Nausea/Vomiting", "Shortness of breath ", "Bleeding"]
        # Dictionary to store session data for clinical analysis or database entry
        self.symptom_selection = {}
        # Iterates through each symptom to ensure a complete clinical picture
        for self.selection in patient_symptoms:
            while True:
                try:
                    print(f"\n Assesssing:{self.selection}")
                    self.score = int(input(
                        f"How would you describe your {self.selection} today? Please enter a number from 0 (not present) to 10 (extremely severe):"))
                    # Range validation to maintain data integrity
                    if 0 <= self.score <= 10:
                        self.symptom_selection[self.selection] = self.score
                        # Critical Threshold Logic: High scores trigger immediate notification flags
                        if self.score >= 8:
                            print(
                                f"⚠️ URGENT ALERT: Dear {self.name}, a score of {self.score} for {self.selection} has triggered an emergency notification. This information has been directed to your doctor immediately. Please seek urgent care.")

                            break  # Exits while loop to move to next symptom
                        else:
                            print(
                                f"✅ Information saved. Your report for {self.selection} of {self.score} has been forwarded to your clinical record for review.")

                            break  # Exits while loop to move to next symptom

                    else:
                        print(error)
                except ValueError:
                    print(error)
        print("\n✅ Assessment complete. All symptom variables have been successfully validated and stored in the clinical dictionary.")


class Clinical_Checking(Symptom_Severity_Assessment):
    def __init__(self, name, age, sex, weight, height, BMI):
        super().__init__(name, age, sex, weight, height, BMI)
     # Triage protocol: Designed to intercept life-threatening complications before general assessment.

    def clinical_red_flag(self):
        # Scalable Checklist: New emergency criteria can be added here without modifying the loop logic.
        red_flag_checklist = ["1. Neutropenic Fever:Do you have a fever of 100.4°F (38°C) or higher?",  "2. Respiratory Distress: Are you experiencing sudden shortness of breath or sharp chest pain?:", " 3. Neurological Change:Have you noticed any new confusion, dizziness, or sudden loss of balance ?: ", " 4. Hemostatic Failure: Do you have any active bleeding that won't stop or are you coughing up blood?",
                              " 5. Bowel Obstruction:Are you experiencing persistent vomiting or an inability to pass stool for over 24 hours?", " 6. Neuropathy/Cord Compression: Do you have any new numbness, tingling, or sudden weakness in your legs?", "7.Severe Dehydration:Are you unable to keep any liquids down or feeling extremely faint when standing?"]
        print("--- CRITICAL SAFETY CHECK ---")
        print("Please confirm if you are experiencing any of the following emergency symptoms.")
        for self.red_flag in red_flag_checklist:
            while True:
                # Normalization: the validation logic.
                response = input(
                    f" Are you currently experiencing {self.red_flag} ? Please enter 'Y' for Yes or 'N' for No:").strip().upper()
                if response == "Y":
                    print("-- ⚠️ EMERGENCY PROTOCOL ACTIVATED --")
                    print(f" Dear {self.name} , your report of {self.red_flag} has been directed to your doctor's emergency dashboard. Please stop this assessment and proceed to the nearest ER immediately.")
                    print(
                        "Information directed to your doctor. Please STOP and go to the ER now....")
                    # Critical Safety Stop: Terminates the script to force immediate medical intervention.
                    sys.exit()
                elif response == "N":
                    print(
                        f"✅ Negative for {self.red_flag}. Continuing safety check...")
                    break
                else:
                    print(
                        "⛔️ ENTRY ERROR: To ensure your safety and direct your data correctly, please use 'Y' or 'N' only.")


class Medical_Regimen(Clinical_Checking):
    """
     Purpose: Manages the collection and verification of oncological treatments.
    It links treatment types to specific medications, dosages, and schedules.
    """

    def __init__(self, name, age, sex, weight, height, BMI):
        super().__init__(name, age, sex, weight, height, BMI)

    def add_treatment(self):
        # mapping for standardized clinical categories
        treatment_checklist = {
            1: "chemotherapy",
            2: "Radiation",
            3: "Immunotherapy",
            4: "Hormonal",
            5: "Targeted Therapy",
            6: "Supportive Care",
            7: "Other"
        }
        error = "⛔️ INVALID SELECTION: Please enter a number from the list provided (e.g., 1-7)."

        print("--- Treatment list Verification  ---")

        for key, value in treatment_checklist.items():

            print(f" {key} : {value} ")

        while True:
            try:

                self.treatment_choice = int(input(
                    "Please select your primary treatment category (1-7) from the list below by entering the corresponding number:"))
                self.treatment_choice_review = input(
                    "Is the information provided correct? (Yes/No) Please enter 'y' for Yes or 'n' for No : ").strip().upper()
                if self.treatment_choice in treatment_checklist and self.treatment_choice_review == "Y":
                    # Data Persistence: Saves custom input to self so the final summary can access it
                    self.treatment_selected = treatment_checklist[self.treatment_choice]
                    if self.treatment_choice == 7:
                        self.treatment_selected = input(
                            "Please type your treatment name:")
                        print(f"Recorded : {self.treatment_selected}")

                    else:
                        self.treatment_selected = treatment_checklist[self.treatment_choice]
                        print(
                            f"✅ You have selected: {self.treatment_selected}. This has been added to your profile.")
                    break
                else:
                    print(error)
            except ValueError:
                print(error)

    def add_medication(self):
        error = "⛔️ INVALID SELECTION: Please enter a number from the list provided (e.g., 1-7)."
        medication_checklist = {1: "Cisplatin, Paclitaxel, 5-Fluorouracil, Doxorubicin, Cyclophosphamide",
                                2: "Pembrolizumab (Keytruda), Nivolumab (Opdivo), Ipilimumab, Atezolizumab",
                                3: "Dexamethasone, Amifostine, Silver Sulfadiazine, Ondansetron ",
                                4: "Tamoxifen, Letrozole, Anastrozole, Leuprolide, Goserelin",
                                5: "Trastuzumab, Erlotinib, Imatinib, Bevacizumab, Rituximab",
                                6: "Lorazepam, Prochlorperazine, Morphine, Gabapentin, Metoclopramide",
                                7: "Other"
                                }
        print("-- Medication verification --")
        for key, value in medication_checklist.items():
            print(f"{key} : {value}")
        while True:
            try:

                self.medication_choice = int(input(
                    f"Based on your treatment ({self.treatment_selected}), please select your medication (1-7):"))
                self.medication_choice_review = input(
                    "Is the information provided correct? (Yes/No) Please enter 'y' for Yes or 'n' for No : ").strip().upper()

                if self.medication_choice in medication_checklist and self.medication_choice_review == "Y":
                    self.medication_selected = medication_checklist[self.medication_choice]
                    if self.medication_choice == 7:
                        self.medication_selected = input(
                            "Please type your medication name:")
                        print(f"Recorded : {self.medication_selected}")
                    else:
                        print(
                            f"✅ You have selected: {self.medication_selected}. This has been added to your profile.")
                    break  # Loop control: Exits successfully for both standard and manual entry

                else:
                    print(error)
            except ValueError:
                print(error)

    def medication_dosage(self):
        dosage_list = {
            1: "5 mg",
            2: "10 mg",
            3: "25 mg",
            4: "50 mg",
            5: "100 mg",
            6: "250 mg",
            7: "500 mg",
            8: "Other"
        }
        error = " ⛔️ INVALID INPUT: Please enter a number between 1 and 8 to select your dosage."

        print("-- Dosage Verification --")
        for key, value in dosage_list.items():
            print(f"{key} : {value}")
        while True:
            try:

                self.dosage_choice = int(input(
                    f"Based on your medication :({self.medication_selected}), Please select the prescribed dosage for your medication from the list (1-8:"))
                self.dosage_choice_review = input(
                    "Is the information provided correct? (Yes/No) Please enter 'y' for Yes or 'n' for No : ").strip().upper()

                if self.dosage_choice in dosage_list and self.dosage_choice_review == "Y":
                    self.dosage_selected = dosage_list[self.dosage_choice]
                    if self.dosage_choice == 8:
                        # Order of Operations: Get input first, then assign to instance variable
                        manual_dosage_enter = input(
                            "You selected 'Other.' Please type your specific frequency instructions (e.g., Every 48 hours): ")
                        self.dosage_selected = manual_dosage_enter
                        print(f"Recorded : {manual_dosage_enter}")

                    else:
                        print(
                            f"✅ Dosage Recorded:: {self.dosage_selected}. has been saved to your regiment")
                    break

                else:
                    print(error)
            except ValueError:
                print(error)

    def medication_frequency(self):
        medication_frequency_list = {
            1: "Once daily (Morning)",
            2: "Once daily (Night)",
            3: "Twice daily (Every 12 hours)",
            4: "Three times daily (Every 8 hours)",
            5: "Four times daily (Every 6 hours)",
            6: "Weekly",
            7: "As needed (PRN) ",
            8: "Other"
        }
        error = "⛔️ SELECTION ERROR: Please choose a valid frequency number from 1 to 8."
        print("-- Medication Frequency Verification --")
        for key, value in medication_frequency_list.items():
            print(f"{key} : {value}")
        while True:
            try:

                self.frequency_choice = int(input(
                    f"Please select your medication schedule (1-8): "))
                self.frequency_choice_review = input(
                    "Is the information provided correct? (Yes/No) Please enter 'y' for Yes or 'n' for No : ").strip().upper()

                if self.frequency_choice in medication_frequency_list and self.frequency_choice_review == "Y":
                    self.frequency_selected = medication_frequency_list[self.frequency_choice]
                    if self.frequency_choice == 8:

                        manual_frequency_enter = input(
                            "You selected 'Other.' Please specify  your medication schedule: ")
                        self.frequency_selected = manual_frequency_enter
                        print(f"Recorded : {manual_frequency_enter}")
                    else:
                        print(
                            f"✅ Schedule Recorded: {self.frequency_selected}.")
                    break
                else:
                    print(error)
            except ValueError:
                print(error)

    def final_regimen_verification(self):
        print(f"\nDear {self.name},")
        print("Here is the summary of the regimen details you just completed:")
        print("-" * 40)
        print(f"• Treatment Category: {self.treatment_selected}")
        print(f"• Medication Name:    {self.medication_selected}")
        print(f"• Prescribed Dosage:  {self.dosage_selected}")
        print(f"• Intake Frequency:   {self.frequency_selected}")
        print("-" * 40)

        while True:
            verify = input(
                "Please take your time to verify if everything in this summary is correct. Reply 'Y' for Yes or 'N' for No: ").strip().upper()

            if verify == 'Y':
                print(
                    "✅ Thank you. Your information is verified. We can now continue to the next task.")
                break  # Exit verification loop

            elif verify == 'N':
                print(
                    "⚠️ Profile Redirected:⚠️ Please try Again..")
                #  Safety Loop: Forces a re-entry of all data to ensure medical accuracy
                self.add_treatment()
                self.add_medication()
                self.medication_dosage()
                self.medication_frequency()
                break  # Prevents old verification loop from persisting

            else:
                print("⛔️Invalid input. Please enter 'y' or 'n'.")


class Side_Effects_Tracker(Medical_Regimen):
    def __init__(self, name, age, sex, weight, height, BMI):
        super().__init__(name, age, sex, weight, height, BMI)

    def symptom_localization(self):
        """
        Step 1: Identify the body region affected.
        Uses a nested if/else to handle either standard dictionary selection 
        or a manual 'Other' description.
        """

        body_area_checklist = {
            1: "Head & Neck (Headaches, dizziness, mouth issues)",
            2: "Chest & Respiratory (Breathing, heart, or lungs)",
            3: "Gastrointestinal (Stomach, digestion, or bowel)",
            4: "Extremities (Arms, legs, joints, or neuropathy)",
            5: "Systemic (Full body issues like fatigue or fever)",
            6: "Skin & Integumentary (Rashes, itching, or injection site)",
            7: "Other"
        }
        error = (
            "⛔️ INPUT ERROR: That is not a valid selection. You must enter a single number from 1 to 7 to proceed.")
        print("--- Symptom Localization Assessment ---")
        for key, value in body_area_checklist.items():
            print(f"{key} : {value}")
        while True:
            try:
                self.symptom_area_choice = int(input(
                    "To begin your report, Based on the list above, please type the number (1-7) that corresponds to the body region you wish to report: "))
                self.symptom_area_choice_review = input(
                    "Is the selected area correct? Please enter 'Y' for Yes or 'N' for No: ").strip().upper()
                if self.symptom_area_choice in body_area_checklist and self.symptom_area_choice_review == "Y":
                    # Path A: Manual input for custom descriptions

                    if self.symptom_area_choice == 7:
                        self.symptom_area_selected = input(
                            "Please provide a specific description of the area or location: ")

                        print(
                            f"✅ Area Recorded: We are now documenting symptoms for the {self.symptom_area_selected}")
                    # Path B: Standard selection from the checklist
                    else:
                        self.symptom_area_selected = body_area_checklist[
                            self.symptom_area_choice]
                        print(
                            f"✅ Area Recorded: We are now documenting symptoms for the {self.symptom_area_selected}")
                    break  # Exits loop only after a valid path is executed
                else:
                    print(error)
            except ValueError:
                print(error)

    def symptom_identification(self):
        """
        Step 2: Identify the specific symptom within the chosen body area.
        The prompt dynamically references self.symptom_area_selected from Method 1.
        """
        symptom_indetification_checklist = {
            1: "Head & Neck	: Headaches, Dizziness, Mouth Sores, Sore Throat, Difficulty Swallowing",
            2: "Chest:Shortness of Breath, Chest Pain, Coughing, Palpitations",
            3: "Gastro: Nausea, Vomiting, Diarrhea, Constipation, Abdominal Pain",
            4: "Extremities: Numbness/Tingling, Joint Pain, Swelling (Edema), Muscle Weakness",
            5: "Systemic : 	Fatigue, Fever, Chills, Night Sweats, Weight Loss",
            6: " Skin : Rash, Dryness, Redness, Itching, Hand-Foot Syndrome",
            7: "Other"
        }
        error = "⛔️ SELECTION ERROR: Please enter a number from 1 to 7 to identify your specific symptom."
        print("--- Symptom Identification ---")
        for key, value in symptom_indetification_checklist.items():
            print(f"{key} : {value}")
        while True:
            try:
                # Dynamic prompt using the previously saved body area
                self.symptom_identification_choice = int(input(
                    f"Based on the area selected ({self.symptom_area_selected}), please select the specific symptom you are experiencing (1-7): "))
                self.symptom_identification_choice_review = input(
                    "Is the selected symptom correct? Please enter 'Y' for Yes or 'N' for No: ").strip().upper()
                if self.symptom_identification_choice in symptom_indetification_checklist and self.symptom_identification_choice_review == "Y":
                    # Path A: Manual input captures symptom name directly to the instance variable
                    if self.symptom_identification_choice == 7:
                        self.symptom_identification_selected = input(
                            "You selected 'Other' Please type the name of the symptom you are experiencing in this area: ")
                        print(
                            f"✅ Recorded: {self.symptom_identification_selected}. This has been added to your symptom report.")
                    # Path B: Logic pulls specific symptom string from the checklist dictionary
                    else:
                        self.symptom_identification_selected = symptom_indetification_checklist[
                            self.symptom_identification_choice]
                        print(
                            f"✅ Symptom Logged: {self.symptom_identification_selected}  You have reported We will now assess the severity.")
                    break  # Loop exit upon successful data capture
                else:
                    print(error)
            except ValueError:
                print(error)

    def assess_severity(self):
        """
        Step 3: Grade the intensity of the reported symptom.
        Uses the CTCAE-based scale (Grades 1-4) or a manual description for 'Other'.
        """
        severity_scale = {
            1: "Grade 1: Mild (Asymptomatic or mild symptoms; intervention not indicated)",
            2: "Grade 2: Moderate (Minimal, local, or non-invasive intervention indicated)",
            3: "Grade 3: Severe (Severe or medically significant but not immediately life-threatening)",
            4: "Grade 4: Critical (Life-threatening consequences; urgent intervention indicated)",
            5: "Other"
        }
        error = (
            "⛔️ INPUT ERROR: Please enter a number between 1 and 5 to accurately grade your symptom severity.")
        print("--- Symptom Severity Assessment ---")
        for key, value in severity_scale.items():
            print(f"{key} : {value}")

        while True:
            try:
                # References the symptom name selected in Method 2
                self.symptom_severity_choice = int(input(
                    f"Based on your report of {self.symptom_identification_selected}, please select the severity grade that best describes your current state (1-5): "))
                self.symptom_severity_choice_review = input(
                    "Is this severity rating correct? Enter 'Y' for Yes or 'N' for No: :").strip().upper()
                # Verification specific to the severity grading
                if self.symptom_severity_choice in severity_scale and self.symptom_severity_choice_review == "Y":
                    # Path A: Captures specific intensity details manually
                    if self.symptom_severity_choice == 5:
                        self.symptom_severity_selected = input(
                            "Please provide any additional details regarding the intensity of this symptom: ")
                        print(
                            f"✅ Recorded: {self.symptom_severity_selected}. This has been added to your symptom report.")
                    # Path B: Maps the numeric choice to the clinical grade string
                    else:
                        self.symptom_severity_selected = severity_scale[self.symptom_severity_choice]
                        print(
                            f"✅ Severity Recorded: This symptom is logged as {self.symptom_severity_selected}.")
                    break  # Data confirmed and saved
                else:
                    print(error)
            except ValueError:
                print(error)

    def duration_checklist(self):
        duration_checklist = {
            1: "Less than 24 hours",
            2: "1 to 3 days",
            3: "4 to 7 days (1 week)",
            4: "1 to 2 weeks",
            5: "More than 2 weeks",
            6: "Other (Intermittent or specific timeframe)"
        }
        error = "⛔️ SELECTION ERROR: Please enter a valid number (1-6) to record the duration."
        print("--- Symptom Duration Assessment ---")

        for key, value in duration_checklist.items():
            print(f"{key} : {value}")

        while True:
            """
        Step 4: Record the onset and timeframe of the symptom.
        Captures either a range from the checklist or a specific pattern (Path A).
        """
            try:
                # References the symptom name to provide context for the duration question
                self.symptom_duration_choice = int(input(
                    f"How long have you been experiencing {self.symptom_identification_selected}? Please select a timeframe (1-6): "))
                self.symptom_duration_choice_review = input(
                    "Is this timeframe correct? (Y/N):").strip().upper()
                if self.symptom_duration_choice in duration_checklist and self.symptom_duration_choice_review == "Y":
                    # Path A: Captures specific temporal patterns (e.g., 'every morning')
                    if self.symptom_duration_choice == 6:
                        self.symptom_duration_selected = input(
                            "You selected 'Other.' Please type the specific duration or pattern (e.g., 'Only after meals' or 'Started 3 hours ago'): ")
                        print(
                            f"✅ Recorded: {self.symptom_duration_selected}. This has been added to your symptom report.")
                    # Path B: Stores the standard timeframe string from the dictionary
                    else:
                        self.symptom_duration_selected = duration_checklist[self.symptom_duration_choice]
                        print(
                            f"✅ Duration Logged: This symptom has been present for {self.symptom_duration_selected}")
                    break  # Data saved to instance
                else:
                    print(error)
            except ValueError:
                print(error)

    def verify_report(self):
        """
        Step 5: Final Summary.
        Displays all collected symptom data to the user for final review.
        """
        print(f"Dear {self.name}, your report is ready.")
        # Pulls identification and localization from Methods 1 & 2
        print(
            f"Summary: {self.symptom_identification_selected} affecting the {self.symptom_area_selected}.")
        # Pulls severity and duration from Methods 3 & 4
        print(f"Severity: {self.symptom_severity_selected}")
        print(f"Duration: {self.symptom_duration_selected}")


class ClinicalContext(Side_Effects_Tracker):
    def __init__(self, name, age, sex, weight, height, BMI):
        super().__init__(name, age, sex, weight, height, BMI)

    def test_verification(self):
        """
        Identifies recent medical tests to provide clinical context.
        Logic: Uses a validated dictionary lookup with a nested if/else 
        to separate manual 'Other' entries from predefined categories.
        """
        recent_tests_checklist = {
            1: "Laboratory Work (Blood, Urine, or Stool Analysis)",
            2: "Diagnostic Imaging (X-Ray, CT, MRI, or Ultrasound)",
            3: "Pathology (Biopsy or Tissue Sample)",
            4: "Functional Studies (EKG, ECG, or Stress Test)",
            5: "None / No recent tests performed",
            6: "Other"
        }
        error = f"⛔️ INPUT ERROR: Please select a valid category (1-6) to ensure your {self.symptom_area_selected} symptoms are properly documented."
        print("--- Recent Medical Tests Verification ---")
        for key, value in recent_tests_checklist.items():
            print(f"{key} {value}")
        while True:
            try:

                self.recent_tests_choice = int(input(
                    f"Dear {self.name} , to better understand your {self.symptom_identification_selected},have you had any medical tests recently that might be related? Please choose a number between (1-6) from the list above: "))
                self.recent_tests_choice_review = input(
                    f"Confirming: You would like to link '{recent_tests_checklist[self.recent_tests_choice]}' to your current report? Please enter 'Y' for Yes or 'N' for No: ").strip().upper()
                # Ensures the input exists in the dictionary to prevent a KeyError crash.
                if self.recent_tests_choice in recent_tests_checklist and self.recent_tests_choice_review == "Y":

                    if self.recent_tests_choice == 6:
                        # Path A: Captures custom user input for the 'Other' category.
                        self.recent_tests_selected = input(
                            "You selected 'Other.' Please type the name of the specific test or procedure performed: ")
                        print(
                            f"✅ Linked: Your {self.recent_tests_selected} results have been flagged for review alongside your symptoms.")
                    else:
                        # Path B: Assigns the standard category name from the checklist.
                        self.recent_tests_selected = recent_tests_checklist[self.recent_tests_choice]
                        print(
                            f"✅ Linked: Your {self.recent_tests_selected} results have been flagged for review alongside your symptoms.")
                    break
                else:
                    print(error)
            except ValueError:
                print(error)

    def patient_concern(self):
        """Captures patient concerns by validating narrative length or an explicit skip ('N')."""

        print("--- Patient Advocacy: Personal Concerns ---")

        error = "⛔️ INPUT TOO SHORT >> Try Again: To ensure your doctor understands your perspective, please provide a bit more detail (at least 5 characters), or type 'N' to skip."
        while True:
            try:
                clinical_staff_followup = "We want to ensure your voice is a central part of this report. The following statement will be shared directly with your doctor to highlight what matters most to you."
                print(f'Dear {self.name} , {clinical_staff_followup}')
                self.patient_concern_statement = input(
                    f"Regarding your {self.symptom_identification_selected}, what is your primary concern or question for the medical team? (Please write 1-2 sentences, or type 'N for None ' if you have no specific questions): ")
                self.patient_concern_review = input(
                    f"You have expressed: '{self.patient_concern_statement}'. Should we include this exact wording in the final report for your doctor? Please enter 'Y' for Yes or 'N' for No: ").strip().upper()
                no_concerns = ("N").strip().upper()
                # Begins validation only if text is present and the user confirms with 'Y'.
                if len(self.patient_concern_statement) >= 1 and self.patient_concern_review == "Y":
                    # Path A: Standardizes the report if the user explicitly skips by typing 'N'.
                    if self.patient_concern_statement.upper() == no_concerns:

                        no_concerns = "Patient reports no specific concerns at this time."
                        self.patient_concern_statement = no_concerns
                        print(
                            "✅ Noted:Patient reports no specific concerns at this time.")
                        break
                        # Path B: Accepts the narrative if it meets the minimum clinical detail requirement.
                    elif len(self.patient_concern_statement) >= 5:
                        print(
                            "✅ Recorded: Your personal concern has been added to the physician's summary.")
                        break
                    else:
                        print(
                            # Error Handling: Triggered if input is 1-4 characters (too short for medical context).
                            error)

                else:
                    print(
                        "Entry cleared. Let's try again. Please rephrase your concern or question!")
            except ValueError:
                print(error)

    def functional_status(self):
        """Validates functional capability levels with nested confirmation to ensure medical record accuracy."""
        functional_status_option = {
            1:	"Fully Independent (No impact on daily activities or work)",
            2:	"Modified Independent (Can perform tasks but with pain or extra effort)",
            3:	"Partially Restricted (Requires help with some tasks like lifting or stairs)",
            4:	"Severely Restricted (Unable to perform basic daily activities)",
            5: "Other"
        }
        error = "⛔️ SELECTION ERROR: Please select a valid level **(1-5)** to ensure the severity of your condition is correctly logged."
        print("--- Functional Status Assessment ---")
        for key, value in functional_status_option.items():
            print(f"{key} {value}")
        while True:
            try:
                clinical_staff_followup = f" to assist with clinical triaging, we need to assess how your {self.symptom_area_selected} symptoms affect your daily routine."
                print(f"Dear {self.name} , {clinical_staff_followup}")
                self.functional_status_choice = int(input(
                    f"Based on the list above, which level best describes your current physical capability? Please choose a number (1-5):"))

                if self.functional_status_choice in functional_status_option:
                    self.functional_status_choice_review = input(
                        f"Confirming: You have categorized your functional status as '{functional_status_option[self.functional_status_choice]}'. Is this accurate for your medical record? Please enter 'Y' for Yes or 'N' for No: ").strip().upper()
                    # Step 2: User Confirmation - Only processes data if the patient explicitly confirms with 'Y'.
                    if self.functional_status_choice_review == "Y":
                        self.functional_status_selected = functional_status_option[
                            self.functional_status_choice]
                        # Special Case: Diverts to text input if 'Other' (5) is selected for detailed narrative.
                        if self.functional_status_choice == 5:
                            self.functional_status_selected = input(
                                f"You selected {functional_status_option[self.functional_status_choice]} **Please briefly describe how your symptoms are currently limiting your physical activities:** ")

                            confirmation = input(
                                "Is the information provided correct? (Yes/No) Please enter 'y' for Yes or 'n' for No : ").strip().upper()
                            if confirmation == "Y":

                                print(
                                    f"✅ Assessment Complete : Your {self.functional_status_selected} has been recorded as Your current functional status.")
                                break
                            else:
                                print("Selection cleared Please Try Again..")
                        else:
                            print(
                                # Default Case: Records standard levels 1-4 once confirmed.
                                f"✅ Assessment Complete : Your {self.functional_status_selected} has been recorded as Your current functional status")
                        break
                else:
                    print("Selection cleared. Please pick the correct number.")
            except ValueError:
                print(error)


class Clinical_Summary(ClinicalContext):
    """
    Consolidates data from all 7 specialized child classes into a 
    structured report formatted for physician-patient consultation.
    """

    def __init__(self, name, age, sex, weight, height, BMI):
        super().__init__(name, age, sex, weight, height, BMI)

    def generate_professional_report(self):
        """
        Aggregates and prints the final report using the SOAP (Subjective, 
        Objective, Assessment, Plan) clinical documentation standard.
        """
        print("\n" + "═" * 60)
        print("                 OFFICIAL CLINICAL SUMMARY")
        print("═" * 60)

        # Chief Complaint: Pulled from Oncology_Clinical.verify_consultation_type()
        print(f"REASON FOR VISIT:  [ {self.visit_reason_confirmation} ]")
        print("─" * 60)

        # Objective Metrics: Pulled from Receptionnist parent class
        print(f"PATIENT: {self.name.upper()}")
        print(
            f"METRICS: {self.age}y | {self.height}m | {self.weight}kg | BMI: {round(self.BMI, 1)}")
        print("─" * 60)

        # Clinical Background: Pulled from the 2 methods in ClinicalContext
        print("FUNCTIONAL & CLINICAL CONTEXT:")
        print(f"• Mobility Status: {self.functional_status_selected}")
        print(f"• Background:      {self.patient_concern_statement}")
        print("─" * 60)

        # Diagnosis & Plan: Pulled from Oncology_Clinical and Medical_Regimen
        print(
            f"DIAGNOSIS: {self.pathology_type_confirmation} (Stage {self.pathology_stage_confirmation})")
        print(
            f"CURRENT REGIMEN: {self.medication_selected} ({self.dosage_selected})")
        print(f"FREQUENCY:       {self.frequency_selected}")
        print("─" * 60)

        # Subjective Symptoms: Pulled from Side_Effects_Tracker and Symptom_Severity_Assessment
        print(
            f"CURRENT ISSUE: {self.symptom_identification_selected} ({self.symptom_area_selected})")
        print("\nREPORTED SEVERITY (0-10):")
        for symptom, score in self.symptom_selection.items():
            alert = "⚠️" if score >= 8 else "•"
            print(f"  {alert} {symptom}: {score}")

        print("═" * 60)
        print("REPORT COMPLETE - FORWARDED TO CLINICAL DASHBOARD")
        print("═" * 60)


patients = 0
while patients != 100:

    app = Clinical_Summary(name="", age=0, sex="",
                           weight=0.0, height=0.0, BMI=0.0)

# --- PHASE 1: Administrative ---
    app.patient_registration_step1()
    app.patient_registration_step2()
    app.patient_registration_step3()

# --- PHASE 2: Triage & Background ---
    app.clinical_red_flag()         # Safety check
    app.verify_consultation_type()  # Oncology branch
    app.Pathology_information()     # Diagnostic branch

# --- PHASE 3:  Treatment & Symptoms  ---
# (Medications, Dosages, Symptom Localization/ID)

    app.add_treatment()
    app.add_medication()
    app.medication_dosage()
    app.medication_frequency()
    app.symptom_localization()
    app.symptom_identification()
    app.assess_symptom()
    # Verification
    app.final_regimen_verification()
# ---  Clinical Context  ---
    app.functional_status()
    app.test_verification()
    app.patient_concern()


# --- PHASE 5: Output ---
    app.generate_professional_report()
    patients += 1
if patients == 100:
    print("\n" + "═"*60)
    print("DAILY CAPACITY REACHED")
    print("═"*60)
    name = input("Please enter your name: ")
    print(f"Hey {name}, unfortunately our 100 daily capacity was reached. Please return tomorrow at 8:00 AM.")
