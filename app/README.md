
# Work Order API Documentation

The Work Order API provides endpoints for managing work orders in the property management system, specifically designed for hotels.

## Base URL

The base URL for the Work Order API is:

https://your-api-domain.com/api/v1/work_order

## Authentication

Authentication is required to access the Work Order API. The API uses OAuth2 for authentication. You need to obtain an access token to make authorized requests.

### Generating Access Token

To generate an access token, use the following endpoint:

**Endpoint:** `/oauth/token` **Method:** POST

#### Request

> {   "grant_type": "client_credentials",   "user_info": {
>     "client_id": "your_client_id",
>     "client_secret": "your_client_secret"   } }

-   `grant_type`: Set to `"client_credentials"`.
-   `client_id` and `client_secret`: Your client credentials.

#### Response

> {   "access_token": "your_access_token",   "token_type": "bearer" }

### Getting Access Token

To get an access token, use the following endpoint:

**Endpoint:** `/oauth/token` **Method:** GET

#### Request

> {   "grant_type": "get_client_credentials",   "user_info": {
>     "client_id": "your_client_id",
>     "client_secret": "your_client_secret"   } }

-   `grant_type`: Set to `"get_client_credentials"`.
-   `client_id` and `client_secret`: Your client credentials.

#### Response

> {   "access_token": "your_access_token",   "token_type": "bearer" }

## Endpoints

### List Work Orders

**Endpoint:** `/` **Method:** GET

Retrieve a list of work orders.

#### Request Parameters

-   `skip` (optional): Number of records to skip (default is 0).
-   `limit` (optional): Maximum number of records to return (default is 10).

#### Response

> [   {
>     "work_order_number": "WO001",
>     "created_by": "Maid Supervisor",
>     "assigned_to": "Housekeeping Staff",
>     "room": "101",
>     "started_at": "2023-09-30T08:00:00",
>     "finished_at": "2023-09-30T10:00:00",
>     "type": "Cleaning",
>     "status": "Done"   },   {
>     "work_order_number": "WO002",
>     "created_by": "Guest",
>     "assigned_to": "Maintenance Technician",
>     "room": "202",
>     "started_at": "2023-09-30T14:00:00",
>     "finished_at": null,
>     "type": "Technician Request",
>     "status": "Assigned"   } ]

### Get Work Order by ID

**Endpoint:** `/{work_order_id}` **Method:** GET

Retrieve a specific work order by its unique ID.

#### Response

> {   "work_order_number": "WO001",   "created_by": "Maid Supervisor",  
> "assigned_to": "Housekeeping Staff",   "room": "101",   "started_at":
> "2023-09-30T08:00:00",   "finished_at": "2023-09-30T10:00:00",  
> "type": "Cleaning",   "status": "Done" }

### Create Work Order

**Endpoint:** `/` **Method:** POST

Create a new work order.

#### Request

> {   "work_order_number": "WO003",   "created_by": "Maid Supervisor",  
> "assigned_to": "Housekeeping Staff",   "room": "203",   "started_at":
> "2023-09-30T16:00:00",   "type": "Cleaning",   "status": "Created" }

#### Response

> {   "work_order_number": "WO003",   "created_by": "Maid Supervisor",  
> "assigned_to": "Housekeeping Staff",   "room": "203",   "started_at":
> "2023-09-30T16:00:00",   "type": "Cleaning",   "status": "Created" }

### Update Work Order

**Endpoint:** `/{work_order_id}` **Method:** PUT

Update an existing work order by its ID.

#### Request

> {   "status": "In Progress" }

#### Response

> {   "work_order_number": "WO003",   "created_by": "Maid Supervisor",  
> "assigned_to": "Housekeeping Staff",   "room": "203",   "started_at":
> "2023-09-30T16:00:00",   "type": "Cleaning",   "status": "In Progress"
> }

## Error Handling

-   If an error occurs during an API request, the API will return an error response with an appropriate HTTP status code and error message.

Sample error response:

> {   "detail": "An error occurred during the request." }

The API includes error handling for common scenarios such as invalid input data, authentication failures, and internal server errors. Specific error messages and status codes are provided to assist in troubleshooting.

-------------------------------------------------------------------------
| Work Order ID | Created By    | Assigned To     | Room | Started At       | Finished At      | Type            | Status     |
-------------------------------------------------------------------------
| WO001         | Maid Supervisor | Housekeeping Staff | 101  | 2023-09-30 08:00 | 2023-09-30 10:00 | Cleaning         | Done       |
-------------------------------------------------------------------------
| WO002         | Guest          | Maintenance Technician | 202 | 2023-09-30 14:00 | null             | Technician Request | Assigned   |
-------------------------------------------------------------------------
| WO003         | Maid Supervisor | Housekeeping Staff | 203  | 2023-09-30 16:00 | null             | Cleaning         | Created    |
-------------------------------------------------------------------------
| WO004         | Guest          | Maintenance Technician | 204 | 2023-09-30 09:30 | null             | Technician Request | Created    |
-------------------------------------------------------------------------
| WO005         | Maid Supervisor | Housekeeping Staff | 102  | 2023-09-30 11:30 | 2023-09-30 13:30 | Cleaning         | Done       |
-------------------------------------------------------------------------
