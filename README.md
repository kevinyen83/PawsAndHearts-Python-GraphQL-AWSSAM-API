# Paws And Hearts-Pet Profile GraphQL API

![Alt text](https://github.com/kevinyen83/PawsAndHearts-AWSSAM-GraphQL-API/blob/main/screenshots/AWS.drawio.png)

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
