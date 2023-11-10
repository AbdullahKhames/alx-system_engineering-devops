Issue Summary
•	The issue was with my driver service I was working on. when pushed it caused bugs that a driver can accept order that was already accepted in case it wasn’t collected from the store.
•	The issue was discovered at 8:00 pm 10/10/2023 so the senior developer 
•	And was solved at 8:30 pm
Timeline
•	All time in GMT
•	Outage toke about 30 minutes
•	Outage began on at 8:00 pm
•	Senior dev notified responsible engineer immidiatly when issue was discovered
•	Issue discovered and reported by the drivers
•	service was restored at 8:30 pm
Root Cause
•	the cause of the issue was not covered check in the service and the code was pushed without testing
Resolution and recovery
•	action taken was a rollback to a previous version of the application and prevent push without testing
Corrective and Preventative Measures
•	prevent issues like this is easy just implement a more thorugh testing before pushing to production
