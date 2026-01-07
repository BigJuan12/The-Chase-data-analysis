# The-Chase-data-analysis

<img src="https://github.com/BigJuan12/The-Chase-data-analysis/blob/main/The%20chase%20gameplay%20image.webp">

Overview
The Chase is a Brittish quiz show where 4 contestants work together to beat a chaser, one of the worlds best quizzers. There are 3 phases. The first phase is the cash builder round where each contestant has a minute to answer rapid fire questions to accumulate as much money as possible. Each correct answer is worth 1000 pounds. The second phase is the head to head where the Chaser gives the contestant a high offer and a low offer as well as a middle offer which is decided by how much money they accumulated in the cash builder. The offer the contestant takes decides how many steps ahead of the chaser they will start (the high offer being 2 steps ahead, the middle being 3 and the low being 4). The chaser and the contestant will then answer the same multi choice questions. A correct answer will move the contestant or chaser forward by one step. The head to head ends with either the chaser catching the contestant or the contestant making it home before the chaser catches them. If the contestant gets home, the money from the offer they took is added to the team bank. The last round is the final chase where all the contestants who made it home will have 2 minutes to answer quickfire questions. Each correct answer gives the contestants another step towards their target. The contestants gain a head start based on how many made it home (4 contestants = 4 step head start, 2 = 2 step head start etc). Once the 2 minutes is up, the chaser has 2 minutes to try and reach their target however getting an incorrect answer gives the contestants a chance to push the chaser back 1 step if they can come up with the correct answer. If the chaser is unable to catch the team in time, the team leave with all the money in their bank or otherwise leave with nothing.

Questions
Some of the questions I want to answer with this analysis:
Does gender and age influence the likelihood of a contestant taking the various offers. For example are male and younger contestants more likely to risk it and take the high offer.
Does gender and age influence the ammount of money a contestant is expected to accumulate in their cash builder. For example, older contestants may do better as they have lived longer and gained more knowledge.
Are contestants effected by momentum. For example does a previous correct answer increase the chances that a contestant will get the next one correct.
Do teams answer questions evenly in the final chase. For example do teams typically perform better and then go cold.
Create a model to predict target based on contestants who made it through and their cash builders.
How do cashbuilders and number of contestants in the final chase impact likelihood of pushing the chaser back.

Collecting the data

<img width="610" height="816" alt="chase data collection image" src="https://github.com/user-attachments/assets/0a5c3047-0a43-4a25-886d-1061ef50c5de" />
<br
  
  >

<img width="742" height="208" alt="final chase data image" src="https://github.com/user-attachments/assets/09426430-367c-40c7-8f69-9231e4cb7c95" />
<br
  
  >

<img width="1122" height="316" alt="contestant data image" src="https://github.com/user-attachments/assets/9fe9d324-92b8-4833-b23b-45b894f2234f" />
