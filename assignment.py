import sys
import os
import requests
import markdown
from bs4 import BeautifulSoup
from datetime import date,datetime
from fetch_wiki_table import fetch_wiki_table_data


wiki_url = 'https://github.com/prajaktag-20/TestJava/wiki/Home'
vacation_date = []

changed_files_list=sys.argv[1:]
changed_files=changed_files_list[0].split('\n')

changed_files.remove('assignment.py')
changed_files.remove('logfile.txt')
changed_files.remove('fetch_wiki_table.py')




#changed_files=["leogang/hangman.cpp","finale/ligure/rollercoaster.cpp"]


def main(): 
    table_data = fetch_wiki_table_data(wiki_url)
    if table_data:
       for row in table_data:
          vacation_date.append(row)

    current_date = date.today()
    formatted_date = datetime.strftime(current_date,'%m/%d/%Y')
    def Isonvacation(user):
        for record in vacation_date:
            if record['user'] == user and record['from'] <= formatted_date <=record['Till']:
                return True
            else:
                return False

    # Function to find .reviewer file by traversing downwards
    def find_reviewer_file_downwards(start_dir):
        current_dir = os.path.abspath(start_dir)
        
        # Traverse downwards from current directory
        while current_dir != '/':
            reviewer_file = os.path.join(current_dir, '.reviewer')
            if os.path.exists(reviewer_file):
                return reviewer_file
            current_dir = os.path.dirname(current_dir)    
        return None

    def read_reviewer_file(file_path):
        with open(file_path, 'r') as f:
            content = f.read().strip()
        return content


    for file in changed_files:
        full_path = os.path.abspath(file)
        ##print(full_path)
        reviewer_file = find_reviewer_file_downwards(full_path)
        if reviewer_file:
            content = read_reviewer_file(reviewer_file)
            print(os.path.basename(file) + " - " + content)
            username = content.split(':')
            user_list = username[1].split(',')
            
            for usr in user_list:
                result = Isonvacation(usr.strip())
               ## print(usr + '-' + str(result))
                if result:
                    user_list.remove(usr)
            
            user_count = len(user_list)
            print(user_list)
            default_user = ["neff", "schurter"]
            if user_count < 2:
                user_list.extend(default_user)
                print(user_list)
        else:
            print("No .reviewer file present")

if __name__ == "__main__":
    main()        



    
   
