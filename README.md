# Craft Application

In fulfilment of the solo project assignment due Monday week 7 at QA consulting.

## Index
[Brief](#brief)
   * [Solution](#solution)
   
[Architecture](#architecture)
   * [CI Pipeline](#CI)
   
	
[Testing](#testing)
   * [Report](#report)

     
[Deployment](#depl)
   * [Technologies Used](#tech)
     
[Front End Design](#FE)

[Overview](#group)

[Improvements for the Future](#improve)

[Authors](#auth)

[Acknowledgements](#ack)

<a name="brief"></a>
## The Brief

As a group we were required to create an application using a micro service architecture that when deployed will be able to handle rolling updates without causing any interruptions to the user. As our final project we are required to utilise all of the skills and technologies we have learned over the last 12 weeks to make it run in the most agile way. 


<a name="solution"></a>
### Solution

We took the time to do some brain storming and each came up with three ideas from which we decided on an art app which eventually became a craft app. The user will press a generation button which will then provide them with a colour, a medium, a subject matter and a number of shades. The idea behind our app is that using the outputs the user can then go away and create the output given. 

<a name="architecture"></a>
## Architecture

As part of this brief we were required to create a micro service architecture to determine how our different services would communicate with each other in order to make the application run. 
Service one:

A user loads the webpage which will show them a generator button.

Service two & three:

Once the user has pressed the generate button a request will be sent to both services simultaneously. 
-	Service 2 will randomly generate a colour 
-	Service 3 will randomly generate a medium
Both of the outputs for each service will then be sent to service 4.

Service four:

Once this service has received the outputs for both service two and three it will then generate a subject matter and number of shades based off the information it has previously been given. 
Once all of this information has been brought together it will then be sent back to service one where it will be displayed to the user.

User Journey 

The page is loaded and the user presses the generate button.
Because the button was pressed a colour and a medium is randomly generated. 
The back end then decides the subject matter and the number of shades based upon the colour and the medium previously created, which is then displayed for the user. 
All of this is then stored in a database



<a name="erd"></a>
## CI Pipeline

. Source code – Visual Studio code
. Version Control System – Github
. Project Tracking – Trello
. CI Server – Jenkins
. Build Tool – Azure/Docker
. Automated testing – Pytest/Selinium 
. Testing Enviroment – Terraform 
. Staging Enviroment – Kubernetes
. Live Enviroment – Kubernetes 


## Risk Assessment 

Before staring to build our application we wanted to look into all the different risks that we felt we might face during the building of our application. At different stages dring the development process we revisited our risk assessment form to adjust it to what we felt would happen during the different stages of our build. I also ment that we could go in and amment different risk levels once we had either got past them or been able to reduce the risk. 



#### Delivered solution
.



<a name="testing"></a>
## Testing

Throughout the different stages of our development process it was important to test the different services to ensure that they work both together and separately. 


### Report




<a name="tech"></a>
### Technologies Used

. Visual studio Code
. Python
. Linux Scripting 
. [Trello](https://trello.com/b/f0BXMr16/sofia-project-2)
. [Git](https://github.com/Alexandracope/SOFIA-project-2)
. Jenkins
. Microsoft Azure
. Selinium
. Pytest
. Docker
. Terrafrom
. Kubernetes

<a name="FE"></a>
## Front End Design


<a name="improve"></a>
## Overview of working proccess 

Overall, our group has worked really well together from the beginning we had clear roles within our team and throughout the project we had continued to be happy with these. During the beginning of the project we worked very quickly to get our services up and running, before later working on the second phase of our application. 

When it came to any problems that we either encountered as a group or on individual levels, we were able to come together and workout what the problem was and help each other to come to a solution, occasionally needing some outside help from tutors. 

As a group we have been able to really show our individual skill sets throughout the making of our application and where different members didn’t have the same understanding as others. We were able to help bring them up to the same level so that we can all understand exactly what is going on at each stage.


<a name="improve"></a>
## Improvements for the Future

When creating our Trello board and using MoSCoW there were aspects to our application that we were not able to get done within the time along with also doing our continued studies. In the future upon completing the course we would like to either as a group or individually be able to complete some of these. For example, to make our application a little it more personal to the user we would have an account they would sign into so that every time they generate it will store their result in a database with relationships in its tables so it doesn’t get the same result again. 


<a name="auth"></a>
## Authors

Yassir Satti - Product Owner
Tiffany Cowman - Developer 
Alexandra Cope - Scrum Master

