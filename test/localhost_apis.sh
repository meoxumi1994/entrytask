#!/usr/bin/env bash

curl -X POST \
      http://localhost:8000/admin/create \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran minh 12 13666",
        "password" : "123456_hihi",
        "email" : "minhtd5@gmail.com",
        "address" : "213 binh thanh, hcm",
        "is_active" : 1
    }'
echo

curl -X POST \
      http://localhost:8000/admin/create \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "meoxumi1994",
        "password" : "123456",
        "email" : "minhtd5@gmail.com",
        "address" : "213 binh thanh, hcm",
        "is_active" : 1
    }'
echo

curl -X GET \
  'http://localhost:8000/admin/salt?user_name=meoxumi1994' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc'
echo

curl -X POST \
      http://localhost:8000/admin/login \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "ducminh",
        "password" : "71577625d304c36397deaf1f941af51a54096a67e9675dc17b9f87bdb868f65cfe32701b2c9efdba65625fc98cef9d4ff3ceffbba310a1e1ab601b443ff18e72"
    }'
echo

curl -X GET \
  'http://localhost:8000/admin/get?user_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc'
echo

curl -X GET \
  'http://localhost:8000/admin/get?user_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDA5OjU2OjA1IiwicGFzc3dvcmQiOiIyNmIyZGM0OWM0ZWI4YTFmNGNiZWQ5MDBiODZjMDIwMzVhNjlkOTk4YTZiN2ZmNjMzYjc3MjZhMjdiOGIwNWNmZGE5YWMyYjU3YzA3M2FjNTJkZGJkZmU2YTRhN2FlNGFkYWY0YjJhYmI5MDdjNzZhZTRiZGU3NmRmMTM1MGZmZiIsInVzZXJfbmFtZSI6InRyYW4gbWluaCAxMiAxMyIsImlkIjo4fQ.j70bvUUQJX2WZNsYUf3ENHYbRxMf4eO1NxGCx8PP9dg'
echo

curl -X POST \
  http://localhost:8000/admin/event \
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
  'http://localhost:8000/admin/category' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDA5OjU2OjA1IiwicGFzc3dvcmQiOiIyNmIyZGM0OWM0ZWI4YTFmNGNiZWQ5MDBiODZjMDIwMzVhNjlkOTk4YTZiN2ZmNjMzYjc3MjZhMjdiOGIwNWNmZGE5YWMyYjU3YzA3M2FjNTJkZGJkZmU2YTRhN2FlNGFkYWY0YjJhYmI5MDdjNzZhZTRiZGU3NmRmMTM1MGZmZiIsInVzZXJfbmFtZSI6InRyYW4gbWluaCAxMiAxMyIsImlkIjo4fQ.j70bvUUQJX2WZNsYUf3ENHYbRxMf4eO1NxGCx8PP9dg'
echo

curl -X POST \
  http://localhost:8000/admin/photo \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 00817a12-5e35-4f32-ae41-8cb88e08e751' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDEwOjU5OjM0IiwicGFzc3dvcmQiOiIyNmIyZGM0OWM0ZWI4YTFmNGNiZWQ5MDBiODZjMDIwMzVhNjlkOTk4YTZiN2ZmNjMzYjc3MjZhMjdiOGIwNWNmZGE5YWMyYjU3YzA3M2FjNTJkZGJkZmU2YTRhN2FlNGFkYWY0YjJhYmI5MDdjNzZhZTRiZGU3NmRmMTM1MGZmZiIsInVzZXJfbmFtZSI6InRyYW4gbWluaCAxMiAxMyIsImlkIjo4fQ.AVF7gnOdpU3ikv8wDl5nEL7XELuKvNCw2WA27nVlkY8' \
  -d '{
	"base64" : "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
}'

curl -X POST \
      http://localhost:8000/api/create \
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
  'http://localhost:8000/api/salt?user_name=tran' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc'
echo

curl -X POST \
      http://localhost:8000/api/login \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran",
        "password" : "4d46452a1bb2726f3fd9ee394aa0bfa5364c57f931267c70e9bd5e2d9f755ec6a0b2b6bc68e14ddfe50462f0fb9ba26c540bcb23de16dcf81ad43a40d92d4893"
    }'
