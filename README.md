# Cab Drivers NGinx-Flask-Postgres System 

This system takes an NGinx-Flask-Postgres Database deployment and modifies it into an API cloud system. 

## Usage

1. Bootstrap the DB
```bash
docker-compose up -d db
docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"
```

2. Bring up the cluster
```bash
docker-compose up -d
```

3. Browse to localhost:8080 to see the app in action.

4. Insert the data

5. Use the postman requests to make the enpoint queries


### Insert the data into the Postgres Docker Container
```
docker ps
docker exec -it cab_trips_db_1 bash
psql flaskapp_db postgres
\dt
\d+ medallions
```

### Insert Data
```
INSERT INTO medallions (medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance) 
VALUES ('aaa', 'license-code', 'sssvendor_id', 'ppp_ratecode', 'flag', TIMESTAMP '2011-05-14 15:36:38', TIMESTAMP '2011-05-16 15:39:38', 5, 43434343, 14.4 );

INSERT INTO medallions (medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance) 
VALUES ('aaa', 'license-code', 'sssvendor_id', 'ppp_ratecode', 'flag', TIMESTAMP '2011-06-16 15:35:38', TIMESTAMP '2011-05-16 15:39:38', 5, 43434343, 14.4 );

INSERT INTO medallions (medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance) 
VALUES ('aaa', 'license-code', 'sssvendor_id', 'ppp_ratecode', 'flag', TIMESTAMP '2011-05-16 12:36:18', TIMESTAMP '2011-05-16 15:39:38', 5, 43434343, 14.4 );

INSERT INTO medallions (medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance) 
VALUES ('aaa', 'license-code', 'sssvendor_id', 'ppp_ratecode', 'flag', TIMESTAMP '2011-05-16 12:36:38', TIMESTAMP '2011-05-16 15:39:38', 5, 43434343, 14.4 );

INSERT INTO medallions (medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance) 
VALUES ('bbb', 'license-code', 'sssvendor_id', 'ppp_ratecode', 'flag', TIMESTAMP '2011-05-16 15:36:38', TIMESTAMP '2011-05-16 15:39:38', 5, 43434343, 14.4 );

INSERT INTO medallions (medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance) 
VALUES ('bbb', 'license-code', 'sssvendor_id', 'ppp_ratecode', 'flag', TIMESTAMP '2011-05-16 15:16:38', TIMESTAMP '2011-05-16 15:39:38', 5, 43434343, 14.4 );

```


### Remove all docker containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

### Transfer files to cloud server
sudo scp -i <key_file> -r user_management_system ubuntu@ec2-13-211-112-10.ap-southeast-2.compute.amazonaws.com:~/.
ssh -i "<key_file>" ubuntu@ec2-13-211-112-10.ap-southeast-2.compute.amazonaws.com

#### Open the endpoints with Postman to access the API