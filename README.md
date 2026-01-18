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

The process of collecting the data was extensive. There was no existing dataset that had the data I needed so I had to manually enter the data. Setting up a button system with contestants and answers enabled me to speed up the process. Using google firebase, I was able to automatically create a record from each click. I chose 100 episodes as my sample size as this is a large enough number for me to gain valuable insights and be fairly confident in the valadity of the data. I could have collected more, however I decided 100 episodes was the best value for time and gathering data on any more episodes would give diminishing returns.

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

It appears that teams seem to do well at the start and end but not as well in the middle 40 seconds. Running a chi square test gives the p value of 0.26, not enough evidence to say that there is a difference.

## Logistic regression to predict whether a player will make it through to final chase

Working out whether to risk it for the high offer or play it safe and go with the lower offer is a dilema that all contestants on the Chase face. Predicting the probability of making it home with each offer is often what the contestants think about when deciding which offer to take. To model this, I used logistic regression with the features offer taken, age, and cash builder. I chose logistic regression because the features are likely independent and it assumes a linear relationship between the features and the odds it produces. I thought about using the chaser as a feature as well but I decided I didn't have enough data for this to be accurate as each chaser would roughly have 15 episodes of data each. I also concluded that all chasers are roughly similar in skill which would mean they would have little difference on a contestants chance of making it to the final chase. The model produced the following coefficients.

| Feature      | Coefficient |
| ------------ | ----------- |
| offer taken  | -0.597002   |
| age          | 0.020550    |
| cash builder | 0.000174    |


In human terms, this means that for every step up in offer (low-middle-high), the models prediction of weather a contestant will make it to the final chase decreases by 45%. The cash builder coefficient looks incredibly low because it's measured in pounds whereas the cash builders go up in 1000 pounds per correct answer. This means that for every 1000 pound increase to the cash builder, the models prediction increases by 18.98% (this includes compounding from every pound increase). Interestingly, age proved to be a valuable feature as the model predicted a 2.08% increase for every year increase in age. Originaly, I was suspicious and thought this could be due to age confounding with offer taken, meaning that older contestants are more likely to make it through not because of their age but because they are more likely to take the lower offer. After further analysis however, I was more certain that this wasn't the case as older contestants were actually associated with taking the higher offer rather than the lower offer.

| offer taken | average age |
| ----------- | ----------- |
| high        | 46.53       |
| low         | 42.30       |
| middle      | 42.10       |


Looking at the average age of contestants who made it to the Final Chase also suggested that age is a meaningful predictor in its own right. This could be because older contestants have better intuition about their own abilities, allowing them to make more informed decisions about which offers they can realistically take and still make it home. Additionally, older contestants may perform better in the head-to-head round than younger contestants, which would also increase their chances of reaching the Final Chase. Although earlier in my analysis I found that age had little effect on Cash Builder performance, this does not necessarily mean it has no impact on head-to-head performance. Older contestants may be better suited to this stage because they can take more time to reason through questions, and the multiple-choice format provides more opportunity to work out the correct answer compared to the fast recall required in the Cash Builder round.


| made it | average age |
| ------- | ----------- |
| False   | 39.41       |
| True    | 44.83       |


After testing, the model produced an accuracy of 0.717 and an AUC of 0.733. This is a decent improvement than if the model had guessed True for every contestant in which it would have gotten an accuracy of 0.595 (the proportion of contestants who made it through to final chase). 

### Testing with theoretical contestants

To get a closer look at how the model was making it's predictions, I tested some theoretical contestants on it.  
Offer taken:  
1 = low  
2 = middle  
3 = high  

| cash builder | offer taken | age | predicted probs |
| ------------ | ----------- | --- | --------------- |
| 2000         | 2           | 30  | 0.378400        |
| 4000         | 3           | 60  | 0.467742        |
| 6000         | 1           | 50  | 0.769758        |

We can see that in the first contestant scenario, the contestant only gets 2000 in the cash builder, their age is 30 and they take the middle offer. The model predicts their chance of making it to the final chase at 37.8% The second contestant gets 4000 but is 60 years old and takes the high offer. The model predicts 46.7% indicating that although they took the high offer which considerably decreases their chances, their high cash builder and older age makes them more likely of making it through.
The third contestant is 50 years old, gets 6000 in the cash builder and is 50 years old showing how an above average cash builder and taking the lower offer considerably increases a contestants chance of making it to the final chase.

## Random forest model to predict target

There are many factors that influence the target the team will set in the final Chase which contribute in different ways. I chose to use a random forest model rather than a linear model as the random forest will be able to learn complex non-linear relationships between the features. A linear model on the other hand wouldn't be able to model the data accurately as features such as number of contestants won't necessarily have a linear relationship to target. For example, the increase from 1-2 contestants may contribute more than the increase from 3-4 contestants.  
Initially I used the features, max cash builder, min cash builder, average cash builder, and number of contestants in final to predict targets. This wasn't particularly effective as the model had a mean average error of 2.83 steps. Part of the reason for the poor performance was the limited data available (only 100 episodes) as well as decision tree models like random forest tending to come up with complex relationships to fit the training data which isn't always reflective of the real relationship. Removing the features min cash builder and max cash builder resulted in slightly better performance with a mean absolute error of 2.26 steps. Still not perfect, but a decent improvement. 

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

The scatter plots demonstrate a generally positive relationship between the model’s predicted target and both average cash builder and number of contestants. There is noticeably greater variation in predictions across different values of num_made_it, which is consistent with this feature having lower predictive importance compared to average cash builder.


### Testing model on theoretical teams

To properly evaluate how the model predicts its target, I tested the model on theoretical values. 

| avg_cash_builder | num_made_it | predicted target |
| ---------------: | ----------: | ---------------: |
|             6000 |           1 |        16.657750 |
|             1000 |           2 |        13.787071 |
|             2000 |           4 |        18.267452 |

The table shows how the model trades off individual strength against team size. A team with one relatively strong player (average cash builder of 6,000) is predicted to set a moderate target of 16.66. In contrast, a team with two very weak players (average cash builder of 1,000) is predicted to set a much lower target of 13.79, suggesting that the model views “two very poor contestants” as worse than “one good one.” Meanwhile, a team of four weak players (average cash builder of 2,000) is predicted to set the highest target (18.27), indicating that the model sometimes places more weight on the number of contestants reaching the Final Chase than on their individual cash builder performance. This highlights both the importance of team size in the model and some unintuitive behavior likely driven by noise in the data and the flexibility of the random forest.

## Gradient boosting to predict probability of catching target

The chasers often like to pick favourites before trying to catch the team. Typically, a target of around 19 puts the team in what is called the fun-zone, where both the chaser and the team have similar chances of winning. To predict the chances of the chaser catching the team, I used a gradient boosting model. I chose this model as I have already done a logistic regression and random forest model already.

## Finding which offer leads to maximum expected value

Expected value is a gambling concept which is the ammount you would get if you repeated a bet many times. 

## Limitations

Although the analysis gives a general overview of trends and patterns, there are a few limitations that could have skewed results.
The first is the relatively small dataset of 100 chase episodes. This increases the chances that my results could be due to random variation rather than actual relationships. Particularly for my random forest model to predict targets, the small dataset could contribute to the model finding complex relationships where there is none.  
Another limitation is the assumption that question difficulty stays the same from episode to episode. Because the data comes from multiple seasons that were years apart, question difficulty may not have stayed the same in that time and this could be skewing results for the momentum analysis and the target predictions.
The third limitation is that the data was collected manually which could lead to inputting incorrect data. 

