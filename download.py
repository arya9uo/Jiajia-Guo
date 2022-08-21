import wget

common_prefix = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
cab_prefix = ["yellow", "fhvhv"]
timespan = ["2021-11", "2021-12", "2022-01", "2022-02"]
common_suffix = "parquet"


# download yellow taxis and fhvhv datasets
for cab in cab_prefix:
    url = common_prefix + cab + "_" "tripdata" + "_"
    for time in timespan:
        real_url = url + time + "." + common_suffix
        print(real_url) 
        wget.download(real_url)

# download covid-19 2021 and 2022
wget.download("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2022.csv")
wget.download("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2021.csv")

