# rich_oak_test

Front end url = https://rich-oak-app.codemagic.app


## RICH OAK APP TEST API DOCUMENTATION

## Access

## Methods

  [ Jump to [Models](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Models) ]   

### Table of Contents 

#### [Accounts](file:///C:/Users/hp/Downloads/html-client-generated/index.html#Accounts)

- [`post /accounts/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#createAccountDetails)
- [`delete /accounts/{user_id}/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#destroyAccountDetails)
- [`get /accounts/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#listAccountDetails)
- [`patch /accounts/{user_id}/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#partialUpdateAccountDetails)
- [`get /accounts/{user_id}/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#retrieveAccountDetails)
- [`put /accounts/{user_id}/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#updateAccountDetails)

#### [Api](file:///C:/Users/hp/Downloads/html-client-generated/index.html#Api)

- [`post /api/token/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#createTokenObtainPair)
- [`post /api/token/refresh/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#createTokenRefresh)

#### [User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)

- [`post /user/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#createUser)
- [`delete /user/{id}/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#destroyUser)
- [`get /user/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#listUsers)
- [`patch /user/{id}/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#partialUpdateUser)
- [`get /user/{id}/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#retrieveUser)
- [`put /user/{id}/`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#updateUser)

# Accounts



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
post /accounts/
```

 (createAccountDetails)

### Consumes

​    This API call consumes the following media types via the Content-Type request header:    

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

### Request body

body [AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails) (optional)

Body Parameter —  

### Form parameters

id (optional)

Form Parameter —  

user (optional)

Form Parameter —  

bank_details (optional)

Form Parameter —  

account_balance (optional)

Form Parameter —  

id (optional)

Form Parameter —  

user (optional)

Form Parameter —  

bank_details (optional)

Form Parameter —  

account_balance (optional)

Form Parameter —  

### Return type

​      [AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)          

### Example data

Content-Type: application/json

```
{
  "account_balance" : 2.3021358869347655,
  "bank_details" : {
    "bank_code" : "bank_code",
    "credit_card" : 5,
    "name" : "name",
    "id" : 5
  },
  "id" : 0,
  "user" : {
    "is_superuser" : true,
    "is_active" : true,
    "user_permissions" : [ "user_permissions", "user_permissions" ],
    "is_staff" : true,
    "last_login" : "2000-01-23T04:56:07.000+00:00",
    "last_name" : "last_name",
    "groups" : [ "groups", "groups" ],
    "id" : 6,
    "date_joined" : "2000-01-23T04:56:07.000+00:00",
    "bvn" : 1,
    "first_name" : "first_name",
    "email" : ""
  }
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 201

[AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
delete /accounts/{user_id}/
```

 (destroyAccountDetails)

### Path parameters

user_id (required)

Path Parameter —  

### Responses

#### 204



------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
get /accounts/
```

 (listAccountDetails)

### Return type

​      array[[AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)]          

### Example data

Content-Type: application/json

```
[ {
  "account_balance" : 2.3021358869347655,
  "bank_details" : {
    "bank_code" : "bank_code",
    "credit_card" : 5,
    "name" : "name",
    "id" : 5
  },
  "id" : 0,
  "user" : {
    "is_superuser" : true,
    "is_active" : true,
    "user_permissions" : [ "user_permissions", "user_permissions" ],
    "is_staff" : true,
    "last_login" : "2000-01-23T04:56:07.000+00:00",
    "last_name" : "last_name",
    "groups" : [ "groups", "groups" ],
    "id" : 6,
    "date_joined" : "2000-01-23T04:56:07.000+00:00",
    "bvn" : 1,
    "first_name" : "first_name",
    "email" : ""
  }
}, {
  "account_balance" : 2.3021358869347655,
  "bank_details" : {
    "bank_code" : "bank_code",
    "credit_card" : 5,
    "name" : "name",
    "id" : 5
  },
  "id" : 0,
  "user" : {
    "is_superuser" : true,
    "is_active" : true,
    "user_permissions" : [ "user_permissions", "user_permissions" ],
    "is_staff" : true,
    "last_login" : "2000-01-23T04:56:07.000+00:00",
    "last_name" : "last_name",
    "groups" : [ "groups", "groups" ],
    "id" : 6,
    "date_joined" : "2000-01-23T04:56:07.000+00:00",
    "bvn" : 1,
    "first_name" : "first_name",
    "email" : ""
  }
} ]
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 200

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
patch /accounts/{user_id}/
```

 (partialUpdateAccountDetails)

### Path parameters

user_id (required)

Path Parameter —  

### Consumes

​    This API call consumes the following media types via the Content-Type request header:    

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

### Request body

body [AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails) (optional)

Body Parameter —  

### Form parameters

id (optional)

Form Parameter —  

user (optional)

Form Parameter —  

bank_details (optional)

Form Parameter —  

account_balance (optional)

Form Parameter —  

id (optional)

Form Parameter —  

user (optional)

Form Parameter —  

bank_details (optional)

Form Parameter —  

account_balance (optional)

Form Parameter —  

### Return type

​      [AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)          

### Example data

Content-Type: application/json

```
{
  "account_balance" : 2.3021358869347655,
  "bank_details" : {
    "bank_code" : "bank_code",
    "credit_card" : 5,
    "name" : "name",
    "id" : 5
  },
  "id" : 0,
  "user" : {
    "is_superuser" : true,
    "is_active" : true,
    "user_permissions" : [ "user_permissions", "user_permissions" ],
    "is_staff" : true,
    "last_login" : "2000-01-23T04:56:07.000+00:00",
    "last_name" : "last_name",
    "groups" : [ "groups", "groups" ],
    "id" : 6,
    "date_joined" : "2000-01-23T04:56:07.000+00:00",
    "bvn" : 1,
    "first_name" : "first_name",
    "email" : ""
  }
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 200

[AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
get /accounts/{user_id}/
```

 (retrieveAccountDetails)

### Path parameters

user_id (required)

Path Parameter —  

### Return type

​      [AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)          

### Example data

Content-Type: application/json

```
{
  "account_balance" : 2.3021358869347655,
  "bank_details" : {
    "bank_code" : "bank_code",
    "credit_card" : 5,
    "name" : "name",
    "id" : 5
  },
  "id" : 0,
  "user" : {
    "is_superuser" : true,
    "is_active" : true,
    "user_permissions" : [ "user_permissions", "user_permissions" ],
    "is_staff" : true,
    "last_login" : "2000-01-23T04:56:07.000+00:00",
    "last_name" : "last_name",
    "groups" : [ "groups", "groups" ],
    "id" : 6,
    "date_joined" : "2000-01-23T04:56:07.000+00:00",
    "bvn" : 1,
    "first_name" : "first_name",
    "email" : ""
  }
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 200

[AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
put /accounts/{user_id}/
```

 (updateAccountDetails)

### Path parameters

user_id (required)

Path Parameter —  

### Consumes

​    This API call consumes the following media types via the Content-Type request header:    

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

### Request body

body [AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails) (optional)

Body Parameter —  

### Form parameters

id (optional)

Form Parameter —  

user (optional)

Form Parameter —  

bank_details (optional)

Form Parameter —  

account_balance (optional)

Form Parameter —  

id (optional)

Form Parameter —  

user (optional)

Form Parameter —  

bank_details (optional)

Form Parameter —  

account_balance (optional)

Form Parameter —  

### Return type

​      [AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)          

### Example data

Content-Type: application/json

```
{
  "account_balance" : 2.3021358869347655,
  "bank_details" : {
    "bank_code" : "bank_code",
    "credit_card" : 5,
    "name" : "name",
    "id" : 5
  },
  "id" : 0,
  "user" : {
    "is_superuser" : true,
    "is_active" : true,
    "user_permissions" : [ "user_permissions", "user_permissions" ],
    "is_staff" : true,
    "last_login" : "2000-01-23T04:56:07.000+00:00",
    "last_name" : "last_name",
    "groups" : [ "groups", "groups" ],
    "id" : 6,
    "date_joined" : "2000-01-23T04:56:07.000+00:00",
    "bvn" : 1,
    "first_name" : "first_name",
    "email" : ""
  }
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 200

[AccountDetails](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)

------

# Api



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
post /api/token/
```

 (createTokenObtainPair)

Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

### Consumes

​    This API call consumes the following media types via the Content-Type request header:    

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

### Request body

body [TokenObtainPair](file:///C:/Users/hp/Downloads/html-client-generated/index.html#TokenObtainPair) (optional)

Body Parameter —  

### Form parameters

email (optional)

Form Parameter —  

password (optional)

Form Parameter —  

email (optional)

Form Parameter —  

password (optional)

Form Parameter —  

### Return type

​      [TokenObtainPair](file:///C:/Users/hp/Downloads/html-client-generated/index.html#TokenObtainPair)          

### Example data

Content-Type: application/json

```
{
  "password" : "password",
  "email" : "email"
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 201

[TokenObtainPair](file:///C:/Users/hp/Downloads/html-client-generated/index.html#TokenObtainPair)

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
post /api/token/refresh/
```

 (createTokenRefresh)

Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Consumes

​    This API call consumes the following media types via the Content-Type request header:    

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

### Request body

body [TokenRefresh](file:///C:/Users/hp/Downloads/html-client-generated/index.html#TokenRefresh) (optional)

Body Parameter —  

### Form parameters

refresh (optional)

Form Parameter —  

refresh (optional)

Form Parameter —  

### Return type

​      [TokenRefresh](file:///C:/Users/hp/Downloads/html-client-generated/index.html#TokenRefresh)          

### Example data

Content-Type: application/json

```
{
  "refresh" : "refresh"
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 201

[TokenRefresh](file:///C:/Users/hp/Downloads/html-client-generated/index.html#TokenRefresh)

------

# User



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
post /user/
```

 (createUser)

### Consumes

​    This API call consumes the following media types via the Content-Type request header:    

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

### Request body

body [User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User) (optional)

Body Parameter —  

### Form parameters

id (optional)

Form Parameter —  

last_login (optional)

Form Parameter —  format: date-time

is_superuser (optional)

Form Parameter —  

is_staff (optional)

Form Parameter —  

is_active (optional)

Form Parameter —  

date_joined (optional)

Form Parameter —  format: date-time

email (optional)

Form Parameter —  format: email

first_name (optional)

Form Parameter —  

last_name (optional)

Form Parameter —  

bvn (optional)

Form Parameter —  

groups (optional)

Form Parameter —  

user_permissions (optional)

Form Parameter —  

id (optional)

Form Parameter —  

last_login (optional)

Form Parameter —  format: date-time

is_superuser (optional)

Form Parameter —  

is_staff (optional)

Form Parameter —  

is_active (optional)

Form Parameter —  

date_joined (optional)

Form Parameter —  format: date-time

email (optional)

Form Parameter —  format: email

first_name (optional)

Form Parameter —  

last_name (optional)

Form Parameter —  

bvn (optional)

Form Parameter —  

groups (optional)

Form Parameter —  

user_permissions (optional)

Form Parameter —  

### Return type

​      [User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)          

### Example data

Content-Type: application/json

```
{
  "is_superuser" : true,
  "is_active" : true,
  "user_permissions" : [ "user_permissions", "user_permissions" ],
  "is_staff" : true,
  "last_login" : "2000-01-23T04:56:07.000+00:00",
  "last_name" : "last_name",
  "groups" : [ "groups", "groups" ],
  "id" : 0,
  "date_joined" : "2000-01-23T04:56:07.000+00:00",
  "bvn" : 6,
  "first_name" : "first_name",
  "email" : ""
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 201

[User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
delete /user/{id}/
```

 (destroyUser)

### Path parameters

id (required)

Path Parameter — A unique integer value identifying this user. 

### Responses

#### 204



------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
get /user/
```

 (listUsers)

### Return type

​      array[[User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)]          

### Example data

Content-Type: application/json

```
[ {
  "is_superuser" : true,
  "is_active" : true,
  "user_permissions" : [ "user_permissions", "user_permissions" ],
  "is_staff" : true,
  "last_login" : "2000-01-23T04:56:07.000+00:00",
  "last_name" : "last_name",
  "groups" : [ "groups", "groups" ],
  "id" : 0,
  "date_joined" : "2000-01-23T04:56:07.000+00:00",
  "bvn" : 6,
  "first_name" : "first_name",
  "email" : ""
}, {
  "is_superuser" : true,
  "is_active" : true,
  "user_permissions" : [ "user_permissions", "user_permissions" ],
  "is_staff" : true,
  "last_login" : "2000-01-23T04:56:07.000+00:00",
  "last_name" : "last_name",
  "groups" : [ "groups", "groups" ],
  "id" : 0,
  "date_joined" : "2000-01-23T04:56:07.000+00:00",
  "bvn" : 6,
  "first_name" : "first_name",
  "email" : ""
} ]
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 200

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
patch /user/{id}/
```

 (partialUpdateUser)

### Path parameters

id (required)

Path Parameter — A unique integer value identifying this user. 

### Consumes

​    This API call consumes the following media types via the Content-Type request header:    

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

### Request body

body [User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User) (optional)

Body Parameter —  

### Form parameters

id (optional)

Form Parameter —  

last_login (optional)

Form Parameter —  format: date-time

is_superuser (optional)

Form Parameter —  

is_staff (optional)

Form Parameter —  

is_active (optional)

Form Parameter —  

date_joined (optional)

Form Parameter —  format: date-time

email (optional)

Form Parameter —  format: email

first_name (optional)

Form Parameter —  

last_name (optional)

Form Parameter —  

bvn (optional)

Form Parameter —  

groups (optional)

Form Parameter —  

user_permissions (optional)

Form Parameter —  

id (optional)

Form Parameter —  

last_login (optional)

Form Parameter —  format: date-time

is_superuser (optional)

Form Parameter —  

is_staff (optional)

Form Parameter —  

is_active (optional)

Form Parameter —  

date_joined (optional)

Form Parameter —  format: date-time

email (optional)

Form Parameter —  format: email

first_name (optional)

Form Parameter —  

last_name (optional)

Form Parameter —  

bvn (optional)

Form Parameter —  

groups (optional)

Form Parameter —  

user_permissions (optional)

Form Parameter —  

### Return type

​      [User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)          

### Example data

Content-Type: application/json

```
{
  "is_superuser" : true,
  "is_active" : true,
  "user_permissions" : [ "user_permissions", "user_permissions" ],
  "is_staff" : true,
  "last_login" : "2000-01-23T04:56:07.000+00:00",
  "last_name" : "last_name",
  "groups" : [ "groups", "groups" ],
  "id" : 0,
  "date_joined" : "2000-01-23T04:56:07.000+00:00",
  "bvn" : 6,
  "first_name" : "first_name",
  "email" : ""
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 200

[User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
get /user/{id}/
```

 (retrieveUser)

### Path parameters

id (required)

Path Parameter — A unique integer value identifying this user. 

### Return type

​      [User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)          

### Example data

Content-Type: application/json

```
{
  "is_superuser" : true,
  "is_active" : true,
  "user_permissions" : [ "user_permissions", "user_permissions" ],
  "is_staff" : true,
  "last_login" : "2000-01-23T04:56:07.000+00:00",
  "last_name" : "last_name",
  "groups" : [ "groups", "groups" ],
  "id" : 0,
  "date_joined" : "2000-01-23T04:56:07.000+00:00",
  "bvn" : 6,
  "first_name" : "first_name",
  "email" : ""
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 200

[User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)

------



[Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods)

```
put /user/{id}/
```

 (updateUser)

### Path parameters

id (required)

Path Parameter — A unique integer value identifying this user. 

### Consumes

​    This API call consumes the following media types via the Content-Type request header:    

- `application/json`
- `application/x-www-form-urlencoded`
- `multipart/form-data`

### Request body

body [User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User) (optional)

Body Parameter —  

### Form parameters

id (optional)

Form Parameter —  

last_login (optional)

Form Parameter —  format: date-time

is_superuser (optional)

Form Parameter —  

is_staff (optional)

Form Parameter —  

is_active (optional)

Form Parameter —  

date_joined (optional)

Form Parameter —  format: date-time

email (optional)

Form Parameter —  format: email

first_name (optional)

Form Parameter —  

last_name (optional)

Form Parameter —  

bvn (optional)

Form Parameter —  

groups (optional)

Form Parameter —  

user_permissions (optional)

Form Parameter —  

id (optional)

Form Parameter —  

last_login (optional)

Form Parameter —  format: date-time

is_superuser (optional)

Form Parameter —  

is_staff (optional)

Form Parameter —  

is_active (optional)

Form Parameter —  

date_joined (optional)

Form Parameter —  format: date-time

email (optional)

Form Parameter —  format: email

first_name (optional)

Form Parameter —  

last_name (optional)

Form Parameter —  

bvn (optional)

Form Parameter —  

groups (optional)

Form Parameter —  

user_permissions (optional)

Form Parameter —  

### Return type

​      [User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)          

### Example data

Content-Type: application/json

```
{
  "is_superuser" : true,
  "is_active" : true,
  "user_permissions" : [ "user_permissions", "user_permissions" ],
  "is_staff" : true,
  "last_login" : "2000-01-23T04:56:07.000+00:00",
  "last_name" : "last_name",
  "groups" : [ "groups", "groups" ],
  "id" : 0,
  "date_joined" : "2000-01-23T04:56:07.000+00:00",
  "bvn" : 6,
  "first_name" : "first_name",
  "email" : ""
}
```

### Produces

​    This API call produces the following media types according to the Accept request header;    the media type will be conveyed by the Content-Type response header.    

- `application/json`

### Responses

#### 200

[User](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)

------

## Models

  [ Jump to [Methods](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Methods) ]   

### Table of Contents

1. [`AccountDetails`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails)
2. [`AccountDetails_bank_details`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails_bank_details)
3. [`AccountDetails_user`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails_user)
4. [`TokenObtainPair`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#TokenObtainPair)
5. [`TokenRefresh`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#TokenRefresh)
6. [`User`](file:///C:/Users/hp/Downloads/html-client-generated/index.html#User)

### `AccountDetails` [Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Models)

id (optional)

[Integer](file:///C:/Users/hp/Downloads/html-client-generated/index.html#integer)  

user (optional)

[AccountDetails_user](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails_user)  

bank_details (optional)

[AccountDetails_bank_details](file:///C:/Users/hp/Downloads/html-client-generated/index.html#AccountDetails_bank_details)  

account_balance (optional)

[BigDecimal](file:///C:/Users/hp/Downloads/html-client-generated/index.html#BigDecimal)  

### `AccountDetails_bank_details` [Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Models)

id (optional)

[Integer](file:///C:/Users/hp/Downloads/html-client-generated/index.html#integer)  

name 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

bank_code 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

credit_card (optional)

[Integer](file:///C:/Users/hp/Downloads/html-client-generated/index.html#integer)  

### `AccountDetails_user` [Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Models)

id (optional)

[Integer](file:///C:/Users/hp/Downloads/html-client-generated/index.html#integer)  

last_login (optional)

[Date](file:///C:/Users/hp/Downloads/html-client-generated/index.html#DateTime)  format: date-time

is_superuser (optional)

[Boolean](file:///C:/Users/hp/Downloads/html-client-generated/index.html#boolean) Designates that this user has all permissions without explicitly assigning them. 

is_staff (optional)

[Boolean](file:///C:/Users/hp/Downloads/html-client-generated/index.html#boolean) Designates whether the user can log into this admin site. 

is_active (optional)

[Boolean](file:///C:/Users/hp/Downloads/html-client-generated/index.html#boolean) Designates whether this user should be treated as active. Unselect this instead of deleting accounts. 

date_joined (optional)

[Date](file:///C:/Users/hp/Downloads/html-client-generated/index.html#DateTime)  format: date-time

email 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  format: email

first_name 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

last_name 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

bvn (optional)

[Integer](file:///C:/Users/hp/Downloads/html-client-generated/index.html#integer)  

groups (optional)

[array[String\]](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string) The groups this user belongs to. A user will get all permissions granted to each of their groups. 

user_permissions (optional)

[array[String\]](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string) Specific permissions for this user. 

### `TokenObtainPair` [Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Models)

email 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

password 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

### `TokenRefresh` [Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Models)

refresh 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

### `User` [Up](file:///C:/Users/hp/Downloads/html-client-generated/index.html#__Models)

id (optional)

[Integer](file:///C:/Users/hp/Downloads/html-client-generated/index.html#integer)  

last_login (optional)

[Date](file:///C:/Users/hp/Downloads/html-client-generated/index.html#DateTime)  format: date-time

is_superuser (optional)

[Boolean](file:///C:/Users/hp/Downloads/html-client-generated/index.html#boolean) Designates that this user has all permissions without explicitly assigning them. 

is_staff (optional)

[Boolean](file:///C:/Users/hp/Downloads/html-client-generated/index.html#boolean) Designates whether the user can log into this admin site. 

is_active (optional)

[Boolean](file:///C:/Users/hp/Downloads/html-client-generated/index.html#boolean) Designates whether this user should be treated as active. Unselect this instead of deleting accounts. 

date_joined (optional)

[Date](file:///C:/Users/hp/Downloads/html-client-generated/index.html#DateTime)  format: date-time

email 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  format: email

first_name 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

last_name 

[String](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string)  

bvn (optional)

[Integer](file:///C:/Users/hp/Downloads/html-client-generated/index.html#integer)  

groups (optional)

[array[String\]](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string) The groups this user belongs to. A user will get all permissions granted to each of their groups. 

user_permissions (optional)

[array[String\]](file:///C:/Users/hp/Downloads/html-client-generated/index.html#string) Specific permissions for this user. 
