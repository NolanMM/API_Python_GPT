# Minh note

# Step 1: Install python
# First Download python 3.10 from website https://www.python.org
# Check python version in terminal: python -V

# Step 2: Install the pip for python
# Open default Terminal
# type curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# Allow curl time to download the script onto your Mac.
# Type python3 get-pip.py
# Wait untill it successful downloaded

# Step 3: Install OpenAi library to import
# Open default Terminal
# Type pip install openai
# Wait untill it successfull downloaded

# How to run the program from Terminal
# Go to the folder that contain the .py file
# Right Click on the folder and select 
# New Terminal at Folder
# type python3 Chat_GPT_API_Console_App.py

# How to use
# Option 1: [Type Quit or quit or QUIT to safe escapse the program]
# Option 2: [Type the question and wait for the respond]

# How to configure the program
# 
# \* Configure the api key: Take API key from your accound and paste into openai.api_key


import openai

openai.api_key = "Paste Your API KEY HERE"

print('Enter the question below or type \'Quit\' to escapse the application')

while True:
	ask = input('Question: ')
	if ask == 'Quit' or ask == 'quit' or ask == 'QUIT' :
		break
	else:
		response = openai.Completion.create(
  			model="text-davinci-003",
  			prompt=ask,
  			temperature=0.9,
  			max_tokens=150,
  			top_p=1,
  			frequency_penalty=0,
  			presence_penalty=0.6,
  			stop=[" Human:", " AI:"]
			)

		text = response['choices'][0]['text']
		print ('Reply: '+text)