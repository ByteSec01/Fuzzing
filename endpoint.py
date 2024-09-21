#ByteSec01
import requests # requests useg for protocol http and control in response & request

target = input("Enter URL: ").strip() # strip = delete space
wordlist = input("Enter wordlistFile: ").strip()

with open(wordlist, 'r') as file: # read file 
    word = [line.strip() for line in file] # for formal 
    print("Scanner...")

    for endpoint in word: 
        url = f"{target}/{endpoint}"
        response = requests.get(url) # send request for website

        if response.status_code == 200: # get only 200 
            print(f"found: { url}")
        
