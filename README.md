# unanuevanormalidad.com

<img src="images/header.png" alt="200" width="850"/>

In Spain the return to normality is being done by territories. Depending on the epidemiological conditions of each health area, the regions are in a de-escalation phase where different policies are applied.

unanuevanormalidad.com arises from this situation, where in many areas of Spain it can be confusing to know what phase they are in. 

## Tools

I have created and hosted in **MongoDB Atlas** a database with the zip codes of the health areas that were advancing in phase. 

This database consists of a document for each of the 52 provinces of Spain, and, in the case that there are exceptions by health regions in that province, it includes the postal codes of these exceptions.

<img src="images/database example.png" alt="150" width="250"/>

The website is built with **Streamlit**, a very interesting framework that speeds up and makes it easy and nice to assemble a GUI.

Hope you like it! 💛

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.