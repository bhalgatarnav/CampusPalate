import pandas as pd
import os
import numpy as np

os.system('cls')
print('-'*101)
print('************************************** Campus Palate ***************************************')
print('************************************ Revolution UC 2024 ************************************')
print()
print("Introducing Campus Palate:\nCampus Palate is a user-friendly interface designed to empower college students, "
      "especially freshmen, in making\ninformed dietary choices at their campus dining centers.\nOur goal is to help "
      "you meet your dietary goals and maintain a healthy lifestyle during your college journey.\n \nWith Campus Palate,"
      "you can:")

print("1. Easily access information about nutritional value and ingredients of various food items offered at your "
      "dining centers.")
print("2. Make informed choices that align with your dietary preferences and restrictions, such as allergies, vegan, "
      "vegetarian, or gluten-free options.")
print("3. Discover new and exciting dishes that meet your dietary needs and expand your culinary horizons.")
print("4. Stay on track with your health and wellness goals by making mindful food choices that support your overall "
      "well-being.")

agree = input("Lets start: (Y/N) ")

if agree == 'Y':
    os.system('cls')

    # Now the user should get a form to answer the personal information and save it in the csv file using the panda commands
    # The form alignment should be interactive and formatted properly.
    print('************************************** Campus Palate ***************************************')
    print('************************************ Revolution UC 2024 ************************************')

    name =        input("What is your name?                  ")
    age =         input("What is your age?                   ")
    weight =  int(input("What is your weight?                "))
    height =float(input("What is your height in meters       "))
    phone =   int(input("What is your phone number?          "))
    gender =      input("What is your gender?                ")
    print()
    dic = {'Name':[name],'Age':[age],'Weight':[weight],'Height':[height],'Phone':[phone],'Gender':[gender]}
    df2 = pd.DataFrame(dic)
    print(df2)
    print()
    # Calculate the BMI of teh user to report it to them for better deciding the goals.
    # The BMI should take the gender into consideration to declare the category they fall into.

    calculate_bmi = weight/(height**2)

    print("Note: The calculated BMI and the category is just an estimate based on the values entered by the user.\n")
    print("These values and category are subject to change and should be consulted by a doctor.\n ")
    # Determining the categories using if else ladder

    if calculate_bmi < 18.5:
        print("Your BMI category is Underweight")
    elif calculate_bmi < 25:
        print("Your BMI category is Normal Weight")
    elif calculate_bmi < 30:
        print("Your BMI category is Overweight")
    else:
        print("Your BMI category  is Obesity")


    # Preparing the form for user to enter the dietary preferences to personalise the meal for the student
    print('-'*101)
    print()
    print("This is your chance to tell us about any specifications preferred in the meal you are looking for.\n")
    veg = input("What is your preferred meal type: Vegetarian [V], Vegan [VE], Non Vegetarian [NV] \n\n")
    nuts = input("Do you have allergy for nuts? [Y/N]  \n\n")
    lactose = input("Are you Lactose intolerant? [Y/N] \n\n")

    ######
##  Take the inputs and save them in the excel file associated with the user.
    ######

    print("\n\n")
    print('-' * 101)
    print()
    print("Its Time to Set Goals\n")
    cal =     input("What should be your expected calories intake? [High/Low]: ")
    protein = input("What should be your expected protein intake?  [High/Low]: ")

    ######
##  Take the inputs and save them in the excel file associated with the user.
    ######

    print("All the inputs and preferences are successfully saved.")
    print('Press \'ENTER\' to continue')
    input()
    os.system('cls')

    # Now categorise the data and ensure that all the goals are met.
    # The menu will be included in a dataframe using pandas.

    print('************************************** Campus Palate ***************************************')
    print('************************************ Revolution UC 2024 ************************************')

    print("\n We currently support the meal plan for Center Court and soon we plan on expanding the service")
    print("\n Here is the dinner menu for the center court on average day.")
    print()
    df1 = pd.read_csv(os.getcwd() + '\\CCD.csv', usecols = ['Category','Item'])
    print(df1)
    df2 = pd.read_csv(os.getcwd() + '\\CCDA.csv', usecols = ['Category','Item','Calories','Protein (g)','Fat (g)','Cholesterol (mg)','Sodium (mg)','Carbohydrates (g)','Meal Pref','Allergies'])
    print('Press \'ENTER\' to continue')
    input()
    l1 = df2.loc[:,'Category']
    l2 = df2.loc[:,'Item']
    l3 = df2.loc[:,'Calories']
    l4 = df2.loc[:,'Protein (g)']
    l5 = df2.loc[:,'Fat (g)']
    l6 = df2.loc[:,'Cholesterol (mg)']
    l7 = df2.loc[:,'Sodium (mg)']
    l8 = df2.loc[:,'Carbohydrates (g)']
    l9 = df2.loc[:,'Meal Pref']
    l10 = df2.loc[:,'Allergies']


    if veg == 'V':
        for i in range(len(l9)):
            if l9[i] == 'V':
                print(str(i) + " " + l2[i])
        protsum = 0
        n = 0
        calsum = 0
        while(n==0):
            calnum = int(input("Enter the number of the food item that you'd like to eat. (Enter -1 to exit): "))
            if(calnum == -1):
                break
            else:
                calsum += l3[calnum]
                protsum += l4[calnum]
        if(cal == "Low" and calsum > 500):
            print("It is recommended to eat a few less items")
        elif(cal == "High" and calsum < 300):
            print("It is recommended to eat a few more items")
        else:
            print("You're all set for calories!")
        if(protein == "High" and protsum < 8):
            print("It is recommended to eat items with more protein")
        elif(protein == "Low" and protsum < 25):
            print("It is recommended to eat items with a little less protein")
        else:
            print("You're all set for proteins!")
            
    elif veg == 'VE':
        for j in range(len(l9)):
            if l9[j] == 'VE':
                print(str(j) + " " + l2[j])
        n = 0
        calsum = 0
        protsum = 0
        while(n==0):
            calnum = int(input("Enter the number of the food item that you'd like to eat. (Enter -1 to exit): "))
            if(calnum == -1):
                break
            else:
                calsum += l3[calnum]
        if(cal == "Low" and calsum > 500):
            print("It is recommended to eat a few less items")
        elif(cal == "High" and calsum < 300):
            print("It is recommended to eat a few more items")
        else:
            print("You're all set for calories!")
        if(protein == "High" and protsum < 8):
            print("It is recommended to eat items with more protein")
        elif(protein == "Low" and protsum < 25):
            print("It is recommended to eat items with a little less protein")
        else:
            print("You're all set for proteins!")
    else:
        for k in range(len(l9)):
            if l9[k] == 'NV' or l9[k] == 'V' or l9[k] == 'VE':
                print(str(k) + " " + l2[k])
        n = 0
        calsum = 0
        protsum = 0
        while(n==0):
            calnum = int(input("Enter the number of the food item that you'd like to eat. (Enter -1 to exit): "))
            if(calnum == -1):
                break
            else:
                calsum += l3[calnum]
        if(cal == "Low" and calsum > 500):
            print("It is recommended to eat a few less items")
        elif(cal == "High" and calsum < 300):
            print("It is recommended to eat a few more items")
        else:
            print("You're all set for calories!")
        if(protein == "High" and protsum < 8):
            print("It is recommended to eat items with more protein")
        elif(protein == "Low" and protsum < 25):
            print("It is recommended to eat items with a little less protein")
        else:
            print("You're all set for proteins!")