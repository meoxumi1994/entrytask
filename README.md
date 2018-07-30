# Entry task

### Design Database :
![](https://i.imgur.com/5YZgfzK.png)

sql file : ./sql/create_table.sql

### API Endpoints :

all API body below using JSON format

##### Admin
```
request:
POST admin/create
body {
    email,
    user_name,
    password,
    address
}
response: 
body {
    status: 'success'
}
body {
    error: 'email has been used' || 'email is not valid' || 'missing field'
}
```

```
request:
GET admin/salt
params {
    user_name,
}
response: 
body {
    status: 'success',
    data: {
        salt: string
    }
}
body {
    error: 'token is not valid' 
}
```

```
request:
POST admin/login
body {
    user_name,
    password,
}
response: 
body {
    status: 'success',
    data: {
        access_token: string
    }
}
body {
    error: 'email and password not match' || 'email invalid'
}
```

```
request:
POST admin/event
header "entry-task-token" : access_token
body {
    location,
    title,
    description,
    event_time
}
response: 
body {
    status: 'success',
    data: {
        access_token: string
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```

```
request:
GET admin/category
header "entry-task-token" : access_token
response: 
body {
    status: 'success',
    data: {
        categories: [ ... ]
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```

```
request:
POST admin/photo
header "entry-task-token" : access_token
body {
    base64: 'base64 string of image'
}
response: 
body {
    status: 'success',
    data: {
        image_url
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```

##### Visitor

```
request:
POST visitor/comment
header "entry-task-token" : access_token
body {
    content,
    event_id
}
response: 
body {
    status: 'success',
}
body {
    error: 'auth fail' || 'missing field' 
}
```
```
request:
POST visitor/like
header "entry-task-token" : access_token
body {
    event_id
}
response: 
body {
    status: 'success',
}
body {
    error: 'auth fail' || 'missing field' 
}
```
```
request:
POST visitor/participant
header "entry-task-token" : access_token
body {
    event_id
}
response: 
body {
    status: 'success',
}
body {
    error: 'auth fail' || 'missing field' 
}
```

```
request:
GET visitor/search_event_by_tag
header "entry-task-token" : access_token
param {
    tag_prefix_string: ''
}
response: 
body {
    status: 'success',
    data: {
        events : [ 
            {
                title, location, description, create_by, create_time, event_time
            }, ...
        ]
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```

```
request:
GET visitor/search_by_category
header "entry-task-token" : access_token
param {
    category_id
}
response: 
body {
    status: 'success',
    data: {
        events : [ 
            {
                title, location, description, create_by, create_time, event_time
            }, ...
        ]
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```

```
request:
GET visitor/search_event_by_event_time
header "entry-task-token" : access_token
param {
    start_time,
    end_time
}
response: 
body {
    status: 'success',
    data: {
        events : [ 
            {
                title, location, description, create_by, create_time, event_time
            }, ...
        ]
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```
```
request:
GET visitor/event
header "entry-task-token" : access_token
param {
    event_id
}
response: 
body {
    status: 'success',
    data: {
        title, location, description, create_by, create_time, event_time
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```
```
request:
GET visitor/user
header "entry-task-token" : access_token
param {
    user_id
}
response: 
body {
    status: 'success',
    data: {
        user_name,
        first_name,
        last_name,
        full_name,
        avatar,
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```
```
request:
GET visitor/comment_by_event
header "entry-task-token" : access_token
param {
    event_id,
    last_time,
    limit
}
response: 
body {
    status: 'success',
    data: {
        comments: [ // sorted
            content,
            creat_time
        ]
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```
```
request:
GET visitor/comment_by_time
header "entry-task-token" : access_token
param {
    event_id,
    last_time,
    limit
}
response: 
body {
    status: 'success',
    data: {
        comments: [ // sorted
            content,
            creat_time
        ]
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```
```
request:
GET v1/like_total
header "entry-task-token" : access_token
param {
    event_id
}
response: 
body {
    status: 'success',
    data: {
        total_like
    }
}
body {
    error: 'auth fail' || 'missing field' 
}
```

# Run
install : Python, Django
install and run : Mysql, Memcached

open mysql and run file sql/create_table.sql

# Deploy

ssh to server
install an run ngnix

run server at 0.0.0.0:3000

# Test
go inside project
cd /test
chmod +x localhost_apis.sh server_apis.sh

./localhost_apis.sh // test API for localhost
./server_apis.sh // test API for server-deploy