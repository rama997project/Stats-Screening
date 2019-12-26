## 1. Introduction

### 1.1 Purpose

This document provides a comprehensive architectural overview of the system, using a number of different architectural 
views to depict different aspects of the system. It is intended to capture and convey the significant architectural 
decisions which have been made on the system.

### 1.2 Scope

<<<<<<< HEAD
This document describes the technical architecture of stats-screening, including module structure and dependencies as 
=======
This document describes the technical architecture of the bookly project, including module structure and dependencies as 
>>>>>>> 4cf1eb9fb247ff27c7e8d11194073e3f29363c64
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

<<<<<<< HEAD
| Reference                                                                        						    | Date       |
|-----------------------------------------------------------------------------------------------------------|------------|
| <a href="https://blog.bookly.online/">Bookly Blog</a>                         						    | 28/10/2019 |
| <a href="https://gitlab.com/project_bookly/bookly">GitLab Repository</a>         				            | 28/10/2019 |
| <a href="https://nicoschinacher.myjetbrains.com/youtrack/issues?q=project:%20bookly">YouTrack</a>			| 28/10/2019 |

### 1.5 Overview

This document contains the architectural representation, goals and constraints as well as logical, deployment, 
implementation and data views.
=======
| Reference                                                                        						              | Date       |
|-----------------------------------------------------------------------------------------------------------|------------|
| <a href="https://hertzsch2.wixsite.com/stats-screening">Stats Screening Blog</a>                         	| 25/12/2019 |
| <a href="https://github.com/GeorgHs/Stats-Screening">Git</a>         				                              | 25/12/2019 |
| <a href="https://dhbw-karlsruhe.myjetbrains.com/youtrack/agiles/108-5/109-115">YouTrack</a>			          | 25/12/2019 |

### 1.5 Overview

This document contains the architectural representation, goals and constraints.
>>>>>>> 4cf1eb9fb247ff27c7e8d11194073e3f29363c64

## 2. Architectural Representation

Our project bookly uses the classic MVC structure as follows:

<<<<<<< HEAD
![booklyMVC](booklyMVC.png "MVC diagram")

## 3. Architectural Goals And Constraints

As our main technology we decided to use Spring MVC, which is a framework that takes not only care of the backend but 
also of the frontend. Besides the controller and model language is Java, so that we do not have to care about 
serialization. 

=======
![MVC](MVC.png "Average MVC")

source: Telusko, 
## 3. Architectural Goals And Constraints

Main technology is Django MVT. This framework includes backend as well as frontend operations. Besides, the controller/template and model language is Python. That way we have to worry about serialization. 
>>>>>>> 4cf1eb9fb247ff27c7e8d11194073e3f29363c64

## 4. Use-Case View

This is our overall use-case diagram:

<<<<<<< HEAD
![Overall use-case diagram](design/usecase.png "Overall use-case diagram")
=======
![Use-case diagram](Use Case Diagram.png "Use Case Diagram")
>>>>>>> 4cf1eb9fb247ff27c7e8d11194073e3f29363c64

## 5. Logical View

### 5.1 Overview

We split our architecture according to the MVC architecture as follows:

<<<<<<< HEAD
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
=======
Model: Model is going to act as the interface of your data. It is responsible for maintaining data. It is the logical data structure behind the entire application and is represented by a database (generally relational databases such as MySql, Postgres).
View: The View is the user interface — what you see in your browser when you render a website. It is represented by HTML/CSS/Javascript and Jinja files.
Template: A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

Benefits of Django Architecture –

    Rapid Development
    Loosely Coupled
    Ease of Modification

Drawbacks of MVC Architecture –

    Too much load on Model Component
    Development Complexity is high
    Two components are controlling View


In Python Django its called Model View Template.
![MVT](MVT.png "Python MVT")
### 5.2 Architecturally Significant Design Packages

We have a backend and a frontend module. The backend module contains our model. The frontend module contains our view. 
The Django MVT framework is realized. The controller cannot directly access the database. 
>>>>>>> 4cf1eb9fb247ff27c7e8d11194073e3f29363c64


## 6. Process View

N/A

## 7. Deployment View

<<<<<<< HEAD
This is our deployment view:

![DeploymentView](design/deployment_view.png "Deployment View")

=======
N/A
>>>>>>> 4cf1eb9fb247ff27c7e8d11194073e3f29363c64

## 8. Implementation View

N/A

## 9. Data View

Our data view is modelled as followed:

<<<<<<< HEAD
![DataView](design/DatabaseERM.png "Data View")
=======
![DataView](DB.png "Data View")
>>>>>>> 4cf1eb9fb247ff27c7e8d11194073e3f29363c64

## 10. Size and Performance

N/A

## 11. Quality/Metrics

To ensure a high quality we are using continuous integration. It automatically builds, tests, 
measures and deploys the application, if the respective previous step has not failed. This happens periodically and when 
changes are pushed to a branch. When merging the master branch into the deployment branch, the application will 
automatically be deployed as well after pushing the button.

<<<<<<< HEAD
For serving a most current documentation of our API, we are using Swagger. It is an open-source software framework backed by a large ecosystem of tools that helps developers 
design, build, document, and consume RESTful web services. It is accessible at PATH/swagger-ui.html.
It's also possible to test an API and see all possible responses.
=======
For serving a most current documentation of our API, we are using autosummary/autodoc. It's constantly being updated. Using Sphinx as documentation language.

>>>>>>> 4cf1eb9fb247ff27c7e8d11194073e3f29363c64

## 12. Patterns

N/A
