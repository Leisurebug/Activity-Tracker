from activity import Activity
import matplotlib.pyplot as plt
from datetime import datetime

def main():
    print(f"Running Activity Tracker: ")
    activity_file_path= "activity.csv"
    
    n=int(input("1.Enter a activity record\n2.Display graph\n3.Do both\nEnter your choice: "))
    if n==1:
        act = get_user_activity()
        save_activity_to_file(act, activity_file_path)
    elif n==2:
        Visualising_user_activity(activity_file_path)
    else:
        act = get_user_activity()
        save_activity_to_file(act, activity_file_path)
        Visualising_user_activity(activity_file_path)

def get_user_activity():
    print(f"Getting user activity information: ")
    activity_name = input("Enter Activity name: ")
    activity_time = float(input("Enter time taken by the category in hours: "))
    print(f"You've entered {activity_name}, {activity_time}")
    
    activity_categories = [
       "Study", 
       "Self learning", 
       "Project", 
       "Exercise",  
       "Practice", 
       "Contest",
       "Other",
    ]
    
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(activity_categories):
            print(f" {i+1}. {category_name}")
            
        value_range= f"[1 - {len(activity_categories)}]"
        selected_Index = int(input(f"Enter a category number {value_range}: ")) -1
        
        if(selected_Index in range(len(activity_categories))):
            selected_category = activity_categories[selected_Index]
            new_act = Activity(name=activity_name, category=selected_category, time=activity_time )
            return new_act
        else:
            print("Ivalid category. Please try again!")
            
def save_activity_to_file(act, activity_file_path):
    print(f"Saving user activity: {act}")
    today = datetime.now().strftime('%d-%m-%Y')
    with open(activity_file_path, "a") as f:
        f.write(f"{today}, {act.category}, {act.name}, {act.time}\n")

def Visualising_user_activity(activity_file_path):
    choosen_date = input("Enter the date (DD-MM-YYYY): ")
    print(f"Visualizing user activity :")
    activities: list[Activity]= []
    
    with open(activity_file_path, "r")  as f: 
        lines = f.readlines()
        for line in lines: 
            activity_date, activity_name, activity_category, activity_time = line.strip().split(",")
            if activity_date == choosen_date:
                line_activity = Activity(
                    name=activity_name, category=activity_category, time=activity_time
                )
                activities.append(line_activity)

    if not activities:
        print(f"No activities recordrd for{choosen_date}.")
        return 
    
    time_by_category ={}
    for activity in activities:
        key = activity.category
        if key in time_by_category:
            time_by_category[key] +=activity.time
        else:
            time_by_category[key] =activity.time
    
    categories = list(time_by_category.keys())
    times = list(time_by_category.values())
    
    plt.figure(figsize=(10,6))
    plt.bar(categories, times, color='skyblue')
    plt.xlabel('Activities')
    plt.ylabel("Time Spent (in hrs)")
    plt.title(f"Activity Chart of {choosen_date}")
    plt.show()
    
if __name__=='__main__':
    main()