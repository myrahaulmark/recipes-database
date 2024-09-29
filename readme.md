**Project Charter and Entity Design** 

 **Project Overview **

In the spirit of the French culinary practice mise en place the primary purpose of this project will be to develop a recipe model that helps users organize and explore recipes with ease, just like the culinary practice of preparing ingredients in advance.  Users can browse, create, and manage recipes, track ingredients, and read or leave reviews. Whether the user is looking for new meal ideas or trying to organize favorite dishes, “La Mise en Place1” will make it simple to discover and share recipes, with a focus on efficiency and good preparation. 

**Objectives **
When the site is finished... 

Users will be able to easily search, browse, and filter recipes based on ingredients, dietary preferences, and cooking times. 

Users will be able to create and manage their own recipes, including uploading images, listing ingredients, and providing step-by-step instructions.2 

Users will have the ability to leave reviews and ratings, helping others discover popular and highly rated dishes. 

The system will efficiently organize recipes with features like ingredient tracking, allergen alerts, and category sorting, making meal planning easy and intuitive. 

**Key Stakeholders **

Stakeholder Name (or Role Name) 

Impact / Role in the Project 

Dr. Michael Dereszynski 

 

**User community **

We will need to form a ‘focus group’ of key individuals to provide feedback to the team on the ongoing development to ensure the final product is well received 

**Project Risks **

The API may face security risks, such as unauthorized access or data breaches, especially if sensitive user data (like account information or personal preferences) is stored. Despite best efforts, new vulnerabilities may be discovered, and attacks could exploit weaknesses in the system. 

Recipes and ingredient data might come from multiple sources or be user-generated. There is a risk that this data may be incomplete, inconsistent, or inaccurate, leading to a poor user experience (e.g., incorrect nutritional information or cooking times). This is difficult to control, as the quality of user submissions or external data sources cannot be guaranteed. 

If the project relies on external services (such as image hosting, external APIs for nutrition data, or user authentication systems), there’s a risk that those services could change, break, or become unavailable. This would negatively affect functionality without your team being able to control the external service. 

Long-term risk may include evolving dietary trends: The project might face issues due to rapidly changing dietary trends, such as sudden increases in popularity for certain diets (e.g., keto, plant-based) or new allergen regulations. This could make it challenging to keep the recipe database up to date with relevant content that meets new user expectations or legal requirements. 

**Key Assumptions **

Users will contribute to the platform: The project assumes that users will regularly create recipes, leave reviews, and engage with the content, ensuring the platform remains dynamic and useful. 

The data will be accurate and relevant: It is assumed that both user-generated and external recipe data will be reliable, complete, and accurate, allowing for effective filtering, categorization, and presentation. 

The ability to have a stable API integration: The API will work seamlessly across devices and browsers, with no significant interruptions in service. External dependencies (e.g., hosting, databases) are expected to remain reliable throughout the development and deployment. 

 User interest in dietary filtering: The assumption is made that there will be strong user demand for filtering recipes based on dietary preferences (e.g., allergen-free, vegan), and this feature will enhance the user experience. 

 No significant external changes in technology: It is assumed that there will be no major shifts in the technology used (e.g., programming languages, frameworks, or API protocols) that would require significant rework during the project timeline. 

 

**Additional Constraints: **

Time: With a set project timeline, the team must prioritize key features and ensure the core functionality is delivered on time, which limits the scope of extra or advanced features. 

Being a two-person team, the development pace is constrained by the available manpower. There is limited room for dividing work into highly specialized roles, requiring team members to handle multiple responsibilities. 

Technology Stack: The project is constrained by the tools and technologies available to the team (e.g., databases, programming languages). Changing or upgrading these tools during development would cause delays and rework. 

**Project Scope **

Project Scope defines which functions and features will be delivered, and which features/functions will not be delivered (just as important as the things that are to be delivered).   

**Functionality to Be Delivered: **

Recipe Management System: 

Users can create, edit, and delete recipes. 

Each recipe will include fields like title, description, ingredients, cooking instructions, preparation time, and images. 

Recipes can be categorized by dietary preferences (e.g., vegan, gluten-free) and meal types (e.g., breakfast, dinner). 

Ingredient Tracking: 

Each recipe will include a list of ingredients, along with the ability to filter for specific dietary restrictions (e.g., allergen-free options). 

Users can search recipes by ingredients they have on-hand. 

User Accounts and Reviews: 

Users can sign up, log in, and manage their profiles. 

Users will be able to leave reviews and ratings on recipes. 

Reviews will include a rating system (1-5 stars) and a text description. 

