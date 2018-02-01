# TTEZ
This repository was submitted as an approach to reduce the TTC's (Toronto Transit Commission) carbon emissions by 5%

The majority of the analysis is conducted on the Jupyter notebook. Major requirements are matplotlib, numpy, and pandas.
The "stop_times" files is missing and can be retrieved at http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=96f236899e02b210VgnVCM1000003dd60f89RCRD&vgnextchannel=1a66e03bb8d1e310VgnVCM10000071d60f89RCRD

Using Dataframes, we extracted route information on the TTC in terms of route length, passengers/ride, the different types of vehicles, and the frequency of the buses.

With this data, we calculated how much CO2 each route emits and scaled its impact on a per person basis. This allows us to determine a user's carbon footprint per ride on any bus route on the TTC. This information is then relayed to our ios app (https://github.com/curtischong/TTEZ-APP) which delivers the user an opportunity to be mindful of their impact on global climate.


We concatenated the data into a single dataframe and first filtered out the buses that carried the least amount of people (less than 10% on average) at any moment in time. Using our carbon dioxide models, we determined that these buses which carried barely any people would contribute to 3-4% of the TTC's emissions. If some buses along these routes were removed and re-routed, then the funds saved could be diverted to external climate change initiatives.
