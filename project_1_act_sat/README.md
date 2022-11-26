# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) 
Project 1: Standardized Test Analysis

### Overview

SAT and ACT are standardized tests required by colleges and universities in the United States as part of their admission process. [ACT](https://www.act.org/content/act/en.html) is administered by ACT Inc and has 4 sections comprising English, Math, Reading, and Science, while [SAT](https://collegereadiness.collegeboard.org/sat) is administered by College Board and has 2 sections which is Evidence Based Reading and Writing (EBRW) and Math.

Standardized test has been a controversial topic. Despite the rise of test-optional admission, over 2.2 million students in class 2019 took SAT and more than 52% took ACT in 2019. The intend of a standardize test is to measure college readiness and provide universities and colleges with a common data points of the applicant.

Many questions the objectivity on these tests with the rise of the [famous Varsity Blue scandal](https://www.nytimes.com/2021/10/09/us/varsity-blues-scandal-verdict.html), while there are some who still believe that these tests are able to [predict how well students perform on their freshment year](https://www.ucop.edu/institutional-research-academic-planning/_files/sat-act-study-report.pdf). College Board and ACT have argued that **this standardized tests open opportunities** to merit-based scholarships which can eventually reduce the disparity between higher and lower income.

In March 2016, new format for SAT was released to capture more test-takers share from ACT who has been the preferred test since 2012. Therefore, looking at the previous data from 2017-2019 for both ACT and SAT, we will to explore on how effective this initiative is.

[discrepancy of resource accessibility with respect to their household income](https://www.cnbc.com/2019/10/03/rich-students-get-better-sat-scores-heres-why.html).


# Problem Statement
College Board is looking for **recommendations on increasing the participation rates.** 
As part of College Board staff, we would like to make informed decision on which State we need to focus to increase participation by exploring the past 2017-2019 data for both SAT and ACT.

*Which state should College Board put more attention to?*

# Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**state**|*string*|ACT 2017|State where ACT and SAT data collected| 
|**act_participation_17**|*float*|ACT 2017|Percentage participant rate in 2017(out of 100%)| 
|**act_total_17**|*float*|ACT 2017|Average ACT composite score (1-36)| 
|**act_participation_18**|*float*|ACT 2018|Percentage participant rate in 2018 (out of 100%)| 
|**act_total_18**|*float*|ACT 2018|Average ACT composite score (1-36)| 
|**act_participation_19**|*float*|ACT 2019|Percentage participant rate in 2019(out of 100%)| 
|**act_total_19**|*float*|ACT 2019|Average ACT composite score (1-36)| 
|**sat_participation_17**|*float*|SAT 2017|Percentage participant rate in 2017(out of 100%)| 
|**sat_total_17**|*integer*|SAT 2017|Average SAT total score (400-1600)| 
|**sat_participation_18**|*float*|SAT 2018|Percentage participant rate in 2018(out of 100%)| 
|**sat_total_18**|*integer*|SAT 2018|Average SAT total score (400-1600)| 
|**sat_participation_19**|*float*|SAT 2019|Percentage participant rate in 2019(out of 100%)| 
|**sat_total_19**|*integer*|SAT 2019|Average SAT total score (400-1600)| 
|**gdp_17**|*integer*|BEA|Real Gross Domestic Product by state in 2017, measured in chained 2012 dollars| 
|**gdp_18**|*integer*|BEA|Real Gross Domestic Product by state in 2018, measured in chained 2012 dollars| 
|**gdp_19**|*integer*|BEA|Real Gross Domestic Product by state in 2019, measured in chained 2012 dollars| 
|**gdp_17_cat**|*object*|BEA|Real GDP catergories by state in 2017 (<$40k,$40-50k,$50-60k,$60-70k,>$70k| 
|**gdp_18_cat**|*object*|BEA|Real GDP catergories by state in 2018 (<$40k,$40-50k,$50-60k,$60-70k,>$70k| 
|**gdp_19_cat**|*object*|BEA|Real GDP catergories by state in 2019 (<$40k,$40-50k,$50-60k,$60-70k,>$70k| 
|**preference**|*object*|EducationWeeK|Inclination towards ACT or SAT by state in 2019| 


# Exploratory Data Analysis
#### Limitations of the Analysis
It shows that these scores might **only represent small fraction of the students at a given state (selection bias)**. Thus, we need to be careful on how we analyse the top scorer. (setting threshold at least 50% participation rate on our data visualization analysis and we will show more on why this threshold might help us analyze the data)

# Data Visualization
From the ACT and SAT datasets that we have, we can find found out that students have limited time to study for the test. Therefore, they are focusing one at a time. As what we have expected, real GDP per Capita influences the score test. Higher GDP per capita tent to do better in SAT, while lower GDP per capita tend to have higher ACT participation rates but score lower average score. 

Keeping in mind of our four criteria:
1. States with no preference to any test 
2. States with GDP less than <$50,000 (below average)
3. States with below average score
4. States with low SAT participation rate (<50%)

Excluding Florida with SAT participation rate of 100%, **I would recommend that College Board put more attention to New Mexico to increase the SAT participation rates**.

Looking at the data of delta participation rates change throughout the years, **having an agreement with the state to create state policy for high school student graduation requiremnet** might be the most effective way to achieve this.

However, it is good for College Board to **bring solution on bridging the gap of test preparation access for students** in that state such as:
1. Providing a free access to any test preparation source for free
2. Schedule a sharing session to parents and students so they are aware of the [fee-waiver scheme](https://parents.collegeboard.org/college-board-programs/sat#)
3. Collaborate with schools to create SAT School Day so that students can take test during the school

Aside from that, there is a rise on the test optional policy for college admission, thus, **College Board must strengthen their marketing strategy** such as by leveraging the fact that SAT can open doors to full ride scholarship.