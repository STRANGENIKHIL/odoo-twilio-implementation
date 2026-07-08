# Odoo Developer Internship Demo - Video Preparation Guide

This guide contains the step-by-step recording flow and narration script for your 2–3 minute demonstration video. Follow these steps sequentially to showcase all requirements and bonus features.

---

## 📋 Pre-Video Checklist

1. **Local Server Running**: Ensure Odoo and PostgreSQL are running locally.
2. **Clean State**: Delete any messy test call logs so the dashboard starts clean.
3. **Developer Mode**: Ensure developer mode is active so you can show the Apps menu options if needed.
4. **Test Contact**: Have a contact ready (e.g., *Deco Addict*) with a phone number filled in.

---

## 🎥 Video Walkthrough Script

### Part 1: Intro & Module Installation (approx. 20 seconds)
*   **On-Screen Action**: 
    1. Open your browser to `http://localhost:8069`.
    2. Navigate to **Apps** -> Search for `Phone Call Notes`.
    3. Hover your cursor over the module card showing it is **Installed**.
*   **Narration Script**: 
    > *"Hello, this is a demonstration of the custom Odoo 18 module `phone_call_notes` developed for the Odoo Developer Intern technical assessment. As you can see, the module installs cleanly under Odoo Apps without any traceback errors, which covers Task 1 and our initial installation checklist."*

---

### Part 2: Contact Form & Inline Call Button (approx. 40 seconds)
*   **On-Screen Action**:
    1. Click on the top-left home menu and open **Contacts**.
    2. Select an existing contact that has a phone number (e.g., *Deco Addict*).
    3. Point your mouse to the **Call** button inline next to the phone number.
    4. Point your mouse to the **Call Logs** smart button in the top-right corner.
    5. *(Optional)*: Delete the phone number temporarily to show that the Call button dynamically disappears (re-type and save it to bring it back).
*   **Narration Script**:
    > *"Moving on to Task 2, if we open any Contact record, you'll see a custom inline Call button with a phone icon placed directly next to the Phone number field. This button is configured to be dynamic—it only appears if the contact actually has a phone number. 
    > 
    > Additionally, for Task 5, we have integrated a Call Logs smart button at the top right. This button displays the real-time count of call logs recorded for this specific contact."*

---

### Part 3: Interactive Wizard & Creating a Log (approx. 40 seconds)
*   **On-Screen Action**:
    1. Click the inline **Call** button. (The wizard modal opens).
    2. Point out that the **Customer** and **Phone** fields are auto-filled and read-only (Task 3).
    3. Select **Connected** as the status.
    4. In the **Notes** box, type: *"Discussed project timeline and confirmed database credentials."*
    5. Click the **Save** button. (The wizard saves and closes; note that the smart button count increments).
*   **Narration Script**:
    > *"Now, let's click the Call button. This launches our transient wizard modal for Task 3. The customer's name and phone number are automatically populated as read-only. I'll select the status as Connected and type some call notes. 
    > 
    > When I click Save, the wizard executes our ORM method to create a persistent record in the `phone.call.log` model for Task 4. Notice that the smart button count has instantly updated."*

---

### Part 4: The Phone Menu, List, & Form Views (approx. 40 seconds)
*   **On-Screen Action**:
    1. Click the Odoo Home icon and click the top-level **Phone** menu (Task 6).
    2. Show the **List View**: Point out the custom status badges (Connected in green, Busy in red, etc.).
    3. Click on the log you just created to open the **Form View**.
    4. Highlight the **Date** and **User** fields, showing they are pre-filled with the current date/time and active user admin (Bonus features).
*   **Narration Script**:
    > *"For Task 6, we created a top-level Phone menu. Clicking it opens the Call Logs List View. Here, we've styled the status fields into pastel, color-coded badges matching the Cal.com minimalist design language—green for connected, yellow for pending, red for busy, and purple for no answer.
    > 
    > If we open a log to view the Form View, you'll see that the current datetime and the active user are automatically pre-populated, which ensures audit trail integrity—covering two of our key bonus features."*

---

### Part 5: Kanban & Reporting Analysis Views (approx. 30 seconds)
*   **On-Screen Action**:
    1. Switch to **Kanban View** using the icon at the top right of the view selector (Bonus).
    2. Drag a card from *Pending* to *Connected* (showing Odoo's interactive column tracking).
    3. Switch to the **Pivot View** (grid icon) and **Graph View** (bar chart icon) at the top-right.
*   **Narration Script**:
    > *"As a major bonus requirement, we implemented an interactive Kanban View where calls are grouped into columns by their status. We also added Odoo Graph and Pivot views, enabling management to run business intelligence reports on call activity patterns."*

---

### Part 6: Search, Filters, & Security (approx. 20 seconds)
*   **On-Screen Action**:
    1. Go back to the List view, click the search bar, select the **My Calls** filter, and group by **Status** (Task 6 Search).
    2. Mention security rules (Task 7).
*   **Narration Script**:
    > *"The Search View allows you to search by Customer, Phone, or Status, apply custom filters like 'My Calls', or group by Customer and Date. 
    > 
    > Finally, for Task 7, access rights are defined in the CSV security file to restrict access strictly to Internal Users, keeping sensitive call logs hidden from portal or public users."*

---

### Part 7: Conclusion & Deployment (approx. 10 seconds)
*   **On-Screen Action**: Show the Odoo dashboard or show the Railway/Render URL in the address bar.
*   **Narration Script**:
    > *"The module has also been configured with a Render Blueprint for one-click cloud deployment. This concludes the demo. All technical tasks and bonus requirements are fully functional. Thank you for watching!"*
