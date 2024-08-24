Internal Server(500) Error: Postmortem


Incident -Summary

 On Tuesday at 3:30 pm CAT, Johannesburg, the Holberton Software engineering team received numerous client emails reporting an Internal Server 500 error on HolbertonSchool.com, resulting in students encountering difficulties accessing the webpage. I was the sole individual present on-site when the error occurred, as all other team members were engaged in a training session.
Around 4:00 pm, I commenced the debugging process by executing a curl command utilizing the IP address of the Holberton School website within my Linux container to ascertain the status of the website and the nature of the error. The outcome revealed that the internal server error (500) persisted. Consequently, the server had been non-operational for 30 minutes since the initial email notifications were issued. 
The Holberton School website is deployed using the WordPress Lamp stack. As I progress to the next stage of debugging, my focus shifts towards analyzing the error logs for valuable insights. I conducted a thorough check to ascertain the status of Apache, which was found to be operational. Additionally, I meticulously verified the accessibility and functionality of all pertinent ports, confirming that they were operational without any issues.
At 5:30, two hours after initial errors were reported, I found myself devoid of strategies to rectify the issue, prompting me to seek assistance from my colleagues via the workspace chatbot. Following a thorough discussion, the team collectively decided that the most effective course of action entails utilizing strace and tmux to troubleshoot the web server error. The primary objective is to pinpoint the specific process ID that was in operation. Among the three available PIDs, the initial one proved to be non-functional, leading me to focus on the final one. Subsequently, I proceeded to launch the tmux terminal, attaching the PID in one window, while simultaneously executing the initial curl command in another window.

Root Cause and Fix
His meticulous strace and tmux debugging process yielded fruitful outcomes. Through thorough examination, I discerned a discrepancy in the file name - specifically, the file located at /var/www/html/wp-includes/class-wp-locale.phpp. It became apparent that the file extension should have been 'php' instead of 'phpp'. This realization was further reinforced by the error message indicating "no such file or directory". By utilizing the grep command to confirm the precise path of the intended file, I pinpointed the root of the issue to be the incorrect file extension. Subsequently, I crafted a puppet script to rectify the erroneous filename with the accurate one. Executing the puppet script to implement the necessary corrections, followed by running the curl command to validate the resolution of the internal server error, proved successful.
The restoration of the website to its functional state was achieved by 7 pm, marking the culmination of a meticulous error debugging process that spanned approximately 4.5 hours.



Timeline
3:30 pm - Error reports emails recorded.
4:oo pm - Server status check and initial debugging.
5:00 pm - Second debugging stage using tmux and strace.
7:00 pm - Issue resolved.

Review
Deploying tmux and strace in the debugging process made it easier to resolve the internal server error. However, it also identified that fixing an internal server error is trying to find a needle in a haystack. Using WordPress means that the server error has to be fixed manually, by using different debugging mechanisms, Error logging, Automatic recovery attempts, Fallback, and redundancy, this might prolong the process of making the website operational again

