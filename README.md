# WatchYourProfanityBot
A Discord Bot to censor swearwords/cuss words.
![](https://tenor.com/view/watch-your-mouth-watch-your-profanity-watch-it-gif-5600117)

This started as a fun way to learn the discord API and discord.py.
Currently on trying to make this a bit more than that, an actual usable bot. Please add your desired words to censor to the swears.txt
<br>
# Hosting on Heroku
For the easiest experience I will suggest cloning/forking this repo as a private repo.
<br>
# Setting up the discord bot
1. Create a discord developer account. - https://discord.com/developers/
2. Create a new application
 
![image](https://user-images.githubusercontent.com/65454356/149580620-f5e9820f-df76-4214-be92-333b62a3fa55.png)
3. Add a bot name

![image](https://user-images.githubusercontent.com/65454356/149580696-eab86a32-bb2d-44c6-a1c6-1dfe8914fab7.png)

4. Go to the bot section and click 'Add Bot' and then click 'Yes. Do it!'

![image](https://user-images.githubusercontent.com/65454356/149580820-c160a7f8-9338-4240-a761-75ad247d7ba2.png)
5. Go to the OAuth Tab and select URL Generator > Tick the bot box

![image](https://user-images.githubusercontent.com/65454356/149581253-0eb16b85-d244-4a87-9f87-49853d1a0ca2.png)
6. Select the following bot permissions. > Send Messages, Send Messages in Threads, Manage Messages, Embed Links, Attach Files

![image](https://user-images.githubusercontent.com/65454356/149581466-45c912a3-db5f-4ed8-b7e1-4dca97dbe758.png)
7. Click the copy Generated URL and paste into your browser.

![image](https://user-images.githubusercontent.com/65454356/149581622-3f8503fd-235e-4a9c-ba20-9c706dbc0e7e.png)
8. You should see a dialog for adding the bot to a server. Select a server and click continue. Follow the reCaptcha steps.
9. The bot should be added to your selected server.

# Setting up Heroku
1. Go the bot tab and click the Copy Token button.

![image](https://user-images.githubusercontent.com/65454356/149582005-1074030b-317d-4651-958e-8b44f5cc8218.png)

2. Navigate to the .env file in your cloned repo, click on the file and then click the pencil icon to add your Discord Token. (Please make sure you do not have this repo set to public! If it is anyone can see your discord bot token!)

![image](https://user-images.githubusercontent.com/65454356/149582340-4d96b2a8-305b-493e-a494-cb690cbd9b30.png)

![image](https://user-images.githubusercontent.com/65454356/149582364-ec7aa663-4274-43b4-a236-133e5777ea4d.png)

3. Replace yourDiscordTokenHere with your discord token.
4. Navigate to Heroku to setup your Heroku account. - https://signup.heroku.com/login
5. Complete the signup process by confirming your email.
6. Create your new Heroku app by New > Create new app.

![image](https://user-images.githubusercontent.com/65454356/149582946-646fdadb-b632-44ea-a028-cbdad488eb5b.png)

7. Give your app a name and click Create app

![image](https://user-images.githubusercontent.com/65454356/149583058-85bc47ca-3aef-4c36-9f46-2c8dd91d2cb9.png)

8. Under the 'Deployment method' tab click the 'GitHub - Connect to GitHub' button. > Search your repo name and click connect.

![image](https://user-images.githubusercontent.com/65454356/149583361-9b5a6555-2cab-48b0-90a3-3024fbfee653.png)

9. Navigate to the 'Settings' tab and the scroll down to the 'Buildpacks' section. Click the 'Add buildpack' button and select Python and click 'Save changes'.

![image](https://user-images.githubusercontent.com/65454356/149583706-6eef9418-3aac-4684-88e0-fc680478d200.png)

10. Almost at the end! Navigate back to the 'Deploy' tab, scroll down to the 'Manual deploy' section. Click 'Deploy branch' - main should be selected.

![image](https://user-images.githubusercontent.com/65454356/149583888-a0071593-79a0-4afd-b45a-c8aa0ed37bdf.png)

12. Navigate to the 'Resources' tab and Find the 'Free Dynos' sectio. Select the pencil icon and enable the 'worker python3.py' and click confirm.

![image](https://user-images.githubusercontent.com/65454356/149584632-98cc523f-0aac-4b41-b053-c925799fa8f2.png)

![image](https://user-images.githubusercontent.com/65454356/149584693-d93a56fa-60b8-4078-8875-58ff014782ab.png)

# You did it!:sunglasses:
