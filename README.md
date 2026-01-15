# The Chase data analysis

<img src="https://github.com/BigJuan12/The-Chase-data-analysis/blob/main/The%20chase%20gameplay%20image.webp">

## Overview
The Chase is a Brittish quiz show where 4 contestants work together to beat a chaser, one of the worlds best quizzers. There are 3 phases. The first phase is the cash builder round where each contestant has a minute to answer rapid fire questions to accumulate as much money as possible. Each correct answer is worth 1000 pounds. The second phase is the head to head where the Chaser gives the contestant a high offer and a low offer as well as a middle offer which is decided by how much money they accumulated in the cash builder. The offer the contestant takes decides how many steps ahead of the chaser they will start (the high offer being 2 steps ahead, the middle being 3 and the low being 4). The chaser and the contestant will then answer the same multi choice questions. A correct answer will move the contestant or chaser forward by one step. The head to head ends with either the chaser catching the contestant or the contestant making it home before the chaser catches them. If the contestant gets home, the money from the offer they took is added to the team bank. The last round is the final chase where all the contestants who made it home will have 2 minutes to answer quickfire questions. Each correct answer gives the contestants another step towards their target. The contestants gain a head start based on how many made it home (4 contestants = 4 step head start, 2 = 2 step head start etc). Once the 2 minutes is up, the chaser has 2 minutes to try and reach their target however getting an incorrect answer gives the contestants a chance to push the chaser back 1 step if they can come up with the correct answer. If the chaser is unable to catch the team in time, the team leave with all the money in their bank or otherwise leave with nothing.



## Questions
Some of the questions I want to answer with this analysis:  

Does gender and age influence the likelihood of a contestant taking the various offers. For example are male and younger contestants more likely to risk it and take the high offer.  

Does gender and age influence the ammount of money a contestant is expected to accumulate in their cash builder. For example, older contestants may do better as they have lived longer and gained more knowledge.  

Are contestants effected by momentum. For example does a previous correct answer increase the chances that a contestant will get the next one correct.  

Do teams answer questions evenly in the final chase. For example do teams typically perform well initially and then go cold.  

Create a model to predict target based on contestants who made it through and their cash builders.  

How do cashbuilders and number of contestants in the final chase impact likelihood of pushing the chaser back.

## Collecting the data

<img width="310" height="416" alt="chase data collection image" src="https://github.com/user-attachments/assets/0a5c3047-0a43-4a25-886d-1061ef50c5de" />
<div style="margin-bottom: 20px;"></div>

<img width="742" height="208" alt="final chase data image" src="https://github.com/user-attachments/assets/09426430-367c-40c7-8f69-9231e4cb7c95" />
<div style="margin-bottom: 20px;"></div>
  

<img width="1122" height="316" alt="contestant data image" src="https://github.com/user-attachments/assets/9fe9d324-92b8-4833-b23b-45b894f2234f" />

## Interesting facts

The average cash builder is $4803
  
The average age of a contestant is 43 years old   

59.5% of contestants make it through to the final chase  

The average target the teams set is 16.8

## Does gender effect the offer the contestants take

<img width="599" height="480" alt="Offer taken by gender" src="https://github.com/user-attachments/assets/72349518-e634-4970-bf36-bd50810fc964" />

| Gender | High Offer | Middle Offer | Low Offer |
|--------|-----------:|-------------:|----------:|
| Female | 11.7% | 79.7% | 8.6% |
| Male   | 11.8% | 81.8% | 6.4% |


Originally I thought that males would be more inclined to take risks and therefore have higher rates of taking the high offer however there was little difference between the offers.  
Both males and females overwhelmingly take the middle over the other offers with very few taking the lower offer.
There is a slight difference in the lower offer with females taking this offer slightly more frequently than males.

Running a chi-square test of independence found no statistically significant association between contestant gender and offer taken (p = 0.699). Although there are small differences in the proportions, these can be explained by random variation rather than gender.

## Does age effect cash builder

It may be assumed that older contestants would perform better in the cash builder as they have lived longer to accumulate more knowledge. The scatter plot describes the relationship between age and cash builder.

<img width="891" height="535" alt="scatter plot of age : cashbuilder" src="https://github.com/user-attachments/assets/ed6d95d2-079a-45b2-a76e-10034eee7a0e" />

From these results it's clear that age has no effect on cash builder as there are good and bad contestants of all ages.

## Effect of momentum on contestants

Does momentum have an effect on teams in the final chase? For example do teams have hot streaks where they answer many questions in a row and then go cold.
To answer this question we will examine if the probability of getting the next question correct is different depending on if the previous answer was correct or incorrect.

Ho: The result of the previous answer has no effect on the probability of getting the next question correct, p(correct|previous incorrect) = p(correct|previous correct)  

Ha: The result of the previous answer does have an effect on the probability of getting the next question correct, p(correct|previous incorrect) ≠ p(correct|previous correct)


| Previous Answer | Current Correct | Current Incorrect |
|-----------------|----------------:|------------------:|
| Incorrect         | 763             | 286               |
| Correct       | 543             | 601               |

The raw counts show that there is a difference in the chances of the team getting an answer correct depending on the previous answer however the relationship is in the other direction that expected. It seems that the team is more likely to get the next question correct if the previous question was incorrect than if it was correct.

p (correct) = 0.62  
p (incorrect) = 0.38  
p (correct|previous correct) = 0.56  
p (correct|previous incorrect) = 0.66  

Running a chi square test gives the p value 0.000012, an incredibly small value showing that there is definetly a relationship. This means we can reject the Ha in favour of Ho and we can confidently say that the result of the previous answer does have an effect on the probability of getting the next question correct. It seems counter intuitive that a correct answer is more likely if the previous answer was incorrect. A possible explanation for this could be that they purposely alternate between difficult and easy questions. This could be answered by testing the same questions on others to see if 

