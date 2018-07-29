#!/usr/bin/env bash

curl -X POST \
      http://13.250.111.123:8080/admin/create \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran minh 12 13",
        "password" : "123456_hihi",
        "email" : "minhtd5@gmail.com",
        "address" : "213 binh thanh, hcm",
        "is_active" : 1
    }'
echo

curl -X GET \
  'http://13.250.111.123:8080/admin/salt?user_name=tran%20minh%20123' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc'
echo

curl -X POST \
      http://13.250.111.123:8080/admin/login \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "password" : "26b2dc49c4eb8a1f4cbed900b86c02035a69d998a6b7ff633b7726a27b8b05cfda9ac2b57c073ac52ddbdfe6a4a7ae4adaf4b2abb907c76ae4bde76df1350fff"
    }'
echo

curl -X POST \
      http://13.250.111.123:8080/admin/login \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran minh 12 13",
        "password" : "26b2dc49c4eb8a1f4cbed900b86c02035a69d998a6b7ff633b7726a27b8b05cfda9ac2b57c073ac52ddbdfe6a4a7ae4adaf4b2abb907c76ae4bde76df1350fff"
    }'
echo

curl -X GET \
  'http://13.250.111.123:8080/admin/get?user_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc'
echo

curl -X GET \
  'http://13.250.111.123:8080/admin/get?user_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDA5OjU2OjA1IiwicGFzc3dvcmQiOiIyNmIyZGM0OWM0ZWI4YTFmNGNiZWQ5MDBiODZjMDIwMzVhNjlkOTk4YTZiN2ZmNjMzYjc3MjZhMjdiOGIwNWNmZGE5YWMyYjU3YzA3M2FjNTJkZGJkZmU2YTRhN2FlNGFkYWY0YjJhYmI5MDdjNzZhZTRiZGU3NmRmMTM1MGZmZiIsInVzZXJfbmFtZSI6InRyYW4gbWluaCAxMiAxMyIsImlkIjo4fQ.j70bvUUQJX2WZNsYUf3ENHYbRxMf4eO1NxGCx8PP9dg'
echo

curl -X POST \
  http://13.250.111.123:8080/admin/event \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: f0772c5b-c2ff-4e8b-86a4-c0f620db6a8b' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDA5OjU2OjA1IiwicGFzc3dvcmQiOiIyNmIyZGM0OWM0ZWI4YTFmNGNiZWQ5MDBiODZjMDIwMzVhNjlkOTk4YTZiN2ZmNjMzYjc3MjZhMjdiOGIwNWNmZGE5YWMyYjU3YzA3M2FjNTJkZGJkZmU2YTRhN2FlNGFkYWY0YjJhYmI5MDdjNzZhZTRiZGU3NmRmMTM1MGZmZiIsInVzZXJfbmFtZSI6InRyYW4gbWluaCAxMiAxMyIsImlkIjo4fQ.j70bvUUQJX2WZNsYUf3ENHYbRxMf4eO1NxGCx8PP9dg' \
  -d '{
	"title" : "di choi",
	"event_time" : "2018-07-27 04:04:21",
	"description" : "20 10 ngay quoc te phu nu viet nam"
}'
echo

curl -X GET \
  'http://13.250.111.123:8080/admin/category' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDA5OjU2OjA1IiwicGFzc3dvcmQiOiIyNmIyZGM0OWM0ZWI4YTFmNGNiZWQ5MDBiODZjMDIwMzVhNjlkOTk4YTZiN2ZmNjMzYjc3MjZhMjdiOGIwNWNmZGE5YWMyYjU3YzA3M2FjNTJkZGJkZmU2YTRhN2FlNGFkYWY0YjJhYmI5MDdjNzZhZTRiZGU3NmRmMTM1MGZmZiIsInVzZXJfbmFtZSI6InRyYW4gbWluaCAxMiAxMyIsImlkIjo4fQ.j70bvUUQJX2WZNsYUf3ENHYbRxMf4eO1NxGCx8PP9dg'
echo

curl -X POST \
  http://13.250.111.123:8080/admin/photo \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 00817a12-5e35-4f32-ae41-8cb88e08e751' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDEwOjU5OjM0IiwicGFzc3dvcmQiOiIyNmIyZGM0OWM0ZWI4YTFmNGNiZWQ5MDBiODZjMDIwMzVhNjlkOTk4YTZiN2ZmNjMzYjc3MjZhMjdiOGIwNWNmZGE5YWMyYjU3YzA3M2FjNTJkZGJkZmU2YTRhN2FlNGFkYWY0YjJhYmI5MDdjNzZhZTRiZGU3NmRmMTM1MGZmZiIsInVzZXJfbmFtZSI6InRyYW4gbWluaCAxMiAxMyIsImlkIjo4fQ.AVF7gnOdpU3ikv8wDl5nEL7XELuKvNCw2WA27nVlkY8' \
  -d '{
	"base64" : "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
}'

curl -X POST \
      http://13.250.111.123:8080/visitor/create \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran",
        "password" : "123456_hihi",
        "email" : "minhtd5@gmail.com",
        "address" : "213 binh thanh, hcm",
        "is_active" : 1
    }'
echo

curl -X GET \
  'http://13.250.111.123:8080/visitor/salt?user_name=tran' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc'
echo

curl -X POST \
      http://13.250.111.123:8080/visitor/login \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran",
        "password" : "4d46452a1bb2726f3fd9ee394aa0bfa5364c57f931267c70e9bd5e2d9f755ec6a0b2b6bc68e14ddfe50462f0fb9ba26c540bcb23de16dcf81ad43a40d92d4893"
    }'
echo

curl -X POST \
      http://13.250.111.123:8080/visitor/login \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran minh 12 13",
        "password" : "123456_hihi"
    }'
echo

curl -X GET \
  'http://13.250.111.123:8080/visitor/get?user_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc'
echo

curl -X GET \
  'http://13.250.111.123:8080/visitor/get?user_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDEwOjU0OjM5IiwicGFzc3dvcmQiOiI0ZDQ2NDUyYTFiYjI3MjZmM2ZkOWVlMzk0YWEwYmZhNTM2NGM1N2Y5MzEyNjdjNzBlOWJkNWUyZDlmNzU1ZWM2YTBiMmI2YmM2OGUxNGRkZmU1MDQ2MmYwZmI5YmEyNmM1NDBiY2IyM2RlMTZkY2Y4MWFkNDNhNDBkOTJkNDg5MyIsInVzZXJfbmFtZSI6InRyYW4iLCJpZCI6MTB9.k2Edi2Hw-xjZNyG-VTsUAd5-De9uc3xTKAJjdpPYgDA'
echo

