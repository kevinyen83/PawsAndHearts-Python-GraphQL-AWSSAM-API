# Paws And Hearts-Pet Profile GraphQL API

![Alt text](https://github.com/kevinyen83/PawsAndHearts-Python-GraphQL-AWSSAM-API/blob/main/screenshots/AWS.drawio.png)

## Introduction

This API is based on the Paws And Hearts project and provides a GraphQL interface for managing pet profiles. Users can create, get pet profile data and update pet availability values in the table through this interface. Please feel free to review the parent project: https://github.com/kevinyen83/PawsAndHearts

### Built With

![GraphQL](https://img.shields.io/badge/-GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

1.  Back-end development: Python
2.  API: GraphQL
3.  AWS: SAM, Lambda, CloudFormation, API Gateway, DynamoDB, S3
4.  CI/CD & DevOps: Docker

## Endpoint

GraphQL Endpoint URL:

```sh
https://<your-api-id>.execute-api.<your-region>.amazonaws.com/Prod/pet
```

# AWS API Gateway Configuration

To enable CORS and set headers for your methods in AWS API Gateway, follow these steps:

1.  **Open the AWS Management Console and navigate to API Gateway.**

2.  **Select your API and go to the "Resources" section.**

3.  **For each method (POST /pet, POST /pets, PATCH /pet):**

    - Click on the method and then select **"Method Request"**.
    - Under **"Settings"**, add `Content-Type` and `x-api-key` to the **"HTTP Request Headers"** section.

4.  **Go back to the method and select "Integration Request".**

    - Turn off `Lambda proxy integration` to allow manual setup of integration responses.
    - Expand **"HTTP Headers"** and add `Content-Type` and `x-api-key`.
    - **Turn off `API key required` in each "OPTIONS" method.**

5.  **Go back to the method and select "Method Response".**

    - Add a `200` status code response.
    - Under **"Response Headers for 200"**, add the following headers:
      - `Access-Control-Allow-Headers`
      - `Access-Control-Allow-Methods`
      - `Access-Control-Allow-Origin`

6.  **Go back to the method and select "Integration Response".**

    - Add a `200` status code response.
    - Map the following response headers:
      - `Access-Control-Allow-Headers` to the response header. Input:
        `'Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers'`
      - `Access-Control-Allow-Methods` to the response header. Input:
        `'DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT'`
      - `Access-Control-Allow-Origin` to the response header. Input:
        `'*'`

7.  **Deploy your API to the `Prod` stage.**

## Usage

### Swagger

For more details and to try out the API, please visit: https://kevinyen83.github.io/PawsAndHearts-Python-GraphQL-AWSSAM-API/

## Data Model

### PetInput

```
input PetInput {
  organizationName: String!
  applicantName: String!
  contactEmail: String!
  contactPhone: String!
  petId: ID!
  name: String!
  category: String!
  age: Int!
  color: String!
  gender: String!
  size: String!
  location: String!
  vaccination: String!
  availability: String!
  image: String!
  description: String!
}
```

### Pet

```
type Pet {
  petId: ID!
  organizationName: String!
  applicantName: String!
  contactEmail: String!
  contactPhone: String!
  name: String!
  category: String!
  age: Int!
  color: String!
  gender: String!
  size: String!
  location: String!
  vaccination: String!
  availability: String!
  image: String!
  description: String!
}
```

## Error Handling

If the request fails, the response will contain error information. For example:

```
{
  "errors": [
    {
      "message": "Pet not found",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "pet"
      ]
    }
  ],
  "data": null
}
```

## License

MIT License

## Contact

Currently looking for Front End Developer position in Sydney.
If you have any feedback or job opportunities, please feel free to contact me via LinkedIn / Email!

Kevin Yen - [@Kevin_linkedIn](https://www.linkedin.com/in/kerwinyen83/) - kevinyenhaha@gmail.com
