#### Question 1 (Code in rmongo Shell) ############

length(mongo.distinct(mongo, "coursework.tweets", "id_member"))


#### Question 2 (Code in Mongo Shell) ############


db.tweets.aggregate([{$group:{_id:"$id_member", 'count': {$sum:1}}},{$sort:{'count':-1}},{$limit:10}])

result <- mongo.aggregation(mongo, "coursework.tweets")
result1 <- mongo.bson.to.Robject(result)

users<- mongo.bson.to.Robject(result)
users

totalmessages <- mongo.count(mongo, tweets)# Count tweets


(result$result1$`0`$users / total)*100 # calculated percentage
(result$result1$`0`$users / total)*100

#### Question 3 (Code in Mongo Shell) ############

db.tweets.find().sort({timestamp:1}).limit(1) ##Earliest Date##

db.tweets.find().sort({timestamp:-1}).limit(1) ##latest Date##


earliestdate <- mongo.find.all(mongo, "coursework.tweets", fields = '{"timestamp":1}', 
                       sort = '{"timestamp":1}',
                       limit = 1L)[[1]]$timestamp
                       
lastestdate <- mongo.find.all(mongo, "coursework.tweet", fields = '{"timestamp":1}',
                       query = '{"timestamp" : { "$ne" : "NA" }}',
                       sort = '{"timestamp":-1}',
                       limit = 1L)[[1]]$timestamp

#### Question 4 (Code in rmongodb Shell) ############

timeT <- as.integer(as.POSIXct(last, tz = "UTC")) - as.integer(as.POSIXct(first, tz = "UTC"))
Meantime <- timeT / (mongo.count(mongo, "coursework.tweet") -1 )




#### Question 5 (Code in rmongodb Shell) ############



sum = 0; cursor <- mongo.find(mongo, "coursework.tweets", fields = '{"text":1}', 
                     query = '{"text" : {"$ne" : "Not wanted"}}')
while (mongo.cursor.next(cursor)) {
all <- mongo.cursor.value(cursor)
sum <- sum + nchar(mongo.bson.value(all, "text"))
}

count <- mongo.count(mongo, "coursework.tweets", query = '{"text" : {"$ne" : "Not wanted"}}')
average <- sum / count





#### Question 6 (Code in rmongodb Shell) ############







#### Question 7 (Code in rmongodb Shell) ############


sum = 0
cursor <- mongo.find(mongo, "coursework.tweets", fields = '{"text":1}', 
                     query = '{"text" : {"$ne" : "Not wanted"}}')
while (mongo.cursor.next(cursor)) {all <- mongo.bson.value(mongo.cursor.value(cursor), "text")
  										sum <- sum + str_count(all, "#")
}
average <- sum / count




#### Question 8 (Code in rmongodb Shell) ############









