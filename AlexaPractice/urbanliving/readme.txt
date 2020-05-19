

Inspiration and Credits:
Matt Goyer at urbnlivn.com in seattle

What does this skill do?
-"Open Urban Living" on Alexa
- Gives info about "Urban Living"
- Can subscribe to newsletter, and potential to do more like unsubcribe, listings, sales info etc.

What Tech Stack?
AWS: (use praveen78@hotmail.com account for dev)
- DynamoDB for urbanliving_info.txt
- Python for urbanliving.py as lambda to drive various intents in Alexa Skill.
- Designed Alexa Skill in AWS called "Urban Living" with intents, utterance, etc.
- Use S3 bucket called "urbanliving" to store cotnent like images, etc.

Dev Environment:
- Setup pycharm community edition
- create python project (or you can open existing project)
- pip install ask-sdk-core, etc. (for this project everything is already installed in the project folder)

How to Test:
- Build the project
- Upload the zip file into the lambda function (urbanliving)

What is Design:
- User uses voice to open the urban living app.
- learns about urban living.
- follows directions from the app.

What are possible additions/improvements?
- ubsubscribe
- send email
- generate daily new subscribes email
- listing info
- sales info
- content scroll and background changes
- call ph# or alexa
- text feature via alexa (via SNS and taking to alexa)
- open website feature on alexa
