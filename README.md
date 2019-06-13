# Sentiment-Analysis
It analyse the sentiment of people towards a person (Specified by the user) by fetching the tweets from twitter.

Pre - requisite
Basic Knowledge of Python and machine learning

To do this we need to use twitter API 
for This Follow the steps given below

1) Sign in to twitter developer mode using your twitter account.
click on this given link - https://developer.twitter.com/

2) Click on "create app" button.

3) Fill th required details
 --App name
 --App descrption(maximum of 32 characters)
 --Website URL
 --Callback URL
 --Term of service URL
 --Privacy policy URL
 --Organization name
 --Organization website URL
 --Tell us how this app will be used (required)
 (* Fill all the above required field)
 
 4) Click on "create App" tab.
 
 5) Click on "Keys and access tokens" tab.
 
 
We will use the above obtained keys in our code

Library Used 

---- tweepy library
This library is used to access twitter API, By this it will fetch some tweets from your account 

Install this using pip
	Write the following command on python console
		pip install tweepy

---- textblob library
This library is used to devide the given data into array of words and then we used to count the action word.

	action words - 
		happy
		sad
		joyful
		remorse
		unfaithful
		etc...    
		The words which shows some emotions are called as action word.
	
	Install this using pip
		write the following command on python console
			pip install textblob

Sentimental Analysis give the result in polarity Scale from (-1 to 1)

You can get the 4 keys from your created twitter API:
	1) Consumer Public Keys
	2) Consumer secret Key
	3) Access token
	4) Access token secret
	
	These key will help you in fetching tweets from your twitter account.
	
For Authentication Of tweets
we use :- 
	OAuthHandler(Consumer_public_key, Consumer_private_key);
	
	this is a method of tweepy library taking two arguments
	
For accessing the tweets We will call-
	set_access_token() method
		It takes two argument Access token and access token secret.
		
		
Now the user will be prompted to enter the name for which they want to do sentimental analysis


	print("Enter the name you want to review about")
	x = input(">>")
	public_tweet = api.search(x)
	
api.search() - will search for the tweets in which the name mentioned by the user is present.


This line of code will return the polarity scale ranging from (-1 to 1)

 	k = result_analysis.sentiment.polarity
	
Now you can define the condition to evaluate the result
	For my case I have define following condition
		
		 if k<0 :
        b=b+1
    elif k>0.1 :
        g = g + 1
    else :
        a = a + 1
		
		** You can change the range according to your wish.


Now to write the answer you can also manipulate the below mentioned conditioned.

	if a>b and a>g :
    	print("Average")
	elif b>a and b>g :
		print("Bad Impact")
	else :
		print("Good Impact")
		
You are done with the code
	->run the code and see output.





 
 





		
