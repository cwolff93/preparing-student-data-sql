# Import panda library
import pandas as pd

# Load the dataset
ds_jobs = pd.read_csv("customer_train.csv")

# View the dataset
ds_jobs.head()

# Create a copy of ds_jobs for transforming
ds_jobs_transformed = ds_jobs.copy()

# Verify nulls, data types and number of unique values

ds_jobs_transformed.info()

ds_jobs_transformed.nunique()

# Transform data types in order to fit the formulas used and/or reduce file size (2.0+ MB to 400.2 KB)

ds_jobs_transformed[["relevant_experience", "job_change"]] = ds_jobs_transformed[["relevant_experience", "job_change"]].astype("bool")

ds_jobs_transformed[["student_id", "training_hours"]] = ds_jobs_transformed[["student_id", "training_hours"]].astype("int32")

ds_jobs_transformed["city_development_index"] = ds_jobs_transformed["city_development_index"].astype("float16")

ds_jobs_transformed[["city", "gender", "enrolled_university", "education_level", "major_discipline", "experience", "company_size", "company_type", 
                     "last_new_job"]] = ds_jobs_transformed[["city", "gender", "enrolled_university", "education_level", "major_discipline", "experience", "company_size", "company_type", "last_new_job"]].astype("category")

# Verify changes made

ds_jobs_transformed.info()

# Order category columns

ds_jobs_transformed["education_level"] = ds_jobs_transformed["education_level"].cat.set_categories(new_categories=["Primary School", "High School", "Graduate", "Masters", "Phd"], ordered=True)

ds_jobs_transformed["company_size"] = ds_jobs_transformed["company_size"].cat.set_categories(new_categories=["<10", "10-49", "50-99", "100-499", "500-999", "1000-4999", "5000-9999", "10000+"], ordered=True)

ds_jobs_transformed["last_new_job"] = ds_jobs_transformed["last_new_job"].cat.set_categories(new_categories=["never", "1", "2", "3", "4", ">4"], ordered=True)

ds_jobs_transformed["experience"] = ds_jobs_transformed["experience"].cat.set_categories(new_categories=["<1", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", ">20"], ordered=True)

ds_jobs_transformed["enrolled_university"] = ds_jobs_transformed["enrolled_university"].cat.set_categories(new_categories=["no_enrollment", "Part time course", "Full time course"], ordered=True)

# Create a filter for company size between 1000-4999 and experience equal or over 10 years

bigexperiencecompany = (ds_jobs_transformed["company_size"] >= "1000-4999") & (ds_jobs_transformed["experience"]>= "10")

ds_jobs_transformed = ds_jobs_transformed[bigexperiencecompany]

ds_jobs_transformed.info()
