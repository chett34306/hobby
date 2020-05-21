

Inspiration and Credits:
Discussion with Mohan Devidi for Trish reading proof

What does this skill do?
-"Open Daily Journal" on Alexa
- Gives directions to use it
- Can ask for Trish or Rhea article or dated article like may fifth article of april third two thousand twetnty

What Tech Stack?
AWS: (use praveen78@hotmail.com account for dev)
- S3 bucket to post daily writings by Trish and Rhea into respective buckets, and images.
- Python for lambda_function.py as lambda to drive various intents in Alexa Skill.
- Designed Alexa Skill in AWS called "Daily Journal" with intents, utterance, etc.


Dev Environment:
- Setup pycharm community edition
- create python project (or you can open existing project)
- pip install ask-sdk-core, boto3, etc. (for this project everything is already installed in the project folder)
  - pip install <<package_name>> -t . (to install in current directory)

How to Test:
- Build the project and zip all the files under this "dailyjournal" folder.
- Upload the zip file into the lambda function (daily journal)
p.s. currently daily journal is using inline code and cerfified that way.
- Use "open daily journal" command to start testing on alexa.

What is Design:
- User uses voice to open the daily journal app.
- learn about daily journal.
- follows directions from the app.

What are possible additions/improvements?
- read text, audio and video files.
