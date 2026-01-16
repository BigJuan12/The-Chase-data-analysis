# The Chase data analysis

<img src="https://github.com/BigJuan12/The-Chase-data-analysis/blob/main/The%20chase%20gameplay%20image.webp">

## Overview
The Chase is a Brittish quiz show where 4 contestants work together to beat a chaser, one of the worlds best quizzers. There are 3 phases. The first phase is the cash builder round where each contestant has a minute to answer rapid fire questions to accumulate as much money as possible. Each correct answer is worth 1000 pounds. The second phase is the head to head where the Chaser gives the contestant a high offer and a low offer as well as a middle offer which is decided by how much money they accumulated in the cash builder. The offer the contestant takes decides how many steps ahead of the chaser they will start (the high offer being 2 steps ahead, the middle being 3 and the low being 4). The chaser and the contestant will then answer the same multi choice questions. A correct answer will move the contestant or chaser forward by one step. The head to head ends with either the chaser catching the contestant or the contestant making it home before the chaser catches them. If the contestant gets home, the money from the offer they took is added to the team bank. The last round is the final chase where all the contestants who made it home will have 2 minutes to answer quickfire questions. Each correct answer gives the contestants another step towards their target. The contestants gain a head start based on how many made it home (4 contestants = 4 step head start, 2 = 2 step head start etc). Once the 2 minutes is up, the chaser has 2 minutes to try and reach their target however getting an incorrect answer gives the contestants a chance to push the chaser back 1 step if they can come up with the correct answer. If the chaser is unable to catch the team in time, the team leave with all the money in their bank or otherwise leave with nothing.



## Questions

Does gender and age influence the likelihood of a contestant taking the various offers. For example are male and younger contestants more likely to risk it and take the high offer.  

Does gender and age influence the ammount of money a contestant is expected to accumulate in their cash builder. For example, older contestants may do better as they have lived longer and gained more knowledge.  

Are contestants effected by momentum. For example does a previous correct answer increase the chances that a contestant will get the next one correct.  

Do teams answer questions evenly in the final chase. For example do teams typically perform well initially and then go cold.  

Create a model to predict target based on contestants who made it through and their cash builders.  

How do cashbuilders and number of contestants in the final chase impact likelihood of pushing the chaser back.

## Overview of the data

The dataset contains data on 100 episodes of The Chase. The data is stored within 2 datasets, final_chase_data and contestant_data. each record in final_chase_data is an event from the final chase, either a correct answer, incorrect answer or pushback. More details are stored such as the time left on the clock, the contestant, and the current total.

### Example record from final_chase_df

| chaser              | contestant          | current_total | episode | event           | season | target | time_left (seconds)       |
|---------------------|---------------------|---------------|---------|-----------------|--------|--------|------------------|
| the dark destroyer  | the dark destroyer  | 11            | 131     | correct chaser  | 12     | 16     | 4.571048974990845 |

The contestant_data dataset contains data on each contestant within an episode including age, gender, cash builder and whether the contestant made it through to the final chase or not.

### Example record from contestant_data

| chaser           | contestant1 | contestant1_age | contestant1_cash_builder | contestant1_gender | contestant1_made_it | contestant1_offer_taken | contestant2  | contestant2_age | contestant2_cash_builder | contestant2_gender | contestant2_made_it | contestant2_offer_taken | contestant3 | contestant3_age | contestant3_cash_builder | contestant3_gender | contestant3_made_it | contestant3_offer_taken | contestant4  | contestant4_age | contestant4_cash_builder | contestant4_gender | contestant4_made_it | contestant4_offer_taken | episode | season |
|------------------|-------------|-----------------|--------------------------|--------------------|---------------------|--------------------------|-------------|----------------|--------------------------|--------------------|---------------------|--------------------------|------------|----------------|--------------------------|--------------------|---------------------|--------------------------|-------------|----------------|--------------------------|--------------------|---------------------|--------------------------|--------|--------|
| the sinnerman    | Ash         | 35              | 2000                     | male               | true                | middle                   | Gianluca     | 26             | 4000                     | male               | true                | middle                   | Sally      | 54             | 6000                     | female             | false               | middle                   | Katherine   | 41             | 4000                     | female             | true                | middle                   | 125    | 12     |



## Collecting the data

The process of collecting the data was extensive. There was no existing dataset that had the data I needed so I had to manually enter the data. Setting up a button system with contestants and answers enabled me to speed up the process. Using google firebase, I was able to automatically create a record from each click.

<img width="310" height="416" alt="chase data collection image" src="https://github.com/user-attachments/assets/0a5c3047-0a43-4a25-886d-1061ef50c5de" />


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

Running a chi square test gives the p value 0.000012, an incredibly small value showing that there is definetly a relationship. This means we can reject Ho in favour of Ha and we can confidently say that the result of the previous answer does have an effect on the probability of getting the next question correct. It seems counter intuitive that a correct answer is more likely if the previous answer was incorrect. A possible explanation for this could be that they purposely alternate between difficult and easy questions. If I had more time, this could be answered by testing the same questions on others to see if the same pattern emmerges.

## Momentum on a larger scale

The chasers and the host often comment on a teams course over the final chase. They say things like "the wheels came off in the second minute" or "they got some rythm going". I wanted to find out if teams typically answers questions correct evenly throughout the entire 2 minutes or if for example they start off correctly answering many questions to begin with and then slow down later. To answer this, I split the number of correct answers into 3 bins, the first 0-40 seconds, the next 40-80 seconds and the final 80-120 seconds. The raw counts are as follows.

| Time Bin (seconds) | Correct Answers |
|-------------------|----------------:|
| 0–40              | 471             |
| 40–80             | 415             |
| 80–120            | 478             |


## Random forest model to predict target

There are many factors that influence the target the team will set in the final Chase. Initially I used the features, max cash builder, min cash builder, average cash builder, and number of contestants in final to predict targets. This wasn't particularly effective as the model had a mean average error of 2.83 steps. Part of the reason for the poor performance is the limited data available (only 100 episodes) as well as decision tree models like random forest tending to come up with complex relationships to fit the training data which isn't always reflective of the real relationship. Removing the features min cash builder and max cash builder resulted in slightly better performance with a mean absolute error of 2.26 steps. Still not perfect but a decent improvement. 

<img width="587" height="429" alt="Feature importance" src="https://github.com/user-attachments/assets/de042b65-1309-4493-b2e5-7cb0c1108eaa" />

The feature importance graph shows that the model relies more heavily on average cash builder than on the number of contestants who made it to the Final Chase when making its predictions.

<table>
  <tr>
    <td>
      <img width="564" height="451" alt="Predicted vs avg cash builder" src="https://github.com/user-attachments/assets/1ceb1404-1227-4084-a05a-5c3062c6f293" />
    </td>
    <td>
      <img width="566" height="462" alt="Predicted vs num made it" src="https://github.com/user-attachments/assets/2ef10216-e4c8-4b7e-8284-3fc82cd0795a" />
    </td>
  </tr>
</table>

he scatter plots demonstrate a generally positive relationship between the model’s predicted target and both average cash builder and number of contestants. There is noticeably greater variation in predictions across different values of num_made_it, which is consistent with this feature having lower predictive importance compared to average cash builder.

