create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,              71,              "Cambridge"        union
  select 45,              93,              "Minneapolis"      union
  select 33,             177,              "San Diego"        union
  select 26,              88,              "Miami"            union
  select 98,               0,              "North Pole";

create table cold as
  select name from cities where latitude >= 43;

create table distance as
  select a.name as first, b.name as second,
         60*(b.latitude - a.latitude) as distance
         from cities as a, cities as b;