Search and Filter Functionality: 

Users can search for recipes based on ingredient availability, preparation time, category, or rating. 

Advanced filters for specific dietary restrictions or cooking methods. 

API Integration: 

Full API support for all CRUD operations (Create, Read, Update, Delete) for recipes, ingredients, and reviews. 

API allows for easy interaction with the database from external applications or front-end systems. 

Basic Security Features: 

Secure login and account management with basic encryption for user credentials. 

Role-based access control, where only authorized users can edit or delete content. 

 

**Functionality Not to Be Delivered: **

Recipe Suggestions Based on User Preferences: 

The system will not include advanced recommendation features, such as suggesting recipes based on a user’s past behavior or preferences. This would require more complex algorithms and machine learning integration, which is out of the project’s scope. 

Comprehensive Nutritional Information: 

While basic ingredient information will be provided, a full breakdown of nutritional content (calories, macros, etc.) for each recipe will not be calculated automatically. This would require external nutrition databases and more time to implement. 

Social Features: 

The platform will not include social networking features such as following other users, sharing recipes on social media directly from the app, or private messaging between users. 

Mobile App or Offline Mode: 

The project will focus on a web-based application only. No mobile app or offline functionality will be delivered in this phase due to resource constraints. 

Advanced Security Features: 

The project will not include advanced security features such as two-factor authentication, OAuth integration, or comprehensive data encryption beyond basic login credentials. These enhancements could be added in future phases. 

Monetization Features: 

The site will not include e-commerce functionality, such as selling premium recipes or ad-based monetization features. 

 

 

**Release Plan **


For the purpose of this project, the release plan is limited to the scope of the course; occurring August through the end of November, 2024. There will be only one release and demonstration. 

Initial Timeline 

Provide an overview of the project. 

The initial timeline provides a high-level estimate of project milestones and dates.  Having an initial timeline provides the stakeholders with a better sense of what is to come and when to expect to see progress. 

Week 5/September 16: Project Initiation (requirements gathering, planning, estimations) 

Week 6-16: Development and testing 

Week 16/December 7: Release 1 demo and presentation 

 

**Entity Design **

Recipes: Stores the details of each recipe, including title, description, cooking time, servings, instructions, and an image. This is the core table for the database, representing the recipes users will create and view. 

Ingredients: Contains the information about each ingredient, such as name, whether it's an allergen, and its nutritional information (calories per unit). This helps in managing the list of ingredients used in the recipes. 

Recipe_Ingredients: Establishes a many-to-many relationship between recipes and ingredients. It allows each recipe to have multiple ingredients and each ingredient to be used in multiple recipes, while also specifying the quantity of each ingredient in a recipe. 

Categories: Defines categories for classifying recipes (e.g., "Vegetarian", "Desserts", "Quick Meals"). It helps in organizing recipes into searchable categories for easier navigation. 

Recipe_Categories: Connects recipes to categories through a many-to-many relationship. Each recipe can belong to multiple categories, and each category can contain multiple recipes. 

Users: Stores information about the users of the platform, such as usernames, emails, and their account creation date. This allows the platform to manage user accounts and track who is creating, reviewing, or interacting with the content. 

Reviews: Stores the reviews left by users for recipes. Each review includes the user who wrote it, the recipe being reviewed, the rating (1 to 5 stars), the text of the review, and the date of submission. It helps capture user feedback on recipes, enhancing user engagement. 

​**​References **

​​Use “mise en place” to make meal preparation easier. UNL Food. (2022, March 10). https://food.unl.edu/article/use-mise-en-place-make-meal-preparation-easier  

​​​ 

 

Table and column listing: 


Categories
CategoryID	
Category Name

Users
UserID	
FirstName	
LastName	
Email	
JoinDate

Recipe_Categories
CategoryID	
RecipeID

Reviews
ReviewID	
Rating	
ReviewText	
ReviewDate	
UserID	
RecipeID

Recipes
RecipeID	
Title	
Description	
CookingTime	
Servings	
NumberOfSteps	
Instructions	
SubmittedDate	
NumberOfIngredients	
ImageURL	
CategoryID	

Recipe_Ingredients_fact_table
CompID	
RecipeID	
IngredientsID	
Ingredients

Ingredients
IngredientsID	
Ingredients	
ServingSize	
Calories	
TotalFat	
SaturatedFat	
Cholesterol	
Sodium	
Carbohydrate	
Fiber	
Sugars	
Protein	
Fat	
Caffeine	
Source	
Date	


git remote add origin https://github.com/myrahaulmark/recipe_db_project.git
