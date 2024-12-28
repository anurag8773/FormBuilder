# Anurag Kumar Maurya

## Submission Checklist

- [x] Steps to run the project and documentation are included in a `README.md` file at the root of the project.
- [x] No binaries or compressed files have been added to the repository.
- [x] All pre-existing irrelevant files in the repository have been removed.
- [x] Screenshots have been added to the screenshots folder (optional for backend code).
- [x] All italicized placeholder instructions under submission headings have been replaced or removed.
- [x] You understand that this submission will be publicly visible.
- [x] You confirm that the submission is original work, not plagiarized or blatantly copied, and adheres to the code of ethics.

---

## Briefly Describe Your Project
This project is a Django-based Form Builder application that enables administrators to create customizable forms, users to submit responses, and provides analytics for submitted data. Admins can create unlimited forms with up to 100 questions, while users can respond anonymously. The application also generates insightful analytics for each form, such as response distribution and question-specific trends.

---

## Assumptions Made for This Project
- Users can submit responses anonymously without authentication.
- Admins are authenticated users with access to form creation and management functionalities.
- Text analytics only consider words with a minimum length of 5 characters.
- Top 5 data points are shown in analytics, aggregating the rest under "Others."

---

## Other Information (e.g., Testing Credentials)
None. The project APIs can be tested directly via Postman or curl.

---

## Key Learnings from This Assignment
- Implementation of Django Rest Framework for building robust APIs.
- Designing relational database models to handle dynamic form structures.
- Preprocessing analytics data for different question types (e.g., text fields, checkboxes, dropdowns).
- Structuring backend code for scalability and maintainability.
- Using serializers to validate nested input data.

---

## Time Taken to Complete the Project
Approximately 8-9 hours, including design, implementation, testing, and debugging.

---

## Potential Enhancements with More Time
- Add user authentication and role-based access control for enhanced security.
- Include more question types (e.g., file uploads, rating scales).
- Allow admins to edit forms and responses.
- Export analytics data as CSV or Excel files.
- Optimize performance for analytics calculations on large datasets.


