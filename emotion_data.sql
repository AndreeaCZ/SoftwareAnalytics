create table emotion_data
as select * from filtered_data
where inte_first_emo != "" and inte_first_emo is not null