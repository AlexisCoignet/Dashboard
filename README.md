How the three-pointer shot has changed the face of the NBA

This directory contains a Python application, whose goal is to show significant and dominating the three-pointer has been in the recent history, then help recruters to show from where NBA stars come from and what post they play.

What's here ? User Guide

To launch the code it is necessary to be placed in the file where is the main.py on the cmd. Then make the command: "python main.py". Then use the link that will be printed (http://127.0.0.1:8050/). Then wait for a minute, press F5 to reload internet page. Then the dashboard will appear.
Normally all packages are supposed to be installed automatically if you do not have them. However, it is possible that a bug occurs. In this case, install the packages manually. With the command pip install 'package'. They are the following: numpy, pandas, dash, geopy.

Origins

player.csv can be find at 'https://data.world/datadavis/nba-salaries/workspace/file?filename=players.csv'.
3ppy can be find at 'https://fr.wikipedia.org/wiki/Liste_des_meilleurs_marqueurs_en_NBA_par_saison'. We have only taken the data since 1980 because this is the year when the 3 points came into force.

Repor Analysis

Once you have the app displayed, full-screen on your browser zoom on the first histogram to see better datas from 1980.
The first figure is a histogram that represents the number of 3-pointers scored by the best scorer of each year since 1980. Here we see a noticeable difference between before 2015 and after 2015. We should therefore advise coaches to focus on defensive techniques for 3-point shots but also on training players to improve their percentage of successful 3-point shots.
The second figure is a map that lists the birthplaces of 100 players randomly taken from the player.csv file. If you zoom out you can clearly see that the players are mostly from the USA but more particularly from the East Coast. We can therefore encourage coaches to focus on players who were born and raised on the east coast of the USA.
To display this map we use an API (geopy) which gives us a latitude and a longitude when we give it the name of a place, a city, a state etc... 
The last figure shows the number of positions drafted per year (drafted = selected) over the last 1 to 2 years. Indeed it is intended to show the selectors of which positions will be missing in the next years. The average duration of an NBA career is 5 years. If we take the last 5 years and look at the position that has the least players then we can say that we will have to focus on recruiting young players playing this position.

Improvement ideas

We could take into account more parameters regarding the selection of players based on their place of birth, for example how many players make a career in the NBA compared to the number of people in the state.

Another point is that the code takes a long time to run, almost more than a minute. We should find points to optimize the code.


Alexis Coignet - Romain Bourdeaux
