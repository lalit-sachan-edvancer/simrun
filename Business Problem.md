## Business Problem

Suppose a company wanted to check the frauds in an Insurance Firm.

There are variables which are only captured while the issuance of an insurance. So only these variables can be used for creating this model.

Some features:

-  Age of customer (continuous column , not lesser than 21 and not greater than 50)
-  Customer ID: String with numbers and characters
-  Policy ID: String with numbers and characters
-  Address: String
-  Date of Policy Submitted
-  Date of Policy Enforced
-  Marital status : Married /Unmarried (Single)/ Divorced/ widow/others
-  Occupation: Service Pvt/ Service Govt/ Farmer/ Blue Collar / Student etc.
-  Education of customer( given in strings like, tenth, twelfth, graduation, engineering, masters, uneducated (less than 10th))
-  Smoker Flag: Yes/No
-  Family Size: Continuous number
-  Income: some Continuous number
-  Branch Pin Code: 110001 etc (can be featured engineered for first 3 , and first 2 for district and states)
-  Customer Pin Code: same as above (Featured engineered for distance b/w branch and customer 0(same district), 1(from different district))
-  Branch/State/District/Zone Performance (Number of fraud cases last 5 years last month): In percentage value
-  Product (Strings values 5 years Cancer Plan/10 years ULIP/ 20 Years retirement plan etc)
-  Agent who sold the policy
   -  Agent age : continuous number
   -  agent tenure: continuous number
   -  agent education: (tenth, twelfth, graduation, engineering, masters, uneducated (less than 10th))
   -  agent performance last month
   -  Marital status
-  Target (1%)