echo

curl -X POST \
      http://localhost:8000/api/login \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran minh 12 13",
        "password" : "123456_hihi"
    }'
echo

curl -X GET \
  'http://localhost:8000/api/get?user_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc'
echo

curl -X GET \
  'http://localhost:8000/api/get?user_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a6322d1a-2433-407b-a30e-6fdaa85890cc' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA3LTMxIDEwOjU0OjM5IiwicGFzc3dvcmQiOiI0ZDQ2NDUyYTFiYjI3MjZmM2ZkOWVlMzk0YWEwYmZhNTM2NGM1N2Y5MzEyNjdjNzBlOWJkNWUyZDlmNzU1ZWM2YTBiMmI2YmM2OGUxNGRkZmU1MDQ2MmYwZmI5YmEyNmM1NDBiY2IyM2RlMTZkY2Y4MWFkNDNhNDBkOTJkNDg5MyIsInVzZXJfbmFtZSI6InRyYW4iLCJpZCI6MTB9.k2Edi2Hw-xjZNyG-VTsUAd5-De9uc3xTKAJjdpPYgDA'
echo

curl -X GET \
  'http://localhost:8000/api/event_get_by_id?event_id=1' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 9bd81897-8162-4f12-b5b6-bff25eff6a48' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA4LTAyIDA0OjI0OjI5IiwicGFzc3dvcmQiOiIyNmIyZGM0OWM0ZWI4YTFmNGNiZWQ5MDBiODZjMDIwMzVhNjlkOTk4YTZiN2ZmNjMzYjc3MjZhMjdiOGIwNWNmZGE5YWMyYjU3YzA3M2FjNTJkZGJkZmU2YTRhN2FlNGFkYWY0YjJhYmI5MDdjNzZhZTRiZGU3NmRmMTM1MGZmZiIsInVzZXJfbmFtZSI6InRyYW4gbWluaCAxMiAxMyIsImlkIjo4fQ.T6HnIobC9WTwJfV5YxFQOCqEILag4-6ucrEG_OJ0eyc'
echo


curl -X GET \
  'http://localhost:8000/api/event_search_by_tag?tag_name=coffee' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 3cd26711-4bbd-42fb-b263-a47db83eaa43' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA4LTAyIDA2OjI4OjEzIiwicGFzc3dvcmQiOiIxNWIxMmRkZjA2Yzk1NmQwODExNzZlOGY0OTAyM2Q3NmMzMjZhMGU3NDUwMTIxMWM0NzYzNjRjZWFiMmE2MGMyMjg3YmZjZjg5NzgyMDQ0MWM1ZmZkZmZhNTA0ZmE5ZWUxZTEzMzE1Njc1M2E2YjMyZWNkMDg1Y2Y2ZjM3OTY0NiIsInVzZXJfbmFtZSI6InRyYW4iLCJpZCI6Mn0.hmHeJnwJONhMc4Z7uX6c_PjjqKEWRIvQ9xamXbQpPXs'
echo

curl -X GET \
  'http://localhost:8000/api/event_search_by_event_time?start_time=1533024509&end_time=1533024509' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: bbeb3ebf-09f5-4350-aa25-4109e6dbca2b' \
  -H 'entry-task-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmF0aW9uX2RhdGUiOiIyMDE4LTA4LTAyIDA2OjI4OjEzIiwicGFzc3dvcmQiOiIxNWIxMmRkZjA2Yzk1NmQwODExNzZlOGY0OTAyM2Q3NmMzMjZhMGU3NDUwMTIxMWM0NzYzNjRjZWFiMmE2MGMyMjg3YmZjZjg5NzgyMDQ0MWM1ZmZkZmZhNTA0ZmE5ZWUxZTEzMzE1Njc1M2E2YjMyZWNkMDg1Y2Y2ZjM3OTY0NiIsInVzZXJfbmFtZSI6InRyYW4iLCJpZCI6Mn0.hmHeJnwJONhMc4Z7uX6c_PjjqKEWRIvQ9xamXbQpPXs'
echo




