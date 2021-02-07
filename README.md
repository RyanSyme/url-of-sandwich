# **Milestone 3 – Url of Sandwich**

## **Sandwich Recipe Database**

---

<!-- ![Url of SAndwich](multi-screenshot) -->
This webpage has been created to showcase the skills I have learned in the Datacentric Developement section of the Code Institute Full Stack Web Developer course; this is the third of four projects that I will be creating for the course.
For this project I have chosen to create a sandwich recipe website using the MongoDB database, Python, Flask and Jinja.
The reason for this selection is to create a website that users can interact with by joining the website, being able to view other people's creations and adding there own sandwiches to the database.

---

### **_Table of contents:_**

1. [Description](#sandwich-recipe-database)
2. [UX](#ux)
    1. [The Objective](#the-objective)
    2. [Wireframes](#wireframes)
    3. [Styling](#styling)
    4. [User Stories](#user-stories)
3. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Features Left to Implement](#features-left-to-implement)
4. [Technology Used](#technology-used)
5. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Manual Testing](manual-testing)
6. [Deployment](#deployment)
    1. [Remote Deployment](#remote-deployment)
    2. [Local Deployment](#local-deployment)
7. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Acknowledgements](#acknowledgements)

---

## **UX**


### **The Objective**

The objective of this website is to provide users that love sandwiches with an application that allows them to sign up, login, create and edit their own sandwiches as well as browse the creations of other users for inspiration.

On this site a user is able to:

- view sandwich recipes created by other users
- read the ingredients needed for each sandwich
- read the instructions on how to create each sandwich
- see which user created each sandwich
- see an image of each sandwich (if added by the creator)
- sign up to an account
- login as an existing user
- log out of their account
- view their profile page showing the sandwiches they have created (if any)
- edit sandwich recipes they have created
- delete sandwich recipes they have created

### **Wireframes**
<!-- ![Wireframes](wireframe screens) -->

<!-- you can find a full size PDF of the Wireframes [here](wireframe pdf) -->

#### **Design Differences**

There are some minor differences from the original conception and the final website.
* Origianlly I planned to have the Login and Sign up in the same place and have only one link in the Nav. I decided it would be cleaner to have a Login section and a sign up section.
* I made the callout image a rolling carousel to make the home page more interesting and inviting.
* I changed the search option from a "main ingredient" search to an "any ingredient" search for ease of use for the user.
* I moved the sandwich description in the "view sandwich" page, from the side of the image to underneath, purely for astetical reasons.
* I removed the "create a new sandwich" button from the profile page, as I felt it was an unnessasary addition.
* I changed the database category from "main ingredient" to "category" for ease of use for the user (if a sandwich has only two ingredients, which is the main one?).

### **styling**

#### *Framework*
Bootstrap and jQuery have both been used to form the structural layout of this website.

#### *Fonts*
The Google font Mali had been used exclusively on the website

#### *Colors*
<!-- * There are four non-image colors used on the website: -->
    
    <!-- ![Colors](coolers screen) -->
    *   #2b2d42 has been used for the main text and buttons
    *   #9fd9de has been used for the Nav, Footer and containers
    *   #ffffff has been used for the some text and boxes
    *   #e6e6e6 has been used for the main background color
    *   #993300 has been used for the blue hover response color


### **User Stories**

* **First Time Visitor Goals**

    * *As a First Time Visitor*, I want to be able to navigate the website simply and easily.

    * *As a First Time Visitor*, I want to access the site across all devices.
    * *As a First Time Visitor*, I want to see other users creations.
    * *As a First Time Visitor*, I want a a way to search other users creations.
    * *As a First Time Visitor*, I want to be able to sign up as a user.
    * *As a First Time Visitor*, I want to add my own creations.
    * *As a First Time Visitor*, I want a page where I can see my own creations.


* **Returning Visitor Goals**

    * *As a Returning Visitor*, I want to be able to inspect and edit my own creations.

    * *As a Returning Visitor*, I want other to view my creations but not edit them.
    * *As a Returning Visitor*, I want to easily navigate to the log in page to view my profile
    * *As a Returning Visitor*, I want to view all of the sandwiches I have added to the site
    * *As a Returning Visitor*, I want to be able to delete any of my own creations I no longer want.
    * *As a Returning Visitor*, I want to be able to log out of the site.

---

## **Features**

* The Project is a multi-page website which uses a MongoDB database and Jinja/Python template management.

    1. The Index page consists of a Nav section and footer section that feature on every page. It also includes an image carousel and a favourite sandwiches section.
    <!-- ![Top](screen)     -->
    <!-- ![Carousel](screen)     -->
    <!-- ![Favourites](screen)     -->
    
    2. The sandwiches section displays the full database of sandwiches that users have created. Each sandwich has its own card with an image of the sandwich, it's name and prep time. Each card also has view sandwich button to allow the user to see each recipe. There is also a search bar allowing the user to search the sandwiches by ingredient.
    <!-- ![Sandwich Cards](screen) -->
    
    3. The Login and Sign Up sections take the customer to the related page, allowing the customer to either login or sign up. The pages have links to each other incase the customer has click the wrong one.
    <!-- ![Login](screen) -->
    <!-- ![Sign Up](screen) -->
    
    4. The add sandwich page has a form which allows the customer to add a sandwich to the database.
    <!-- ![Add Sandwich](screen) -->
    
    5. The profile section shows the user their own creations which they can edit or delete if they wish.
    <!-- ![Profile](screen) -->
    
    6. The log out button logs the user out and returns them to the landing page.
    <!-- ![Log Out](screen) -->

    7. The Earl of Sandwich (Admin) has an additional page where they can add, edit or remove categories.
    <!-- ![Categories](screen) -->

### **Existing Features**

*	The site has been designed to be responsive across all devices

*	The navbar remains on every page, allowing easy navigation at all times, It give the user the ability to move to the home page, add sandwich page, their profile page and to log out.
*	The navbar is styled differently for different screen sizes, changing from a three line “hamburger” dropdown nav on mobile to a traditional full screen navbar on larger screens
*	The user has the ability to sign up and/or login using the relative areas
*	The user can view all creations in the database
*   The user can search through all of the created sandwiches by any ingredient using the search bar.
*	The user has the ability to create, edit or remove any creation of their own making.
*	The footer displays the social media links.
*	The admin has the ability to add, edit or remove categories.


### **Features Left to Implement**

* A 'like' or grading feature that allows user to rate other users sandwiches

* The option to have more than one admin.
* The ability for the user to change password
* A 'Favourite section showing the users person favourites. 

---

## **Technologies Used**

All of the following technologies were used to create this website:-

### **Languages**

*	**HTML5**

*   **CSS3** 
*	**JavaScript**

    have been used throughout the project to create the text, style and functionality of the website.

*	[Python](https://www.python.org/) has been used to run the application

### **Frameworks and Libraries**

*   [Jquery]( https://jquery.com/) were used to implement the carousel function on the image carousel section and to simplify DOM manipulation

*	[MongoDB](https://www.mongodb.com/) has been used to to store the database
*	[Flask](https://flask.palletsprojects.com/en/1.1.x/) has been used to to dynamically generate pages, links, and content within the app
*	[PyMongo](https://pypi.org/project/pymongo/) has been used to connect to and transfer data to MongoDB
*	[Jinja](https://jinja.palletsprojects.com/en/2.11.x/) has been used to template the website
*	[Bootstrap]( https://getbootstrap.com/) was used for layout aesthetics, including grid styling and device responsiveness
*	[GitHub]( https://github.com/) was used to host the website
*	[Gitpod]( https://www.gitpod.io/) was used to code the website

### **Software and Resources**

*	[FontAwesome](https://fontawesome.com/) was used to add icons to the exercise class headers

*	[Gimp]( https://www.gimp.org/) was used to size the images
*	[Balsamiq]( https://balsamiq.com/) was used to create the wireframes of the project
*   [FireShot](https://getfireshot.com/) was used to create the screenshots for the README
*   [Techsini](https://techsini.com/multi-mockup/) was used to style the multi screen mockup
*   [Coolors](https://coolors.co/) was used to create the color palette screenshot
*   [User-Agent Switcher](https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg) was used for testing functionality on different browsers

---

<!-- ## **Testing** -->

<!-- ### **Testing User Stories from the UX Section** -->


<!-- **First Time Visitor Goals** -->

<!-- * *As a First Time Visitor*, I would like to know what the company does upon opening the site. -->
    <!-- *   On opening the website the visitor is met with the main image carousel with an advertisement proclaiming they should visit Norrtälje -->

<!-- * *As a First Time Visitor*, I want to be able to navigate the website simply and easily. -->
    <!-- *	The website has a sticky navigation menu that is always available to allow quick access to each section of the site. -->
    <!-- *	Each section is clearly marked with a header -->

<!-- * *As a First Time Visitor*, I want to access the site across all devices. -->
    <!-- *	The website is responsive across all devices -->
    <!-- *	The website has three different layouts depending on what size screen the customer is using -->

<!-- * *As a First Time Visitor*, I want to find out about Norrtälje. -->
    <!-- *	The about section has some information on the town and the navbar has a button that directs the user to the about section -->
    <!-- *   The info section also has additional information about certain subjects such as restaurants and activities -->

<!-- * *As a First Time Visitor*, I want to find where Norrtälje is situated. -->
    <!-- *   The about section explains where Norrtälje is located -->
    <!-- *   The interactive map shows Norrtälje’s exact position in Sweden. -->

<!-- **Returning Visitor Goals** -->

<!-- * *As a Returning Visitor*, I want to locate the websites social media links to stay up to date with any new content. -->
    <!-- *   The social media links are found on the footer at the bottom of the page -->

<!-- * *As a Returning Visitor*, I would like to be able to search for accommodation in the area -->
    <!-- *	The interactive map has an accommodation button, allowing the visitor to see all of the available accommodation -->

<!-- * *As a Returning Visitor*, I would like to be able to search for restaurants and activities in the area -->
    <!-- *	The interactive map has both a restaurant button and an activities button. -->
    <!-- *   Additionally there are several other buttons including a parking button so visitors can decide where best to park. -->

<!-- * *As a Returning Visitor*, I would like to be able to contact the bureau. -->
    <!-- *   The website has a contact form that can be used to contact the bureau directly by email -->
    <!-- *   The navbar has a contact button that direct the visitor to the contact form -->
    <!-- *   The address and contact details of the bureau are also located in the footer -->

<!-- ### **Code Validation** -->

<!-- #### *W3 Validators* -->

<!-- *    The HTML was Validted at [W3C Markup Validation Service](https://validator.w3.org/).  -->

<!-- ![HTML Validation](assets/readme-files/validator.w3.org.png) -->
<!-- ![HTML Validation](assets/readme-files/validator.w3.org-passed.png) -->

<!-- *    The CSS was validate at [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/). -->

<!-- ![CSS Validation](assets/readme-files/jigsaw.w3.org.png) -->

<!-- *    The Javascript was validated at [JSHint](https://jshint.com/). -->

<!-- ![CSS Validation](assets/readme-files/jshint.com.png) -->

<!-- ### **Manual Testing** -->

<!-- #### *Google Developer Tools* -->

   <!-- *    The websites design responsiveness has been tested on all device sizes using Google Developer Tools. -->

<!-- #### *Testing On Mobile Devices* -->
   <!-- *    Apple iOS -->
   <!-- *    Google Android 7 -->
   <!-- *    Microsoft Windows Phone -->
   <!-- *    Samsung Tizen OS -->
   <!-- *    Nokia Symbian -->
   <!-- *    Mozilla Firefox OS -->
 
<!-- #### *Testing On Browsers* -->
   <!-- *    Google Chrome -->
   <!-- *    Opera -->
   <!-- *    Firefox -->
   <!-- *    Apple Safari -->
   <!-- *    Microsoft Explorer -->
   <!-- *    Microsoft Edge -->
    
<!-- #### *Testing On Operating Systems* -->
   <!-- *    Microsoft Windows -->
   <!-- *    Linux -->
   <!-- *    Apple Mac OS -->
   <!-- *    Google Chrome OS -->
   <!-- *    IBM Warp -->

    
<!-- #### *Issues Found* -->

<!-- *   An issue was found with the carousel on mobile devices, the resizing would make the text too large and distort the carousel. -->
    <!-- *   The issue was resolved with some changes to text sizes in the media queries -->

<!-- *   JSHint found a missing semi-colon in my JavaScript. -->
    <!-- *   The issue was fixed by adding the semi-colon -->

<!-- *   I was unable to make EmailJS function using the way I had been taught by Code Institute. -->
    <!-- *   The issue was fixed by using a newer piece of code from the [EmailJS](https://www.emailjs.com/docs/tutorial/creating-contact-form/) website. -->

---

<!-- ## **Deployment** -->

<!-- ### **Remote Deployment** -->
<!-- 1. Navigate to the GitHub [Repository:](https://github.com/RyanSyme/Milestone-2-Visit-Norrtalje) -->
<!-- 2. Click the **Settings** Tab. -->
<!-- 3. Scroll Down to the **Git Hub Pages** Heading. -->
<!-- 4. Select **Master Branch** as the source. -->
<!-- 5. Click the **Save button**. -->
<!-- 6. Click on the link to go to the live deployed page. -->

<!-- ### **Local Deployment** -->
<!-- 1. Navigate to the GitHub [Repository:](https://github.com/RyanSyme/Milestone-2-Visit-Norrtalje) -->
<!-- 2. Click the **Code** drop down menu. -->
<!-- 3. Download the ZIP file and unpack locally -->
<!-- 4. Open a code editor of your choice and open the unzipped file using the code editor. -->
<!-- 5. Click **Save** and save to your local device -->

---

<!-- ## **Credits** -->

<!-- ### **Content** -->
<!-- *	Code was used from [Developers.Google](https://developers.google.com/maps/documentation/javascript/tutorials) -->

<!-- *   With additional help from [Traversy Media](https://www.youtube.com/watch?v=Zxf1mnP5zcw&t=1101s) -->

<!-- ### **Media** -->

<!-- * The photos used in this site were obtained from [Norrtälje Kommun]( https://www.instagram.com/norrtaljekommun/?hl=en/)  -->

<!-- *   The coat of arms image used to as a logo for the site was obtained from  -->
    <!-- [SearchPNG.com]( https://www.searchpng.com/) -->


<!-- ### **Acknowledgements** -->

<!-- *	I received design inspiration from: -->

    <!-- * **Matt Rudge** at [Code Institute](https://courses.codeinstitute.net/login)  -->
    
    <!-- * [Developers.Google](https://developers.google.com/maps/documentation/javascript/tutorials)  -->
    <!-- * [Traversy Media](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA)  -->
    <!-- * [geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-clear-form-after-submit-in-javascript-without-using-reset/) -->

<!-- *	I received styling inspiration from: -->

    <!-- *   [CSS-Tricks.com](https://css-tricks.com)  -->
    
<!-- *   Additional Thanks to my mentor **Oluwafemi Medale** for styling and formatting advice -->