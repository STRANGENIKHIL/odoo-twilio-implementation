
# Odoo Developer Internship Technical Assessment

**Company:** ZantaTech Solutions\
**Position:** Odoo Developer Intern\
**Duration:** 3--4 Hours\
**Difficulty:** Beginner to Intermediate

## Introduction

This practical assessment evaluates your understanding of:

-   Odoo Framework
-   Python
-   XML Views
-   ORM
-   Problem Solving

You may use:

-   Official Odoo Documentation
-   Google
-   Stack Overflow
-   ChatGPT or other AI tools

You must be able to explain every line of code during the interview.

------------------------------------------------------------------------

# Prerequisites

-   Odoo 18 or Odoo 19 Community Edition
-   Python 3.10+
-   PostgreSQL
-   Git
-   Visual Studio Code

------------------------------------------------------------------------

# Module

Create a custom module named:

``` text
phone_call_notes
```

------------------------------------------------------------------------

# Installation

1.  Copy the module into `custom_addons/`
2.  Update `addons_path`
3.  Restart Odoo
4.  Enable Developer Mode
5.  Update Apps List
6.  Install **Phone Call Notes**

Expected:

-   Phone menu appears
-   Call button appears on Contacts
-   Smart Button works
-   Call Logs menu works
-   No traceback errors

------------------------------------------------------------------------

# Business Requirement

Businesses record customer phone conversations.

Examples:

-   Sales Calls
-   Support Calls
-   Payment Follow-up
-   Order Confirmation
-   Lead Qualification

Each Call Log stores:

-   Customer
-   Phone Number
-   Date
-   Status
-   Notes
-   User

Workflow:

``` text
Open Contact
    ↓
Click Call
    ↓
Popup Opens
    ↓
Select Status
    ↓
Write Notes
    ↓
Save
    ↓
Create Call Log
    ↓
View History
```

Benefits:

-   Maintain communication history
-   Improve customer service
-   Track sales activity
-   Record discussions
-   Improve follow-up

------------------------------------------------------------------------

# Technical Tasks

## Task 1

Create module:

``` text
phone_call_notes
```

## Task 2

Add a **Call** button beside the Phone field in Contacts.

## Task 3

Popup fields:

-   Contact Name (Readonly)
-   Phone Number (Readonly)
-   Status
    -   Pending
    -   Connected
    -   Busy
    -   No Answer
-   Notes

Buttons:

-   Save
-   Cancel

## Task 4

Create model:

``` text
phone.call.log
```

Fields:

-   partner_id
-   phone
-   status
-   notes
-   call_date
-   user_id

Saving should create a Call Log.

## Task 5

Add Smart Button:

``` text
Call Logs (5)
```

It should display all logs for that contact.

## Task 6

Create menu:

``` text
Phone
└── Call Logs
```

Include:

-   Tree View
-   Form View
-   Search View

## Task 7

Security:

Only Internal Users should have access.

------------------------------------------------------------------------

# Bonus

-   Kanban View
-   Better UI
-   Color Status
-   Auto Current Date
-   Auto Current User

------------------------------------------------------------------------

# Expected UI

## Contact Form

``` text
John Smith

Phone
+91 9876543210   [ Call ]
```

## Popup

``` text
Call Contact

Customer
John Smith

Phone
+91 9876543210

Status
Connected

Notes
_____________

[Save]   [Cancel]
```

## Tree View

Columns:

-   Customer
-   Phone
-   Status
-   Date

## Form View

Display:

-   Customer
-   Phone
-   Status
-   Notes
-   User
-   Date

## Search View

Search by:

-   Customer
-   Phone
-   Status

------------------------------------------------------------------------

# Final Checklist

-   [ ] Module installs
-   [ ] Call Button works
-   [ ] Popup works
-   [ ] Save works
-   [ ] Smart Button works
-   [ ] Phone Menu works
-   [ ] Tree View works
-   [ ] Form View works
-   [ ] Search View works
-   [ ] Security works
-   [ ] No Errors

------------------------------------------------------------------------

# Submission

Submit:

-   Module ZIP
-   GitHub Repository (Preferred)
-   Installation Steps
-   2--3 Minute Demo Video

------------------------------------------------------------------------

# Interview Topics

Be prepared to explain:

-   Module Structure
-   Python Files
-   XML Files
-   ORM
-   Smart Button
-   Security
-   Relationships
-   Your Approach

You may also be asked to fix a bug or implement a minor feature.

------------------------------------------------------------------------

# Evaluation Criteria

  Criteria                  Marks
  --------------------- ---------
  Module Installation          20
  Python Models                15
  XML Views                    15
  ORM                          10
  Smart Button                 10
  Menu & Security              10
  Code Quality                 10
  UI                            5
  Git                           5
  Bonus Features               10
  **Total**               **100**
