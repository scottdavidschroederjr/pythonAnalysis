import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_df = df.loc[df['sex'] == 'Male'] 
    average_age_men = round((men_df['age'].mean()),1)
  
    # What is the percentage of people who have a Bachelor's degree?
    bachelors_df = df.loc[df['education'] == "Bachelors"]
    percentage_bachelors = round((((bachelors_df.shape[0]) / (df.shape[0])) * 100),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_df = df.loc[(df['education'] == "Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")]

    he_greater50k_df = higher_education_df.loc[df["salary"] == ">50K"]

    lower_education_df = df.loc[(df['education'] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate")]

    le_greater50k_df = lower_education_df.loc[df["salary"] == ">50K"]

    # percentage with salary >50K
    higher_education_rich = round((((he_greater50k_df.shape[0]) / (higher_education_df.shape[0])) * 100),1)
    lower_education_rich = round((((le_greater50k_df.shape[0]) / (lower_education_df.shape[0])) * 100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_df = df.loc[df['hours-per-week'] == 1]
    min_rich_df = min_hours_df.loc[df['salary'] == '>50K']

    rich_percentage = round((((min_rich_df.shape[0]) / (min_hours_df.shape[0])) * 100),1)

    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].value_counts()
    countries = countries.to_dict()

    df5k = df.loc[df['salary'] == '>50K']
    df5k = df5k['native-country'].value_counts()
    df5k = df5k.to_dict()

  
    highestEarning = {}
    for k, v in df5k.items():
      highestEarning[k] = v / countries.get(k)

    percentList = sorted(highestEarning.items(),key=lambda x: x[1], reverse=True)

    highest_earning_country = percentList[0][0]
    highest_earning_country_percentage = round((percentList[0][1]*100),1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df.loc[df['native-country'] == "India"]
    india_lt50k_df = india_df.loc[df['salary'] == '>50K']
    top_occs = india_lt50k_df['occupation'].value_counts()
    occs_list = top_occs.index.tolist()
    top_IN_occupation = occs_list[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
