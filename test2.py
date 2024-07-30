import os

def find_image_folder(root_folder, image_path):
    image_filename = os.path.basename(image_path)
    for folder_name, subfolders, filenames in os.walk(root_folder):
        if image_filename in filenames:
            return folder_name
    return None

def main():
    file = open("data/result.txt", "w")
    l = []
    root_folder = "nurse"  
    folder_path = r'tesing_image'
    items = os.listdir(folder_path)
    first_item = os.path.join(folder_path, items[0])
    image_path = first_item
    image_folder = find_image_folder(root_folder, image_path)

    if image_folder:

        if image_folder == 'nurse/Normal Person ECG ':
            file.write(''' \n\n\n\n Your ECG report is Normal 
                No need to worry !
                It means their heart is functioning well without any significant abnormalities.
                This is reassuring and indicates a healthy heart.To maintain this positive outcome,
                it is recommended to continue practicing a healthy lifestyle, including regular exercise,
                a balanced diet, sufficient sleep, stress management,and avoiding tobacco and excessive alcohol. 
                Routine check-ups with a healthcare provider are important to monitor overall cardiovascular health 
                and address any concerns.Although the ECG is normal, it's crucial to be aware of any 
                unusual symptoms -and promptly consult a healthcare professional if experiencing chest pain, shortness of 
                breath, palpitations, or dizziness.  \n\n''')
            file.close
        

        elif image_folder =='nurse/ECG  of Patient that have History of MI':
            

            file.write(''' \n\n\t Your ECG report is not normal!! \n\t it says you was the patient of Myocardial Infarction  \n\nSo here are some precautions you should take to avoid risk : 
                
                1. Take prescribed medications regularly.
                2. Follow a heart-healthy diet.
                3. Engage in regular physical activity as advised by the healthcare provider.
                4. Quit smoking and avoid exposure to secondhand smoke.
                5. Manage stress through relaxation techniques and stress-reducing activities.
                6. Maintain a healthy weight and manage any underlying conditions like high blood pressure or high cholesterol.
                7. Attend follow-up appointments with the healthcare provider.
                8. Participate in a cardiac rehabilitation program, if recommended.
                9. Be aware of warning signs or symptoms of another heart attack and seek immediate medical help if they occur.
            10. Communicate any concerns or changes in symptoms to the healthcare provider.''')
            file.close
        elif image_folder =='nurse/ECG of  abnormal heartbeat':
            file.write('''\n\n\t Your ECG report is not normal!! \n\t Your Hearbeats are not normal \n\t Please refer a doctor immediately!
                -Having abnormal heartbeats, also known as arrhythmias, means that the heart's rhythm is 
                irregular or abnormal. It is essential to seek medical attention to properly diagnose and manage 
                the condition. Treatment for abnormal heartbeats may involve medication, lifestyle modifications, 
                and in some cases, medical procedures. Regular monitoring and follow-up with a healthcare provider 
                are crucial to ensure the condition is properly managed and potential complications are addressed.


                1.  Follow the prescribed treatment plan and take medications as directed by the healthcare provider.
                2.  Avoid triggers that can worsen the irregular heartbeats, such as excessive caffeine, alcohol, or 
                    certain medications.
                3.  Manage stress through relaxation techniques, exercise, and seeking support from loved ones.
                4.  Maintain a healthy lifestyle by adopting a heart-healthy diet and engaging in regular physical activity.
                5.  Quit smoking and avoid exposure to secondhand smoke.
                6.  Limit or avoid the use of stimulants like energy drinks or recreational drugs that can affect heart rhythm.
                7.  Ensure regular check-ups and follow-up appointments with the healthcare provider to monitor the condition 
                    and adjust treatment as needed.
                8.  Be aware of symptoms that may indicate a worsening of the condition and promptly report any changes to the 
                    healthcare provider.
                9.  Consider wearing a medical alert bracelet or necklace to inform others of the condition in case of emergency.
            10.  Educate oneself about the condition, its triggers, and appropriate self-care measures to better manage and 
                    prevent complications.\n\n ''')
            file.close
        elif image_folder=='nurse/ECG Images of Myocardial Infarction Patients ':
            file.write('''\n\n\t Your ECG report says You have Myocardial Infarction  
                It is a serious medical condition that requires immediate attention and proper care. 
                Myocardial infarction occurs when the blood flow to a part of the heart is blocked, 
                leading to damage or death of the heart muscle. Treatment for myocardial infarction 
                usually involves a combination of medical interventions and lifestyle changes. 
                This may include medications to reduce blood clotting, relieve chest pain, 
                and manage underlying risk factors such as high blood pressure and high cholesterol. 
                Lifestyle changes may involve adopting a heart-healthy diet, regular exercise, quitting 
                smoking, and managing stress. Cardiac rehabilitation programs may also be recommended to
                aid in recovery and provide education and support. It is important for patients who have
                had a myocardial infarction to closely follow their healthcare provider's advice, take prescribed
                medications regularly, attend follow-up appointments, and make necessary lifestyle modifications to 
                prevent further complications and improve heart health.
                \n\n\t Here are some emergency precautions for a patient experiencing a myocardial infarction (heart attack):
                
                    Call for immediate medical help: 
                                    If you or someone around you is experiencing symptoms of a heart attack, 
                                    such as chest pain or discomfort, shortness of breath, pain radiating to 
                                    the arm, jaw, or back, nausea, or lightheadedness, call emergency services
                                    or your local emergency number without delay.
                    
                    Stay calm and rest: 
                                    It is important to stay calm and encourage the person experiencing a heart 
                                    attack to rest in a comfortable position. Loosen any tight clothing and keep 
                                    them calm and reassured until medical help arrives.

                    Chew or swallow aspirin: 
                                    If the person is not allergic to aspirin and it is readily available, they can 
                                    chew or swallow a regular aspirin (325 mg) to help prevent further blood clotting. 
                                    However, it is crucial to consult a healthcare professional for proper guidance.

                    Do not attempt to drive: 
                                    It is not safe for someone experiencing a heart attack to drive themselves to the
                                    hospital. Emergency medical services have the necessary equipment and expertise to 
                                    provide immediate care during transportation.

                    Avoid self-medication: 
                                    While waiting for medical help, it is important to avoid taking any 
                                    other medications or attempting self-treatment without proper medical 
                                    guidance. Only take medications prescribed by a healthcare professional.\n\n''')
            file.close
    else:
                
        print(f"\n\n\nThe image '{image_path}' was not found in any folder.")
    os.remove(first_item)
if __name__ == "__main__":
    main()
