## 1. Introduction

### 1.1 Purpose

This document provides a comprehensive architectural overview of the system, using a number of different architectural 
views to depict different aspects of the system. It is intended to capture and convey the significant architectural 
decisions which have been made on the system.

### 1.2 Scope

This document describes the technical architecture of the bookly project, including module structure and dependencies as 
well as the structure of classes.

### 1.3 Definitions, Acronyms and Abbreviations

| Abbreviation | Description                            |
| ------------ | -------------------------------------- |
| API          | Application programming interface      |
| MVC          | Model View Controller                  |
| REST         | Representational state transfer        |
| SDK          | Software development kit               |
| SRS          | Software Requirements Specification    |
| UC           | Use Case                               |
| VCS          | Version Control System                 |
| N/A          | Not Applicable                         |

### 1.4 References

| Reference                                                                        						              | Date       |
|-----------------------------------------------------------------------------------------------------------|------------|
| <a href="https://hertzsch2.wixsite.com/stats-screening">Stats Screening Blog</a>                         	| 25/12/2019 |
| <a href="https://github.com/GeorgHs/Stats-Screening">Git</a>         				                              | 25/12/2019 |
| <a href="https://dhbw-karlsruhe.myjetbrains.com/youtrack/agiles/108-5/109-115">YouTrack</a>			          | 25/12/2019 |

### 1.5 Overview

This document contains the architectural representation, goals and constraints.

## 2. Architectural Representation

Our project bookly uses the classic MVC structure as follows:

In Python Django its called Model View Template.
![MVT](MVT/MVT.png "Python MVT")

## 3. Architectural Goals And Constraints

As our main technology we decided to use Spring MVC, which is a framework that takes not only care of the backend but 
also of the frontend. Besides the controller and model language is Java, so that we do not have to care about 
serialization. 


## 4. Use-Case View

This is our overall use-case diagram:

![Overall use-case diagram](design/usecase.png "Overall use-case diagram")

## 5. Logical View

### 5.1 Overview

We split our architecture according to the MVC architecture as follows:

Spring uses a Dispatcher Servlet that accepts requests and forwards to the view resolver. 
This resolver serves our view files. See steps 1, 6, 7 and 8. This is our controller according to the MVC model.
![Controller](design/maven_mvc.png "controller")

The backend serves as the model according to the MVC model.
![Model](design/class_diagram.png "Model")

The frontend serves as the view according to the MVC model.
![View](design/VIEW.png "View")

### 5.2 Architecturally Significant Design Packages

We have a backend and a frontend module. The backend module contains our model. The frontend module contains our view. 
The Spring MVC framework is realized. The controller cannot directly access the database. 


## 6. Process View

N/A

## 7. Deployment View

This is our deployment view:

![DeploymentView](design/deployment_view.png "Deployment View")


## 8. Implementation View

N/A

## 9. Data View

Our data view is modelled as followed:

![DataView](design/DatabaseERM.png "Data View")

## 10. Size and Performance

N/A

## 11. Quality/Metrics

To ensure a high quality we are using continuous integration. It automatically builds, tests, 
measures and deploys the application, if the respective previous step has not failed. This happens periodically and when 
changes are pushed to a branch. When merging the master branch into the deployment branch, the application will 
automatically be deployed as well after pushing the button.

For serving a most current documentation of our API, we are using Swagger. It is an open-source software framework backed by a large ecosystem of tools that helps developers 
design, build, document, and consume RESTful web services. It is accessible at PATH/swagger-ui.html.
It's also possible to test an API and see all possible responses.

## 12. Patterns

N/A
