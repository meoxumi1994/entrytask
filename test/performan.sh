#!/usr/bin/env bash
let "TOTAL_TIME = 1 / 2"
for i in {1..10}
 do
    echo test number = $i
    output=$(curl -s -w "%{time_total}\n" -o /dev/null -X POST \
      http://localhost:8000/admin/create_admin \
      -H 'Cache-Control: no-cache' \
      -H 'Content-Type: application/json' \
      -H 'Postman-Token: bbc73dd3-a3fc-49a4-97b6-dac25ea563cf' \
      -d '{
        "user_name" : "tran minh 12 13",
        "password" : "123456_hihi",
        "email" : "minhtd5@gmail.com",
        "address" : "213 binh thanh, hcm",
        "is_active" : 1
    } -f2')
    echo ouput $output
    let "TOTAL_TIME = TOTAL_TIME + ouput"
 done
    echo "total time" $TOTAL_TIME